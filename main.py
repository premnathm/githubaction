from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to python tutorial"

#app.run(port=5008, debug=True)