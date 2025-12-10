from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

if __name__ == "__main__":
    print("=== Testing GPT-4o ===")
    run(
        deployment_name='gpt-4o',
        print_request=True,
        print_only_content=False,
    )

    print("\n\n=== Testing Claude 3.7 Sonnet ===")
    run(
        deployment_name='claude-3-7-sonnet@20250219',
        print_request=True,
        print_only_content=False,
    )

    print("\n\n=== Testing Gemini 2.5 Pro ===")
    run(
        deployment_name='gemini-2.5-pro',
        print_request=True,
        print_only_content=False,
    )

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API