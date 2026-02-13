def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to exit")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! Welcome")

        elif user == "how are you":
            print("Bot: I am fine, thank you")

        elif user == "what is your name":
            print("Bot: I am Python Chatbot")

        elif user == "time":
            from datetime import datetime
            print("Bot:", datetime.now().strftime("%H:%M:%S"))

        elif user == "date":
            from datetime import datetime
            print("Bot:", datetime.now().strftime("%d-%m-%Y"))

        elif user == "bye":
            print("Bot: Goodbye")
            break

        else:
            print("Bot: I don't understand")

# Call function
chatbot()       