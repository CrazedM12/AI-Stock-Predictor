import google.generativeai as genai
from flask import Flask, render_template, request

genai.configure(api_key="AIzaSyBCS3hWbjJ0eErHLoPCBX6jZoyqB0Yi8Tg")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ai_response = None

    if request.method == "POST":
        image_file = request.files["chart"]
        user_message = request.form["message"]

        img_bytes = image_file.read()

        strategy = """
MY STRATEGY RULES:

1. First determine if the market is in an uptrend.
2. Look for a LOWER HIGH and a HIGHER LOW.
3. Check if price breaks ABOVE the lower high.
4. Volume should DECREASE during pullback and INCREASE on breakout.
5. If all conditions align → bullish continuation setup.
"""

        prompt = f"""
Analyze the chart using the strategy below.
Do NOT predict the future — only apply the rules.

STRATEGY:
{strategy}

User message: {user_message}
"""

        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(
            [
                prompt,
                {"mime_type": "image/png", "data": img_bytes}
            ]
        )

        ai_response = response.text

    return render_template("index.html", ai_response=ai_response)

if __name__ == "__main__":
    app.run(debug=True)
