import pyttsx3
import datetime
import api
import json
import requests

news_key = api.news_api

def main():
    print("HELLO WORLD")

    # SPEAK MODULE
    # engine = pyttsx3.init()
    # engine.say('HELLO SIR GOOD EVENING')
    # engine.runAndWait

    # DATE AND TIME MODULE
    # print(datetime.datetime.now().strftime("%H : %M : %S"))
    # print(datetime.datetime.now().strftime("%Y %m %d %A  %H:%M:%S"))

    # NEWSAPI MODULE
    # url = 'https://newsapi.org/v1/articles'
    # url = f"http://newsapi.org/v2/top-headlines?country=in&apiKey={news_key}"
    # response= requests.get(url)
    # news_page = response.json()
    # article = news_page["articles"]
    # results = []
    # for ar in article:
    #     results.append(ar["title"])
    # for i in range(len(results)):
    #     print(i+1,results[i])
    # for aritcle in news_page['articles']:
    #     print(aritcle["title"])
    

if __name__ == "__main__":
    main()