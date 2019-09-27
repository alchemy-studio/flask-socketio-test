#!/usr/bin/python3

from time import sleep;
import numpy as np;
from flask_socketio import SocketIO;
from celery import Celery;
from gevent import monkey;

monkey.patch_all();
celery = Celery('worker', broker = 'amqp://guest:guest@localhost:5672');
socketio = SocketIO(message_queue = "amqp://guest:guest@localhost:5672");

@celery.task
def generate(session):

  assert type(session) is str;
  for i in range(10):
    n = np.random.randint(low = 0, high = 10);
    socketio.emit("msg",namespace = "/socket",room = session, data = {'value': n});
    sleep(1);

