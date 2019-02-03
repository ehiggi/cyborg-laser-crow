from AbstractEvaluator import AbstractEvaluator
import csv
import json
import re
import pandas as pd

class PriceDataEvaluator (AbstractEvaluator):
    def __init__(self,location,cropType):
        super().__init__(location,cropType)
        return

    def evaluate(self,csvFile):
        df = pd.read_csv(csvFile,header = 0,keep_default_na=False)
        #get the headers to rename
        rename = []
        for header in df.columns:
##            if "PRICE RECEIVED, MEASURED IN $ / BU  -  <b>VALUE</b>" in header:
            if re.search("PRICE RECEIVED.*<b>VALUE",header):
                rename.append((header,"PRICE"))
##            elif "YIELD, MEASURED IN BU / ACRE  -  <b>VALUE</b>" in header:
            elif re.search("YIELD.*<b>VALUE",header):
                rename.append((header,"YIELD"))
	#rename them
        for h in rename:
            df.rename({h[0]:h[1]},axis = "columns", inplace= True)
        #only keep the relevent columns
        rel = df.filter(items=["Year","PRICE","YIELD"])
        #only keep the first 10 entries
        f10 = rel.filter(items = [1,2,3,4,5,6,7,8,9,10],axis=0)
        #make a json based on the location/croptype
        json = "./jsons/" + str(self.getLocation()) + str(self.getCropType()) \
               + "price.json"
        f10.to_json(json)



                        
    
