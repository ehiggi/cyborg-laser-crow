from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/data")
def parse_inputs():
    zip = int(request.args.get('zip'))
    crop_list = request.args.get('crops').split(',')
    barleyPriceData = "./data/barley_price.csv"
    cotttonPriceData = "./data/cotton_price.csv"
    cornPriceData = "./data/corn_price.csv"
    soybeanPriceData = "./data/soybean_price.csv"
    wheatPriceData = "./data/wheat_price.csv"
    cropDict = {"Corn": '', "Cotton": '', "Barley": '', "Soybean": '', "Wheat": ''}
    # the dropdown in the UI should use these keys exactly
    data = {"Corn": cornPriceData,
            "Cotton": cottonPriceData,
            "Barley": barleyPriceData,
            "Soybean": soybeanPriceData,
            "Wheat": wheatPriceData}
    for crop in crop_list:
        # get the correct evaluator for each type of crop
        builder = DataEvaluatorBuilder(zip, data[crop])
        evaluator = builder.get("prices")
        # the evaluator prettifys the data
        evaluator.evaluate()
        # do something with the json file
        with open("./jsons/" + str(zip) + str(data[crop]) + "price.json") as f:
            cropDict[data[crop]] = f.read()

    return cropDict