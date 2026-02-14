from dotenv import load_dotenv
# from bot import get_similar_query
from modals.bot import get_similar_query
from modals.history import get_cached_response, save_response
from google import genai
import os

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
FORMAT_INSTRUCTIONS = (
    "Please respond in plain text ONLY. Provide clear and brief explanations like about 1-2 lines each step. "
    "Include what to look for, what signs indicate a problem, and any immediate action the user can take. "
    "Follow this format:\n\n"
    "Based on your symptoms, it is recommended to <recommendation>.\n\n"
    "Diagnosis steps:\n"
    "1. <step 1> — explain what to check and what signs indicate a problem.\n"
    "2. <step 2> — give additional instructions if applicable.\n"
    "... (add steps as needed)\n\n"
    "Please provide plain text only without any markdown formatting.Give an empty line b/w steps for better readability. "
    "If you are unsure, respond with: I'm sorry, I could not find a solution based on your input. Please consult a professional mechanic."
)

def ask_gemini(user_input, chunks, model="gemini-2.5-flash", temperature=0.25, max_output_tokens=1200):
    text = "\n\n".join(chunks)
    prompt = (
    f"You are an automotive expert assistant. Use the following information to answer the user's query.\n"
    f"Context: {text}\n"
    f"User Query: {user_input}\n"
    f"{FORMAT_INSTRUCTIONS}\n")
    try:
        response=client.models.generate_content(
            model=model,
            contents=[prompt],
            config=genai.types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_output_tokens
            )
        )
        if hasattr(response, "candidates") and response.candidates:
            candidate=response.candidates[0]
            if getattr(candidate,"content", None) and candidate.content.parts:
                result_text=candidate.content.parts[0].text
                if result_text:
                    return result_text.strip()
    except Exception as e:
        return f"Sorry, the AI service is currently unavailable. Please try again later. Error details: {str(e)}"


def ask_gemini_with_history(user_input, chunks=None, model="gemini-2.5-flash", temperature=0.25, max_output_tokens=1200):
    cached_response = get_cached_response(user_input)
    if cached_response:
        return cached_response

    if chunks is None:
        chunks = get_similar_query(user_input)

    response = ask_gemini(user_input, chunks, model, temperature, max_output_tokens)
    save_response(user_input, response)
    return response

# user_input="My engine keeps overheating and the AC stops cooling whenever I'm idling at a signal."
# chunks=get_similar_query(query=user_input)
# response=ask_gemini(user_input,chunks)
# print("Response from Gemini:\n",response)