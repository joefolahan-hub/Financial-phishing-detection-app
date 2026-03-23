import re

def preprocess(text):
    # Handle missing values
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)

    return text