from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/gandu')
def gandu():
    return """

<html>
  <head>
    <title> Gandu App </title>
  </head>
  <body>
    <h1> Agar tumne ye khola hai, to pakka gandu ho </h1>
    <h4 style="bottom:0"> Made By Gandu </h4>
  </body>
</html>


    """
