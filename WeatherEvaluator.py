from AbstractEvaluator import AbstractEvaluator
import weather as yourMom
import json
import pandas as pd

class WeatherEvaluator (AbstractEvaluator):
    def __init__(self,location,cropType):
        super().__init__(location,cropType)
        return
    def evaluate(self, csvFile=''):
        #get the weather dictionary
        yourMom.update(self.getLocation)
        wDict = yourMom.getWeather()
        
        
