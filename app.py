import logging
import os
import sys

from flask import Flask, request

from urllib.parse import urlencode
from urllib.request import Request, urlopen

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

GROUPME_API_URL = 'https://api.groupme.com/v3/bots/post'


@app.route('/')
def hello_world():
    app.logger.debug('Hello, World!')
    return 'Hello, World!'


@app.route('/webhook/', methods=['POST'])
def webhook():
    data = request.get_json()
    app.logger.debug('Received: ' + str(data))
    if data['sender_type'] != 'user':
        # Don't process bot messages for now
        return 'OK', 200

    send_message('Hello, ' + data['name'])

    return 'OK', 200


def send_message(msg):
    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text' : msg,
    }
    app.logger.debug('Sending: ' + str(data))
    request = Request(GROUPME_API_URL, urlencode(data).encode())
    urlopen(request).read().decode()


if __name__ == '__main__':  
    app.run()
