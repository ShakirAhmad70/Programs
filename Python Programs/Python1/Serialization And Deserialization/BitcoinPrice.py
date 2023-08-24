import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url) #sending http request to coindesk application/webServer

bitInfo = response.json() #Provides python's dict object
# print(type(bitInfo))

# print(bitInfo)
print("As on :",bitInfo["time"]["updated"])
print("1 Bitcoin price is: $"+bitInfo['bpi']['USD']['rate'])


'''
bitInfo = {
    'time': {
        'updated': 'Aug 15, 2023 19:31:00 UTC',
        'updatedISO': '2023-08-15T19:31:00+00:00', 
        'updateduk': 'Aug 15, 2023 at 20:31 BST'
        },
 
    'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 
    
    'chartName': 'Bitcoin',
    
    'bpi': {
        'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '29,168.3573', 'description': 'United States Dollar', 'rate_float': 29168.3573},
        'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '24,372.8460', 'description': 'British Pound Sterling', 'rate_float': 24372.846},
        'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '28,414.2386', 'description': 'Euro', 'rate_float': 28414.2386}
        }
 }
 
 '''