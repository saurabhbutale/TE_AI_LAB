import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! Welcome to our ecommerce website. How can I assist you today?", "Hey there! How can I help you with your shopping?"]
    ],
    [
        r"how are you ?",
        ["I'm just a bot, but I'm doing well. How about you?", "I don't have feelings like humans do, but I'm functioning well. Thanks for asking!"]
    ],
    [
        r"what is your name ?",
        ["I'm just a chatbot.", "I'm a chatbot, you can call me Chatbot."]
    ],
    [
        r"quit",
        ["Goodbye!", "See you later!", "Bye! Have a great day!"]
    ],
    [
        r"(.*) product (.*)",
        ["Sure, what product are you interested in? Please provide more details so I can assist you better."]
    ],
    [
        r"order status",
        ["To check your order status, please provide your order number."]
    ],
    [
        r"payment options",
        ["We accept various payment methods including credit cards, debit cards, and PayPal. Is there anything else you would like to know?"]
    ],
    [
        r"shipping information",
        ["Our standard shipping takes 3-5 business days. For expedited shipping options, please contact our customer support."]
    ],
    [
        r"return policy",
        ["We offer a 30-day return policy for most items. Please check our website for detailed return instructions."]
    ],
    [
        r"customer support",
        ["Our customer support team is available 24/7 to assist you. You can reach them via phone at 1-800-123-4567 or email at support@example.com."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please rephrase?", "Could you please repeat that?"]
    ]
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

def main():
    print("Hi! Welcome to our ecommerce website. How can I assist you today?")
    chatbot.converse()

if __name__ == "__main__":
    main()
