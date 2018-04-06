import logging
import os
import sys

from flask import Flask, request
app = Flask(__name__)

GROUPME_API_URL = 'https://api.groupme.com/v3/bots/post'

@app.route('/')
def hello_world():
    app.logger.debug('Hello, World!')
    return 'Hello, World!'


@app.route('/webhook/', methods=['POST'])
def webhook():
    data = request.get_json()
    app.logger.debug(data)

    return 'OK', 200


def send_message(msg):
    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text' : msg,
    }
    app.logger.debug(data)


if __name__ == '__main__':
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.DEBUG)
    app.run()
