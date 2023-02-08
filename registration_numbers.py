from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Ali Khan  \n Hello Docker!\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')