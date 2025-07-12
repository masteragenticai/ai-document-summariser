"""
OpenAI API Key Diagnostic Tool
Use this to verify your API key is correctly configured
"""

import os
import openai

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ No OPENAI_API_KEY found in environment")
    print("   Please check your Codespaces secrets or environment variables")
    print("")
    print("To set up:")
    print("1. Go to Settings → Secrets and variables → Codespaces")
    print("2. Add a new secret named OPENAI_API_KEY")
    print("3. Restart your Codespace")
else:
    print(f"✅ API key found: {api_key[:10]}...")
    print(f"   Key length: {len(api_key)} characters")
    
    # Check for common issues
    if '\n' in api_key:
        print("⚠️  WARNING: Your API key contains a newline character!")
    if ' ' in api_key:
        print("⚠️  WARNING: Your API key contains spaces!")
    
    try:
        # Set the API key
        openai.api_key = api_key
        
        # Test with a simple API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hello, API works!'"}],
            max_tokens=10
        )
        
        print("✅ API key is valid and working!")
        print(f"   Response: {response.choices[0].message.content}")
        
    except Exception as e:
        print(f"❌ API test failed: {e}")
        print(f"   Error type: {type(e).__name__}")
        print("")
        print("Common issues:")
        print("- Invalid API key (check you copied it correctly)")
        print("- No credits remaining (check your OpenAI account)")
        print("- Network issues (try again)")