from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/data")
def parse_inputs():
    zip = int(request.args.get('zip'))
    crop_list = request.args.get('crops').split(',')
    soybeanPriceData = "./data/soybean_price.csv"
    builder = DataEvaluatorBuilder(zip,crop_list[0])
    evaluator = builder.get("prices")
    evaluator.evaluate()

    json_as_str = ''
    with open("./jsons/" +  str(zip) + str(cropt_list[0]) + ".json") as f:
        json_as_str f.read()
        
    return json_as_str
