from google import genai
from google.genai import types

def research(topic: str, output_file: str = "research_report.txt"):
    MODEL = 'gemini-2.0-pro-exp-02-05'
    client = genai.Client(api_key=api_key)
    history = []

    response = client.models.generate_content(
        model=MODEL,
        contents=f"Write a comprehensive research report on {topic}. Include current research, key findings, and future directions. Use clear sections and academic citations.",
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearchRetrieval)]
        )
    )
    report = response.text

    with open(output_file, "w") as f:
        f.write(report)
    history.append("Initial report generated.")

    while True:
        response = client.models.generate_content(
            model=MODEL,
            contents=(
                f"Here is the current research report:\n{report}\n"
                f"Revisions made so far: {history}\n"
                "Review thoroughly: Are claims supported by current research? Are all major studies included? "
                "Are citations complete and accurate? Is coverage balanced and comprehensive? "
                "Are implications and future directions clear? Is the writing clear and academic? "
                "List specific improvements needed or respond with 'No revisions'."
            ),
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearchRetrieval)]
            )
        )
        revisions = response.text.strip()

        if "no revisions" in revisions.lower():
            return report

        history.append(revisions)
        response = client.models.generate_content(
            model=MODEL,
            contents=f"Apply these revisions while maintaining academic quality and flow:\n{revisions}\nCurrent report:\n{report}",
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearchRetrieval)]
            )
        )
        report = response.text
        with open(output_file, "w") as f:
            f.write(report)
        print("Updated report written.")

if __name__ == "__main__":
    research("psychedelics as a treatment for adhd")
