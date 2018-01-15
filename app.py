import os, sys
from flask import Flask, request
from pymessenger import Bot


app = Flask(__name__)


PAGE_ACCESS_TOKEN = "EAAbqd2mzriwBAHwhUk2pEYMwJm64s63uEjfXHMbPFwJPoUZAe9y4g7MK4KFMPXtDxUccbaHyOgxqXzOiZADvP7C0LbuQrVn91lKzO50tgcJiHZBrHyavAazgKZA1p4d618JuZAccdn3qT1qZA93QO1LV8FdDF5Xqr6ffqTLLq2QgZDZD"
bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
    # WEBHOOK VERIFICATION
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "secret":
            return "Verification Token Mismatch!", 403
        return request.args["hub.challenge"], 200
    return "Hey", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                # IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    # Extracting text message
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'

                    # Echo
                    response = messaging_text
                    bot.send_text_message(sender_id, response)

    return "ALRIGHT!",    200


def log(message):
    print(message)
    sys.stdout.flush()


'''
def hello_world():
    return 'Finally Done !'
'''
