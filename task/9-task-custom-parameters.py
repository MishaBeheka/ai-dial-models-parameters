from task.app.main import run

# Additional task: Practice with other parameters from OpenAI and Anthropic
# This demonstrates how to use custom parameters via custom_fields configuration

# Example 1: Using OpenAI's reasoning_effort (hypothetical parameter)
def test_openai_custom_parameters():
    print("=== Testing OpenAI Custom Parameters ===")
    run(
        deployment_name='gpt-4o',
        print_request=True,
        print_only_content=False,
        # Custom OpenAI parameters via custom_fields
        custom_fields={
            "configuration": {
                "reasoning_effort": "high",  # OpenAI specific parameter
                "response_format": {"type": "text"}  # Another custom parameter
            }
        }
    )

# Example 2: Using Anthropic's thinking parameter (hypothetical)
def test_anthropic_custom_parameters():
    print("\n\n=== Testing Anthropic Custom Parameters ===")
    run(
        deployment_name='claude-3-7-sonnet@20250219',
        print_request=True,
        print_only_content=False,
        # Custom Anthropic parameters via custom_fields
        custom_fields={
            "configuration": {
                "thinking": True,  # Anthropic specific parameter
                "citations": True  # Another custom parameter
            }
        }
    )

# Example 3: Combining standard and custom parameters
def test_mixed_parameters():
    print("\n\n=== Testing Mixed Parameters ===")
    run(
        deployment_name='gpt-4o',
        print_request=True,
        print_only_content=False,
        # Standard parameters
        temperature=0.7,
        max_tokens=100,
        # Custom parameters
        custom_fields={
            "configuration": {
                "stream_options": {"include_usage": True},
                "tool_choice": "auto"
            }
        }
    )

if __name__ == "__main__":
    print("Testing custom parameters with DIAL API")
    print("Note: Some custom parameters might not be supported by all models")

    # Uncomment the tests you want to run:
    # test_openai_custom_parameters()
    # test_anthropic_custom_parameters()
    # test_mixed_parameters()

    print("Uncomment the function calls above to test custom parameters")

# IMPORTANT: According to DIAL documentation, parameters not in the standard API
# should be provided as: {"custom_fields": {"configuration": {CUSTOM_PARAMETERS}}}
# More info: https://dialx.ai/dial_api#operation/sendChatCompletionRequest
