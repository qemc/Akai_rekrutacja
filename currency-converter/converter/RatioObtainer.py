from genericpath import exists
import json, datetime, urllib.request, os.path
from tokenize import String
import requests 

class RatioObtainer:
    
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        if os.path.isfile(r"ratios.json"):
                with open(r"ratios.json") as f:
                    data = json.load(f)
                    for item in data:
                        
                        print("--------------")
                        print(item["base_currency"])
                        print(self.base)
                        
                        print(item["target_currency"])
                        print(self.target)
                       
                        print("--------------")
                        if item["base_currency"] == self.base and item["target_currency"] == self.target:
                            if str(datetime.datetime.today()) == str(item["date_fetched"]):
                                print("true")
                                return True
                                
                            else:
                                print("false")
                                return False

                    else:
                        print("false")
                        return False
        
    def fetch_ratio(self):
        
        url = 'https://api.exchangerate.host/convert?from='+ self.base + '&to='+ self.target

        response = requests.get(url)
        data = response.json()
        self.save_ratio(float(data["info"]["rate"]))
        print(data["info"]["rate"])
        return float(data["info"]["rate"])
    
    def save_ratio(self, ratio):
        with open(r"ratios.json") as f:
            data = json.load(f)
            date_ = str(datetime.date.today())
            
            
            new_record =   {
                "base_currency": self.base,
                "target_currency": self.target,
                "date_fetched": date_,
                "ratio": ratio
            }
            
            
        with open("ratios.json", "w") as f:
            
            isUpdated = False
            
            for item in data:
                if item["base_currency"] == self.base and item["target_currency"] == self.target:
                        if str(date_) != str(item["date_fetched"]):
                            item["date_fetched"] = date_
                            item["ratio"] = ratio
                            isUpdated = True
                
            
            if isUpdated == False:
                data.append(new_record)
            
            
            json.dump(data, f,indent=4)
        

    def get_matched_ratio_value(self):
         if os.path.isfile(r"ratios.json"):
                with open(r"ratios.json") as f:
                    data = json.load(f)
                    for item in data:
                        if item["base_currency"] == self.base and item["target_currency"] == self.target:
                            return float(item["ratio"])
