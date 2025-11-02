import requests
from bs4 import BeautifulSoup as bs

def get_price():
    page = requests.get('https://www.tgju.org/')

    if page.status_code !=200:
      return None
    soup = bs(page.text , "html.parser")
    obj = {
       
        'دلار' : soup.find('tr' , {"data-market-row" : 'price_dollar_rl'})["data-price"],
        'یورو' : soup.find('tr' , {"data-market-row" : 'price_eur'})["data-price"],
        'سکه امامی' : soup.find('tr' , {"data-market-row" : 'retail_sekee'})["data-price"],
        'نیم سکه' : soup.find('tr' , {"data-market-row" : 'retail_nim'})["data-price"],
        'ربع سکه' : soup.find('tr' , {"data-market-row" : 'retail_rob'})["data-price"],
        'طلا 18 عیار' : soup.find('tr' , {"data-market-row" : 'geram18'})["data-price"]

    }
    return obj
  
