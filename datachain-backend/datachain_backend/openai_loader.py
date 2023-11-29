"""
Temporary this must be refactored to load multiple different models not just openai
"""
import openai 
import requests 
import json
import os

GPT_MODEL = "gpt-4"

def chat_completion_request(messages, tools=None, tool_choice=None, model=GPT_MODEL):
    api_key = os.environ.get("OPENAI_API_KEY")
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
    }
    json_data = {"model": model, "messages": messages}
    if tools is not None:
        json_data.update({"tools": tools})
    if tool_choice is not None:
        json_data.update({"tool_choice": tool_choice})
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

