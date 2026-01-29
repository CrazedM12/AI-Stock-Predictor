import google.generativeai as genai
import base64

# Your AIza key works with THIS library
genai.configure(api_key="AIzaSyBCS3hWbjJ0eErHLoPCBX6jZoyqB0Yi8Tg")

def analyze_chart(image_path, user_message):
    # Load image as bytes
    with open(image_path, "rb") as f:
        img_bytes = f.read()

    strategy = """
MY STRATEGY RULES:

1. First determine if the market is in an uptrend.
   - An uptrend means price is generally moving upward with higher highs and higher lows.

2. Look for a temporary pullback inside the uptrend.
   - During this pullback, price should form:
     • a LOWER HIGH (LH)
     • a HIGHER LOW (HL)

3. After the LH + HL structure forms, check if price breaks ABOVE the lower high.
   - If price breaks above the LH, this signals continuation of the uptrend.

4. Check volume behavior:
   - Volume should DECREASE during the pullback (LH → HL).
   - Volume should INCREASE on the breakout candle above the LH.

5. If all conditions align:
   - The strategy signals a bullish continuation setup.
"""

    prompt = f"""
Analyze the chart using the strategy below.
Do NOT predict the future — only apply the rules.

STRATEGY:
{strategy}

User message: {user_message}
"""

    model = genai.GenerativeModel("gemini-3-flash-preview")

    response = model.generate_content(
        [
            prompt,
            {"mime_type": "image/png", "data": img_bytes}
        ]
    )

    print(response.text)


# Run it
analyze_chart(
    image_path="D:/My Drive/AP Computer Science/Computer Science 3rd Period 2025-2026/AI Stock Predictor/Chart 2.png",
    user_message="Analyze this chart using my strategy"
)
