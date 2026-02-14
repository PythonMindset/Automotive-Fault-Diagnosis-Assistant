import json
import os
import re
from pathlib import Path

HISTORY_FILE = Path(__file__).parent / "query_history.json"

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def load_history():
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_history(history):
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f, indent=2)
    except IOError as e:
        print(f"Error saving history: {e}")

def get_cached_response(user_input):
    normalized_query = clean_text(user_input)
    history = load_history()
    return history.get(normalized_query)

def save_response(user_input, response):
    normalized_query = clean_text(user_input)
    history = load_history()
    history[normalized_query] = response
    save_history(history)

