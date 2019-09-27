#!/usr/bin/python3

from flask import Flask, render_template, session;
from flask_cors import CORS;
from flask_socketio import SocketIO, join_room;
from gevent import monkey;
from uuid import uuid4;
from worker import generate;

monkey.patch_all();
app = Flask(__name__);
app.secret_key = 'breadbread1984';
cors = CORS(app, resources = {r"/*":{"origins":"*"}});
socketio = SocketIO(app, message_queue = "amqp://guest:guest@localhost:5672");

@app.route('/')
def index():
    if 'uid' not in session:
        session['uid'] = str(uuid4())
    # call worker to generate numbers
    generate.delay(session['uid'])
    # return page to receive numbers
    return render_template('index.html')


@socketio.on('connect', namespace='/socket')
def socket_connect():
    print("connected to client!")


@socketio.on('join_room', namespace='/socket')
def on_listening():
    print('listen.....')
    room = str(session['uid'])
    print("joining room " + room)
    join_room(room)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
