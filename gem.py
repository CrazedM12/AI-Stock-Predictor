from google import genai


client = genai.Client(api_key="AIzaSyBO2JczYYN9BzMb8y-BiqMpF6QlZOdaZyg")




def analyze_chart(image_path, user_message):
    with open(image_path, "rb") as f:
        img_bytes = f.read()
        img_b64 = base64.b64encode(img_bytes).decode()

    strategy = """
MY STRATEGY RULES:

1. First determine if the market is in an uptrend.
2. Look for a LOWER HIGH and a HIGHER LOW.
3. Check if price breaks ABOVE the lower high.
4. Volume should DECREASE during pullback and INCREASE on breakout.
5. If all conditions align → bullish continuation setup.
"""

    prompt = f"""
Analyze the chart using the strategy above.
Do NOT predict the future — only apply the rules.
User message: {user_message}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            {"text": prompt},
            {
                "file_data": {
                    "mime_type": "image/png",
                    "data": img_b64
                }
            }
        ]
    )

    print(response.text)


analyze_chart(
    image_path="D:/My Drive/AP Computer Science/Computer Science 3rd Period 2025-2026/AI Stock Predictor/chart.png",
    user_message="Analyze this chart using my strategy"
)

