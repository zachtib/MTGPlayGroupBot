from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    app.logger.debug('Hello, World!')
    return 'Hello, World!'


@app.route('/webhook/', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)

    return 'OK', 200

if __name__ == '__main__':
    app.run()
