"""
Demo script to show hands-on examples of each requirement
Run this to see exactly what each parameter does
"""

from task.app.main import run

def demo_task_2_multiple_choices():
    """Demo: Multiple choices with n parameter"""
    print("\n" + "="*60)
    print("DEMO: Task 2 - Multiple Choices (n parameter)")
    print("="*60)
    print("Question: 'Why is the snow white?'")
    print("Expected: 3 different explanations in the choices array")
    print("\nRunning with n=3...")

    # This will show the different choices in the JSON response

def demo_task_3_temperature():
    """Demo: Temperature effect on creativity"""
    print("\n" + "="*60)
    print("DEMO: Task 3 - Temperature (creativity control)")
    print("="*60)
    print("Question: 'Describe the sound that the color purple makes when it's angry'")
    print("Expected: Very creative, imaginative response")
    print("\nRunning with temperature=0.9...")

def demo_task_4_seed():
    """Demo: Seed for deterministic output"""
    print("\n" + "="*60)
    print("DEMO: Task 4 - Seed (deterministic output)")
    print("="*60)
    print("Question: 'Name a random animal'")
    print("Expected: All 5 choices should be nearly identical")
    print("\nRunning with seed=42, n=5...")

def demo_task_5_max_tokens():
    """Demo: Max tokens limiting response length"""
    print("\n" + "="*60)
    print("DEMO: Task 5 - Max Tokens (length limit)")
    print("="*60)
    print("Question: 'What is token when we are working with LLM?'")
    print("Expected: Response cut off at 10 tokens, finish_reason='length'")
    print("\nRunning with max_tokens=10...")

def demo_task_6_frequency_penalty():
    """Demo: Frequency penalty reducing repetition"""
    print("\n" + "="*60)
    print("DEMO: Task 6 - Frequency Penalty (reduce repetition)")
    print("="*60)
    print("Question: 'Explain the water cycle in simple terms for children'")
    print("Expected: Less repetitive language, more varied vocabulary")
    print("\nRunning with frequency_penalty=1.5...")

def demo_task_7_presence_penalty():
    """Demo: Presence penalty for topic diversity"""
    print("\n" + "="*60)
    print("DEMO: Task 7 - Presence Penalty (topic diversity)")
    print("="*60)
    print("Question: 'What is an entropy in LLM's responses?'")
    print("Expected: Discussion of multiple related topics and concepts")
    print("\nRunning with presence_penalty=1.5...")

def demo_task_8_stop():
    """Demo: Stop parameter for custom stop sequences"""
    print("\n" + "="*60)
    print("DEMO: Task 8 - Stop Parameter (custom stop sequences)")
    print("="*60)
    print("Question: 'Explain the key components of a Large Language Model architecture'")
    print("Expected: Response stops at first double newline, finish_reason='stop'")
    print("\nRunning with stop='\\n\\n'...")

def run_quick_demo():
    """Run a quick demo showing each parameter effect"""
    print("DIAL API Parameters Demo")
    print("=" * 80)
    print("This will demonstrate each parameter with a specific example")
    print("You can see the exact request and response for each requirement")
    print("\n1. Multiple Choices (n=3)")
    print("2. Temperature (creativity)")
    print("3. Seed (deterministic)")
    print("4. Max Tokens (length limit)")
    print("5. Frequency Penalty (less repetition)")
    print("6. Presence Penalty (topic diversity)")
    print("7. Stop Parameter (custom stop)")

    choice = input("\nWhich demo would you like to see? (1-7, or 'all' for all demos): ").strip()

    if choice == '1':
        demo_task_2_multiple_choices()
        # Run actual task 2
        run(deployment_name='gpt-4o', n=3, print_request=True, print_only_content=False)

    elif choice == '2':
        demo_task_3_temperature()
        # Run actual task 3
        run(deployment_name='gpt-4o', temperature=0.9, print_only_content=True)

    elif choice == '3':
        demo_task_4_seed()
        # Run actual task 4
        run(deployment_name='gpt-4o', seed=42, n=5, print_request=True, print_only_content=False)

    elif choice == '4':
        demo_task_5_max_tokens()
        # Run actual task 5
        run(deployment_name='gpt-4o', max_tokens=10, print_request=True, print_only_content=False)

    elif choice == '5':
        demo_task_6_frequency_penalty()
        # Run actual task 6
        run(deployment_name='gpt-4o', frequency_penalty=1.5, print_only_content=True)

    elif choice == '6':
        demo_task_7_presence_penalty()
        # Run actual task 7
        run(deployment_name='gpt-4o', presence_penalty=1.5, print_only_content=True)

    elif choice == '7':
        demo_task_8_stop()
        # Run actual task 8
        run(deployment_name='gpt-4o', stop="\n\n", print_only_content=True)

    elif choice.lower() == 'all':
        # Run all demos in sequence
        for i in range(1, 8):
            input(f"\nPress Enter to run Demo {i}...")
            if i == 1:
                demo_task_2_multiple_choices()
                run(deployment_name='gpt-4o', n=3, print_request=True, print_only_content=False)
            elif i == 2:
                demo_task_3_temperature()
                run(deployment_name='gpt-4o', temperature=0.9, print_only_content=True)
            elif i == 3:
                demo_task_4_seed()
                run(deployment_name='gpt-4o', seed=42, n=5, print_request=True, print_only_content=False)
            elif i == 4:
                demo_task_5_max_tokens()
                run(deployment_name='gpt-4o', max_tokens=10, print_request=True, print_only_content=False)
            elif i == 5:
                demo_task_6_frequency_penalty()
                run(deployment_name='gpt-4o', frequency_penalty=1.5, print_only_content=True)
            elif i == 6:
                demo_task_7_presence_penalty()
                run(deployment_name='gpt-4o', presence_penalty=1.5, print_only_content=True)
            elif i == 7:
                demo_task_8_stop()
                run(deployment_name='gpt-4o', stop="\n\n", print_only_content=True)
    else:
        print("Invalid choice. Please run the script again.")

if __name__ == "__main__":
    run_quick_demo()
