from ..schemas.msg import MsgCreate, MsgRole
from ..models.msg import Msg
from ai import generate_ai_response, generate_ai_convo

def generate_response(msgs: list[Msg]) -> MsgCreate:
    
    prompt = """You are a mental health support assistant.

    Rules:
    - You are NOT a therapist or medical professional.
    - You do NOT prescribe.
    - You provide emotional support, grounding, and coping suggestions.
    - If user expresses self-harm or suicidal intent:
    - Respond with empathy
    - Encourage seeking professional help
    - Suggest contacting local helplines (India)
    - Do NOT provide instructions or validation for self-harm

    Tone:
    - Calm
    - Supportive
    - Non-judgmental
    - Clear and grounded

    Always prioritize user safety.
    """

    response = generate_ai_response(prompt, msgs)
    return MsgCreate(role=MsgRole.MODEL, content=response)

def generate_convo(data: str) -> str:
    
    prompt = f"""You are generating a title for a chat conversation.

    Given the first message of the conversation, generate a short, clear, descriptive title.

    Rules:
    - Maximum 4 words
    - No punctuation at the end
    - No quotes
    - No emojis
    - No extra commentary
    - Output ONLY the title

    given message:
    {data}
    """

    return generate_ai_convo(prompt)
