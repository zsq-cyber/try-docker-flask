from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is running in a dockerized app on DigitalOcean kubernetes cluster!'

if __name__ == "__main__":
    app.run(debug=True, host='localhost')