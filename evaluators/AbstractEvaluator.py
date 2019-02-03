from abc import ABC, abstractmethod

class AbstractEvaluator (ABC):
    def __init__(self,location,cropType):
        self.zip = location
        self.crop = cropType

    def getLocation(self):
        return self.zip
    def getCropType(self):
        return self.crop

    @abstractmethod
    def evaluate(self,csvFile):
        pass
