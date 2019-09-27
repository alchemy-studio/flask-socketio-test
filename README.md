# flask-socketio-test
this is toy project to show how to develop with flask and socketio.

## install prerequisite packages

install with command

```bash
pip3 install -U flask flask-cors flask-socketio celery gevent
sudo apt install rabbitmq-server
```

celery and socketio need rabbit message queue, so launch it with command

```bash
sudo systemctl start rabbitmq-server
```

## how to launch the server

you need to modify the ip address to yours in server.py.

start workers with the following command, first.

```bash
bash start_workers.sh
```

launch the server with command

```bash
python3 server.py
```

## access the server

access the page with

```
firefox <ip>:5000
```

you will see a serial number generated on the page.

