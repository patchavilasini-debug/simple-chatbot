import datetime
import random
user_name = ""
facts = [
    "Honey never spoils.",
    "The human brain contains about 86 billion neurons.",
    "Python was created by Guido van Rossum in 1991.",
    "The Earth revolves around the Sun."
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? Because it left its Windows open!",
    "Why do Java developers wear glasses? Because they don't C#."
]

def chatbot_response(user_input):
    global user_name

    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I am an advanced Python chatbot."

    elif user_input.startswith("my name is"):
        user_name = user_input.replace("my name is", "").strip().title()
        return f"Nice to meet you, {user_name}!"

    elif user_input == "who am i":
        if user_name:
            return f"Your name is {user_name}."
        else:
            return "I don't know your name yet. Tell me by typing: My name is <your name>"

    elif user_input == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current time is {current_time}"

    elif user_input == "date":
        current_date = datetime.date.today()
        return f"Today's date is {current_date}"

    elif user_input == "joke":
        return random.choice(jokes)

    elif user_input == "fact":
        return random.choice(facts)

    elif user_input.startswith("calculate"):
        try:
            expression = user_input.replace("calculate", "").strip()
            result = eval(expression)
            return f"Answer = {result}"
        except:
            return "Invalid calculation."

    elif user_input == "help":
        return """
Available Commands:
• hello
• how are you
• what is your name
• my name is <name>
• who am i
• date
• time
• joke
• fact
• calculate 10+20
• bye
"""

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that. Type 'help' to see commands."


# Main Program
print("=" * 50)
print("🤖 ADVANCED CHATBOT")
print("Type 'help' to see available commands")
print("Type 'bye' to exit")
print("=" * 50)

while True:
    user = input("\nYou: ")

    response = chatbot_response(user)
    print("Bot:", response)

    if user.lower() == "bye":
        break