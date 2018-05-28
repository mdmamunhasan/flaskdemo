from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = 'development_key'


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
