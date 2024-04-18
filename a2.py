import nltk
import random

#Initialize NLTK
nltk.download('punkt')

#Define responses for the chatbot

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well, how about you?", "I'm fine, thank you!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm not sure I understand.", "Can you please rephrase that?", "Sorry, I didn't get that."]
}

#function to generate a response based on user input

def generate_response(message):
    #tokenize the user's input
    words = nltk.word_tokenize(message.lower())

    #check if any known keyword is present in the message
    for key in responses:
        if any(word in words for word in key.split()):
            return random.choice(responses[key])
    
    # if no keyword is found, return a default response
    return random.choice(responses["default"])

#main function to interact with the chatbot

def add_response(keyword, response):
    responses[keyword.lower()] = response
add_response("fuck you", ["oh, fuck you then", "fuck you for saying fuck you to"])
def chat():
    print("Chatbot: Hello! How can I help you? ")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: GoodBye!")
            break
        response = generate_response(user_input)
        print("Chatbot: ", response)

if __name__ == "__main__":
    chat()
        