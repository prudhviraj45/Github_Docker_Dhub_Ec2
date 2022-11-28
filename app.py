from flask import Flask, jsonify
import time
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"Time of Call Home Page change abcd": time.time()})

@app.route("/one")
def one():
    return jsonify({"Time of Call One": time.ctime()})

@app.route("/two")
def two():
    return jsonify({"Time of Call Two": time.time()})

@app.route("/three")
def three():
    return jsonify({"Time of Call Three": time.time()})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
