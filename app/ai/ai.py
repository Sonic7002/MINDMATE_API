from google import genai
from google.genai import types
from ..models.msg import Msg
from ..schemas.msg import MsgRole
import os
import requests

client = genai.Client()

def generate_gemini(prompt: str, msgs: list[Msg]) -> str:
    try:
        data = [
            types.Content(
                role="user",
                parts=[types.Part(text=f"INSTRUCTIONS:\n{prompt}")]
            )
        ]

        for msg in msgs:
            data.append(
                types.Content(
                    role=msg.role,
                    parts=[types.Part(text=msg.content)]
                )
            )

            response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=data)
            return response.text
    except:
        raise ValueError("An error has occured try again")


def generate_ai_response(prompt: str, msgs: list[Msg]) -> str:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    models = os.getenv("MODELS").split(',')

    data = [
        {
            "role": MsgRole.USER,
            "content": prompt
        }
    ]

    for msg in msgs:
        data.append(
            {
                "role": msg.role,
                "content": msg.content
            }
        )

    used_model = "not used"
    for model in models:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
                json={
                    "model": model,
                    "messages": data
                }
            )
            content = response.json()
            if response.status_code == 200 and "error" not in content:
                used_model = model
                print("used model:", used_model)
                break
            else:
                continue
        except:
            continue

    if response.status_code == 200:
        try:
            reply = response.json()
            return reply["choices"][0]["message"]["content"]
        except:
            generate_gemini(prompt, msgs)
    else:
        generate_gemini(prompt, msgs)

def generate_ai_convo(prompt: str) -> str:
    try:
        response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt)
    except:
        raise ValueError("An error has occured")
    return response.text
