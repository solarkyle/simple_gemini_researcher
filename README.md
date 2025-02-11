# Gemini Research Assistant

A minimalist yet powerful research paper generator that uses Google's Gemini Pro to create comprehensive, academically-rigorous reports through iterative refinement.

## Description
This tool leverages Gemini Pro's search capabilities to generate research reports through a simple but effective loop:
1. Generates initial research report
2. Reviews for academic quality, citations, and completeness
3. Applies specific improvements
4. Repeats until quality standards are met

## Features
- Clean, single-function design
- Built-in fact-checking through Google Search integration
- Iterative improvement cycle
- Produces well-structured academic content with proper citations
- Saves progress to file after each iteration

## Usage
```python
from research import research

# Generate a research report
report = research("the effects of psychedelics on mental health")
```

## Requirements
- Google Gemini API key
- Python 3.7+
- google.genai

## Installation
```bash
pip install google.generativeai
```

## Example Output
See [`examples/psychedelics_adhd_research.md`](examples/psychedelics_adhd_research.md) for a sample research report generated by this tool, demonstrating:
- Academic writing quality
- Proper citation usage
- Risk/benefit analysis
- Integration of multiple sources


## License
MIT

## Acknowledgments
Built with Google's Gemini Pro API
