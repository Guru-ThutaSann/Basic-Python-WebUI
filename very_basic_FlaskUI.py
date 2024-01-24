from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is my Python Webpage!'

if __name__ == '__main__':
    app.run(port=9697)
