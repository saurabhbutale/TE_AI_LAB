def greet():
    responses = ["Hi there! How can I help you today?", "Hello! What can I assist you with?", "Hey! What do you need help with?"]
    return responses[0]  # Always returns the first greeting

def respond(user_input):
    responses = {
        "hello": ["Hi!", "Hello!", "Hey there!"],
        "how are you?": ["I'm just a bot, but I'm doing well. How about you?", "I don't have feelings like humans do, but I'm functioning well. Thanks for asking!"],
        "goodbye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
        "thanks": ["You're welcome!", "No problem!", "Happy to help!"],
        "ecommerce": ["Welcome to our ecommerce website! How can I assist you with your shopping today?", "Hello! Are you looking for anything specific on our ecommerce platform?"],
        "product inquiry": ["Sure, what product are you interested in? Please provide more details so I can assist you better."],
        "order status": ["To check your order status, please provide your order number."],
        "help": ["Sure, I can help you with various things such as product inquiries, order status, and general assistance. What do you need help with?"],
        "thank you": ["You're welcome!", "No problem!", "Happy to help!"],
        "payment options": ["We accept various payment methods including credit cards, debit cards, and PayPal. Is there anything else you would like to know?"],
        "shipping information": ["Our standard shipping takes 3-5 business days. For expedited shipping options, please contact our customer support."],
        "return policy": ["We offer a 30-day return policy for most items. Please check our website for detailed return instructions."],
        "customer support": ["Our customer support team is available 24/7 to assist you. You can reach them via phone at 1-800-123-4567 or email at support@example.com."]
    }
    
    if user_input.lower() in responses:
        return responses[user_input.lower()][0]  # Always returns the first response
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print(greet())
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            print(respond(user_input))
main()
'''if __name__ == "__main__":
    main()'''
