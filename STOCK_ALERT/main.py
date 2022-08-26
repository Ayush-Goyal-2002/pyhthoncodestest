import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_KEY = "10HIUUE1H7JUYJMW"
NEWS_KEY = "a26c7671bbb540d79b13eb86fa761e5c"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_PARAMS = { "qInTitle":COMPANY_NAME,
                "apiKey":NEWS_KEY,

}





# newsapi = NewsApiClient(api_key='a26c7671bbb540d79b13eb86fa761e5c')
#
#
# top_headlines = newsapi.get_top_headlines(q='tesla',
#                                           category='business',
#                                           language='en',
#                                           country='us')
# print(top_headlines)

#STOCK PRICE


r = requests.get(STOCK_ENDPOINT,params = {"function" : "TIME_SERIES_DAILY","symbol":"TSLA","apikey" :"10HIUUE1H7JUYJMW" })
data = r.json()["Time Series (Daily)"]
#for getting data of yesterday dynamically
data_list = [value for (key,value) in data.items()]

yesterday = float(data_list[0]["4. close"])
day_before_yesteday = float(data_list[1]["4. close"])

change = yesterday-day_before_yesteday
perc_change = abss(100*change/day_before_yesteday)

if (perc_change>0):
    #getting news
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    article = news_response.json()["articles"]
    three_articles = article[:3]

    formatted_article = [ f"Headline:{article['title']},\nBrief:{article['description']}" for article in three_articles]
    print(formatted_article)




