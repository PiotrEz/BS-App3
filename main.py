from flask import Flask
from flask import jsonify
import redis


IP_ADDRES = "192.168.0.13"
PORT_REDIS = 6379

app = Flask(__name__)


@app.route('/size', methods=['GET'])
def test_GET():
    return jsonify(result=connection(IP_ADDRES,PORT_REDIS))

def connection(IP_ADDRES,PORT_REDIS):
    r = redis.Redis(host=IP_ADDRES, port=PORT_REDIS,db=0)
    return r.dbsize()

app.run(port=2500)