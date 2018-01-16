import os, sys
from flask import Flask, request
from pymessenger.bot import Bot



app = Flask(__name__)


PAGE_ACCESS_TOKEN = "EAAbqd2mzriwBADGeih5R8l2pAvAjKaxfX3AUmv3tm2uIYGLYiHnk3iHH8Fu5DDRMrOjcqRuW3tdGsxxFIXeql3IdPJv27ZB1wGGlu0tHt5rp74LAeiiUoZBmbfcdpQBoT6bsOMD7wwUUrUYVs6wnkTJOVhSXWHZBFvzt9cxFAZDZD"
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
                    '''
                    response = messaging_text
                    bot.send_text_message(sender_id, response)
                    '''
    return "ALRIGHT!",    200
'''
def interactive(self, context=None):
    """Runs interactive command line chat between user and bot. Runs
        indefinitely until EOF is entered to the prompt.
        context -- optional initial context. Set to {} if omitted
    """
    if context is None:
            context = {}

    # input/raw_input are not interchangeable between Python 2 and 3
    try:
        input_function = input
    except NameError:
        input_function = input

    history = InMemoryHistory()
    while True:
        try:
            message = prompt(INTERACTIVE_PROMPT, history=history, mouse_support=True).rstrip()
        except (KeyboardInterrupt, EOFError):
            return
        print(self.message(message, context))
'''

def log(message):
    print(message)
    sys.stdout.flush()


'''
def hello_world():
    return 'Finally Done !'
'''
