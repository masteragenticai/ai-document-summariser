import os
import openai

api_key = os.getenv("OPENAI_API_KEY")
print(f"API key found: {api_key[:10]}...")

try:
    openai.api_key = api_key
    # Test with old API style (matching openai==0.28.1)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say 'Hello, API works!'"}],
        max_tokens=10
    )
    print("✅ API key is valid!")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"❌ Error: {e}")
    print(f"Error type: {type(e).__name__}")