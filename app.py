from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # WEBHOOK VERIFICATION
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "secret":
            return "Verification Token Mismatch!", 403
        return request.args["hub.challenge"], 200
    return "Hey", 200



'''
def hello_world():
    return 'Finally Done !'
'''
