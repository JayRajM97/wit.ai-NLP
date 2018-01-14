from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Finally Done !'

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
