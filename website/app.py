from flask import Flask, render_template, request
from google import genai

client = genai.Client(api_key="AIzaSyBQmGHXe96veojsKvBaWyLTDOqrQ1KjDoY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ai_response = None

    if request.method == "POST":
        chart = request.files["chart"]
        chart_bytes = chart.read()

        user_message = request.form["message"]

        strategy = """
Analyze the chart using this strategy:

1. Identify the trend direction.
2. Look for a lower high and a higher low.
3. Confirm a breakout above the lower high.
4. Volume should decrease during pullback and increase on breakout.
5. Only describe what the chart shows — do NOT predict the future.
"""

        prompt = f"{strategy}\n\nUser message: {user_message}"

        # GEMINI‑3 FORMAT (correct for google-genai 1.63.0)
        result = client.models.generate_content(
            model="gemini-3-flash-preview",
            input=[
                prompt,
                genai.types.Blob(
                    mime_type="image/png",
                    data=chart_bytes
                )
            ]
        )

        ai_response = result.output_text

    return render_template("index.html", ai_response=ai_response)

if __name__ == "__main__":
    app.run(debug=True)
