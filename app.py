from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # WEBHOOK VERIFICATION
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub challenge"):
        if not request.args.get("hub.verify_token") == "HELLO":
            return "Verification Token Mismatch!", 403
        return request.args["hub.challenge"], 200
    return "125577799", 200



'''
def hello_world():
    return 'Finally Done !'
'''


@app.route('/gandu')
def gandu():
    return """

<html>
  <head>
    <title> Gandu Abhisex </title>
  </head>
  <body>
    <h1> Agar tumne ye khola hai, to pakka gandu ho </h1>
    <h4 style="bottom:0"> Made By Gandu Abhisex </h4>
  </body>
</html>


    """
