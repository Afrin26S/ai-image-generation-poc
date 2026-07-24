BLOCKED_WORDS = [
    "nudity",
    "nude",
    "porn",
    "sex",
    "violence",
    "murder",
    "weapon",
    "gun",
    "bomb",
    "drugs"
]

def is_safe_prompt(prompt):
    prompt = prompt.lower()

    for word in BLOCKED_WORDS:
        if word in prompt:
            return False

    return True