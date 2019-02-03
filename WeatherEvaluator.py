from AbstractEvaluator import AbstractEvaluator
import weather
import json
import pandas as pd

class WeatherEvaluator (AbstractEvaluator):
    def __init__(self,location):
        super().__init__(location,"")
        return
    def evaluate(self, csvFile):
        #get the weather dictionary
        weather.update(self.getLocation)
        wDict = weather.getWeather()
        
        
