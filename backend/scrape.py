from datetime import datetime
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot
from bs4 import BeautifulSoup
import requests 
import demjson3
import re 
  
# get html from url
def getHTMLdocument(url): 
     
    response = requests.get(url) 
      
    return response.text 

#get json object from string
def getJsonObject(json):

    word = re.sub(r'[\n]', " ", json)
    word = re.search(r'\'coronavirus-cases-linear\', (.*?)\);', word).group(1)

    return demjson3.decode(word)

#format dates and create dataframe 
def getDataFrame(json_obj):
    dates = []
    for x in json_obj["xAxis"]["categories"]:
        dates.append(datetime.strptime(x, '%b %d, %Y'))

    data = {
        'cases': json_obj["series"][0]["data"]
    }

    dataframe = pd.DataFrame(data)
    dataframe.index = dates

    dataframe.index = dataframe.index.to_period('D')
    return dataframe
 
url_to_scrape = "https://www.worldometers.info/coronavirus/country/south-africa/"

html_document = getHTMLdocument(url_to_scrape) 

soup = BeautifulSoup(html_document, 'html.parser') 
  
json_string = soup.find(string=re.compile("coronavirus-cases-linear"))

json_obj = getJsonObject(json_string)

df = getDataFrame(json_obj)

#create forecast
model = ARIMA(df, order=(5,1,0))
model_fit = model.fit()
output = model_fit.forecast(7)

#save csv
output = pd.DataFrame(output)
output.columns = ["new_cases"]
output.index.name = "date"
output.to_csv('new_cases.csv')

#save plot
output.plot()
pyplot.savefig('new_cases.png')




