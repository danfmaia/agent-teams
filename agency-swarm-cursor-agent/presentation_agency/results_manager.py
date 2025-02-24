import os
import json
from datetime import datetime
import atexit
import signal


class ResultsManager:
    """
    Manages the persistence of intermediary results for the agency.
    """

    def __init__(self, base_dir="results"):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)

        # Create a session directory with timestamp
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_dir = os.path.join(base_dir, self.session_id)
        os.makedirs(self.session_dir, exist_ok=True)

        # Register cleanup handlers
        atexit.register(self._cleanup)
        signal.signal(signal.SIGINT, self._signal_handler)

        # Keep track of unsaved changes
        self._pending_changes = []
        self._last_save = datetime.now()

    def save_result(self, agent_name: str, stage: str, data: dict):
        """
        Saves intermediary results for an agent.
        """
        try:
            filename = f"{agent_name}_{stage}.json"
            filepath = os.path.join(self.session_dir, filename)

            # Add to pending changes
            self._pending_changes.append({
                'filepath': filepath,
                'data': {
                    'timestamp': datetime.now().isoformat(),
                    'agent': agent_name,
                    'stage': stage,
                    'data': data
                }
            })

            # Force save if too many pending changes or too much time passed
            if len(self._pending_changes) >= 5 or (datetime.now() - self._last_save).seconds >= 30:
                self._save_pending_changes()

            return filepath
        except Exception as e:
            print(f"Warning: Failed to save result: {str(e)}")
            return None

    def _save_pending_changes(self):
        """
        Save all pending changes to disk.
        """
        for change in self._pending_changes:
            try:
                with open(change['filepath'], 'w', encoding='utf-8') as f:
                    json.dump(change['data'], f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(
                    f"Warning: Failed to save to {change['filepath']}: {str(e)}")

        self._pending_changes = []
        self._last_save = datetime.now()

    def load_latest_result(self, agent_name: str, stage: str) -> dict:
        """
        Loads the latest result for an agent and stage.
        Returns None if no result exists.
        """
        try:
            # Save any pending changes first
            self._save_pending_changes()

            # List all session directories
            sessions = sorted([d for d in os.listdir(self.base_dir)
                               if os.path.isdir(os.path.join(self.base_dir, d))],
                              reverse=True)

            # Look for the latest result in all sessions
            for session in sessions:
                filename = f"{agent_name}_{stage}.json"
                filepath = os.path.join(self.base_dir, session, filename)

                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        return json.load(f)

            return None
        except Exception as e:
            print(f"Warning: Failed to load result: {str(e)}")
            return None

    def get_session_path(self, filename: str) -> str:
        """
        Gets the full path for a file in the current session directory.
        """
        return os.path.join(self.session_dir, filename)

    def _cleanup(self):
        """
        Cleanup method called when the program exits normally.
        """
        try:
            self._save_pending_changes()
        except:
            pass

    def _signal_handler(self, signum, frame):
        """
        Handle interruption signals by saving pending changes.
        """
        print("\nSaving pending changes before exit...")
        self._cleanup()
        # Re-raise the signal
        signal.default_int_handler(signum, frame)
