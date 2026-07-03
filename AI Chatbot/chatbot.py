import json

with open("responses.json", "r") as file:
    responses = json.load(file)

def get_response(user_message):
    user_message = user_message.lower()

    if user_message in responses:
        return responses[user_message]

    return "Sorry, I don't understand that."