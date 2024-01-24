from flask import Flask
import webbrowser

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is my Python Webpage!'

def open_browser():
    # Open the default web browser with the Flask app URL
    webbrowser.open_new('http://localhost:9697')

if __name__ == '__main__':
    # Start the Flask app in a separate thread
    from threading import Thread
    Thread(target=open_browser).start()

    # Run the Flask app
    app.run(port=9697)
