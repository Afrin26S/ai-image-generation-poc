from safety import is_safe_prompt

prompt = input("Enter image prompt: ")

if not is_safe_prompt(prompt):
    print("Blocked by safety guardrails.")
else:
    print("Prompt approved.")
    print("Ready for image generation.")