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
The tool generates comprehensive research reports with:
- Clear section structure
- Academic citations
- Balanced viewpoints
- Risk assessments
- Future research directions

## Contributing
Open to contributions! Keep it simple.

## License
MIT

## Acknowledgments
Built with Google's Gemini Pro API
