import random

# List of possible user greetings
greetings = ["hello", "hi", "hey", "howdy"]

# List of possible chatbot responses
responses = ["Hello!", "Hi there!", "Hey!", "Howdy!"]

# Function to generate chatbot response
def generate_response(user_input):
    if user_input.lower() in greetings:
        return random.choice(responses)
    else:
        return "I'm sorry, I don't understand."

# Main loop
while True:
    user_input = input("User: ")
    response = generate_response(user_input)
    print("Chatbot:", response)
