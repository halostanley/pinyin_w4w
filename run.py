# coding=UTF-8
import redis
import threading
import requests
import json
import time
import logging
import local_pytranslate
from flask import Flask, request, jsonify, render_template, jsonify, current_app
from flask_cors import CORS
app = Flask(__name__, template_folder='templates')
CORS(app, resources=r'/*')

###############################################################################
logging.basicConfig(
    format='[%(asctime)s] [%(levelname)s] [%(processName)s] [%(threadName)s] : %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler("flask_runtime_log.txt")
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s, %(name)s, [%(levelname)s] : %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)
###############################################################################

def get_connection():
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r


@app.route("/", methods=["POST", "GET"])
def hello():
    return render_template('index.html')


@app.route("/translate", methods=["POST", "GET"])
def translate():
    text = request.form.get('src_text')
    translator = local_pytranslate.LocalPyTranslte()
    res = translator.translate(text)
    map = {}
    map["text"] = res["text"]
    map["pinyin"] = res["pinyin"]
    return jsonify(map)


@app.route("/acticles", methods=["GET"])
def translate_acticles():
    red = get_connection()
    acticles_str = red.get('readhub')
    acticles_l = json.loads(acticles_str)
    return render_template('acticles.html', acticles=acticles_l)


@app.route("/ent", methods=["GET"])
def ent():
    red = get_connection()
    acticles_str = red.get('tencent_news_ent')
    acticles_l = json.loads(acticles_str)
    return render_template('ent.html', acticles=acticles_l)


@app.route("/finance", methods=["GET"])
def finance():
    red = get_connection()
    acticles_str = red.get('tencent_news_finance')
    acticles_l = json.loads(acticles_str)
    return render_template('finance.html', acticles=acticles_l)


@app.route("/tech", methods=["GET"])
def tech():
    red = get_connection()
    acticles_str = red.get('tencent_news_tech')
    acticles_l = json.loads(acticles_str)
    return render_template('tech.html', acticles=acticles_l)


@app.route("/l", methods=["GET"])
def lists_index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=False)
