import sys
sys.path.append("../evaluators")
from PriceDataEvaluator import PriceDataEvaluator
from WeatherEvaluator import WeatherEvaluator
from MemeEvaluator import MemeEvaluator
#dictates which data evaluator object to get
class DataEvalBuilder (object):
    def __init__(self,location,cropType):
        self.zip = location
        self.crop = cropType

    def setLocation(self,location):
        self.zip = location
    def getLocation(self):
        return self.zip
    def setCropType(self,cropType):
        self.crop = cropType
    def getCropType(self):
        return self.crop

    def get(self,dataType):
        dataType = dataType.lower()
        if dataType == "memes":
            return MemeEvaluator(self.zip,self.crop)
        elif dataType == "weather":
            return WeatherEvaluator(self.zip,self.crop)
        elif dataType == "water":
            return GroundWaterEvaluator(self.zip,self.crop)
        elif dataType == "disease":
            return DiseaseInfoEvaluator(self.zip,self.crop)
        elif dataType == "prices":
            #ok got this one done
            return PriceDataEvaluator(self.zip,self.crop)
        elif dataType == "news":
            return NewsDataEvaluator(self.zip,self.crop)
        else:
            raise LookupError
