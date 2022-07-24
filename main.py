from flask import Flask
from flask import jsonify
import redis
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("i", help="Database IP address")
parser.add_argument("-pr", "--port_redis", default="6379", help="Redis Database Port")
parser.add_argument("-p", "--port", default="2500", help="Set application port")
args = vars(parser.parse_args())


REDIS_IP = args["i"]
PORT_REDIS = args["port_redis"]
APP_PORT = args["port"]


app = Flask(__name__)
r = redis.Redis(host=REDIS_IP, port=PORT_REDIS, db=0)


@app.route('/size', methods=['GET'])
def test_GET():
    return jsonify(result=connection(REDIS_IP,PORT_REDIS))


def connection(IP_ADDRES,PORT_REDIS):
    return r.dbsize()

app.run(host='0.0.0.0',port=APP_PORT)
