from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/data")
def parse_inputs():
    zip = int(request.args.get('zip'))
    crop_list = request.args.get('crops').split(',')
    pass
