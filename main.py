from llm import ask_ai

def main():
    print("Smart AI Assistant Started (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        response = ask_ai(user_input)
        print("AI:", response)

if __name__ == "__main__":
    main()