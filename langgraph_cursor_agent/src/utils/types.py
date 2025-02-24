from typing import TypedDict, List, Dict, Optional


class PDFContent(TypedDict):
    text: str
    formulas: List[str]
    data_for_graphs: List[Dict]
    sections: List[Dict[str, str]]


class TranslatedContent(TypedDict):
    sections: List[Dict[str, str]]
    formulas: List[str]
    technical_terms: Dict[str, str]


class SlideContent(TypedDict):
    title: str
    content: str
    layout: str
    elements: List[Dict]


class Presentation(TypedDict):
    slides: List[SlideContent]
    total_time: int
    current_version: int


class ReviewFeedback(TypedDict):
    accuracy_score: float
    grammar_score: float
    timing_score: float
    suggestions: List[str]
    slide_specific_feedback: Dict[int, List[str]]


class AgentState(TypedDict):
    pdf_content: Optional[PDFContent]
    translated_content: Optional[TranslatedContent]
    presentation: Optional[Presentation]
    review_feedback: Optional[ReviewFeedback]
    status: str
    current_agent: str
    messages: List[Dict]
    errors: List[str]
