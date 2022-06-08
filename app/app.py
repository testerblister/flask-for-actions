from flask import Flask

app = Flask(__name__)

@app.route('/apollo')
def apollo():
    return "The eagle has landed"

if __name__ == '__main__':
    app.run(port=5544)
