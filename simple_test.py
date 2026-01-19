#!/usr/bin/env python3
"""
Simple test with basic model names
"""
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def test_simple():
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    
    # Try different model names
    model_names = [
        'gemini-pro',
        'gemini-1.5-pro',
        'gemini-1.0-pro',
        'models/gemini-pro',
        'models/gemini-1.5-pro'
    ]
    
    for model_name in model_names:
        try:
            print(f"🧪 Testing model: {model_name}")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content("Hello, how are you?")
            print(f"✅ SUCCESS with {model_name}")
            print(f"Response: {response.text[:100]}...")
            return model_name
        except Exception as e:
            print(f"❌ Failed with {model_name}: {str(e)[:100]}...")
    
    return None

if __name__ == "__main__":
    working_model = test_simple()
    if working_model:
        print(f"\n🎉 Working model found: {working_model}")
    else:
        print("\n❌ No working models found")