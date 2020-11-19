"""
SimpleKV as a Flask Service.
"""

import logging
import queue

from flask import Flask, request, jsonify, Response
from simplekv import SimpleKV

app = Flask(__name__)

# String <-> SimpleKV
kvstore = {}
# Event queue
event_queue = queue.SimpleQueue()

def event_stream():
    """
    Yield Events from the event queue for watch functionality.
    """
    while True:
        yield "{}\n".format(event_queue.get(block=True))


@app.route("/")
def say_hi():
    """
    Hi...
    """
    return "Hello from SimpleKV"


@app.route("/put/<store_name>", methods=['PUT'])
def put_value_in_store_handler(store_name):
    """
    PUT HTTP Endpoint for putting values in store.
    """
    data_set_from_request = request.get_json(force=True)

    if store_name not in kvstore:
        logging.info("PUT :: INIT STORE %s", store_name)
        event_queue.put_nowait("PUT :: INIT STORE {}".format(store_name))
        kvstore[store_name] = SimpleKV()

    for k,v in data_set_from_request.items():
        logging.info("PUT :: Set %s = %s in %s", k,v,store_name)
        event_queue.put_nowait("PUT :: Set {} = {} in {}".format(k,v,store_name))
        kvstore[store_name].put(k,v)

    return jsonify({"result": "success"})


@app.route("/get/<store_name>/<key>", methods=["GET"])
def get_value_from_store_handler(store_name, key):
    """
    GET HTTP Endpoint for getting values from store.
    """
    if store_name in kvstore:

        if kvstore[store_name].exists(key):
            logging.info("GET :: KEY %s exists in %s", key, store_name)
            event_queue.put_nowait("GET :: KEY {} exists in {}".format(key, store_name))
            return (jsonify({"result": kvstore[store_name].get(key)}), 200)

        logging.info("GET :: KEY %s doesnot exists in %s", key, store_name)
        event_queue.put_nowait("GET :: KEY {} doesnot exists in {}".format(key, store_name))
        return (jsonify({"result": "not_found"}), 404)

    logging.info("GET :: %s store is not initialized.", store_name)
    event_queue.put_nowait("GET :: %s store is not initialized".format(store_name))
    return (jsonify({"result": "not_found"}), 404)

@app.route('/watch')
def watch_event_stream_handler():
    """
    Stream the events published to the Queue
        $ curl -N http://localhost:5000/watch
        PUT :: INIT STORE hello
        PUT :: Set arg1 = val1 in hello
        GET :: KEY 123 doesnot exists in hello
    """
    return Response(event_stream(), mimetype="text/event-stream")


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    app.run(threaded=True)
