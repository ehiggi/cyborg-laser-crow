from AbstractEvaluator import AbstractEvaluator
import csv
import json
import re
import pandas as pd
from google_images_download import google_images_download

class MemeEvaluator (AbstractEvaluator):
    def __init__(self,location,cropType):
        super().__init__(location,cropType)
        return

    def evaluate(self):
        keyword = self.getCropType() + " meme"
        #instantiate a download object
        response = google_images_download.googleimagesdownload()
        #create a qwery
        arguments = {"keywords":keyword,
                     "limit":5,
                     "print_urls":False,
                     "safe_search":"-sa"}
        #download the memes - puts them in ./downloads/[keywords]
        paths = response.download(arguments)
        


                        
    
