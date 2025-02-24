# Presentation Generator System

This system automatically generates a PowerPoint presentation in Portuguese about throughput estimation based on a PDF article.

## Prerequisites

- Anaconda or Miniconda
- OpenAI API key (set in `.env` file)
- Input PDF file in `input/throughput_estimation_article.pdf`

## Installation

1. Create and activate a new local environment:

```bash
conda create -p ./env python=3.10
conda activate ./env
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure your `.env` file contains:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

With the local environment activated, run:

```bash
python presentation_generator.py
```

The script will:

1. Extract content from the PDF
2. Organize it into presentation format
3. Translate the content to Portuguese
4. Generate visualizations
5. Create a PowerPoint presentation

The final presentation will be saved as `apresentacao_throughput.pptx`.

## Note

The environment is created locally in the `./env` folder. To deactivate it:

```bash
conda deactivate
```

To remove the environment completely:

```bash
rm -rf ./env
```
