from AbstractEvaluator import AbstractEvaluator
import weather as yourMom
import json
import pandas as pd
from flask import jsonify

class WeatherEvaluator (AbstractEvaluator):
    def __init__(self,location,cropType):
        super().__init__(location,cropType)
        return
    def evaluate(self, csvFile=''):
        #get the weather dictionary
        yourMom.update(self.getLocation())
        wDict = yourMom.getWeather()
##        weatherJson = "./jsons/" + str(self.getLocation()) + "weather.json"
##        with open (weatherJson,'w') as f:
##            f.write(jsonify(wDict))
        return jsonify(wDict)
        
