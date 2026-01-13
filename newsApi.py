import requests as requests
from bs4 import BeautifulSoup
import unicodedata

def TechNews():
    url = "https://www.businesstoday.in/technology"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    outer_data = soup.find_all('div', class_='widget-listing', limit=10)
    finalNews = {}
    count = 1
    for data in outer_data:
        news = data.div.div.a["title"]
        finalNews[count] = news
        count = count + 1
    return finalNews


def GeopoliticsNews():
    url = "https://foreignpolicy.com/tag/geopolitics/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    geopoliticsNews = soup.find_all('h3', class_='hed')
    GeoNews = {}
    count = 1
    for i in geopoliticsNews:
        GeoNews[count] = i.text
        count = count + 1
    return GeoNews

def UnitedStates_News():
    url = "https://www.nbcnews.com/latest-stories//"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    usnews = soup.find_all('h2', class_='wide-tease-item__headline')

    US_News = {}
    count = 1
    for usnews in usnews:
        US_News[count] = usnews.text
        count = count + 1
    return US_News

def IndiaNews():
    url = 'https://www.indiatoday.in/india'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    soup = soup.find('div', class_='story__grid')
    indiaNews = soup.find_all('a')
    india_News = {}
    count = 1
    for indiaNews in indiaNews:
        # news_txt = indiaNews.text.strip()
        title = indiaNews.get('title')
        if title not in india_News.values():
            india_News[count] = title
            count = count + 1
    return india_News


def HealthNews():
    url = "https://www.nbcnews.com/health"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    healthNews = soup.find_all('h2', class_='wide-tease-item__headline')
    health_News = {}
    count = 1
    for news in healthNews:
        health_News[count] = news.text
        count = count + 1
    return health_News

def SportsNews():
    url = 'https://www.rediff.com/sports/headlines'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    sports_news = soup.find_all('h2', class_='hdtitle', limit=20)
    sports_News = {}
    count = 1
    for sports in sports_news:
        sports_News[count] = sports.text
        count = count + 1
    return sports_News

def currencyNews():
    url = 'https://www.zeebiz.com/markets/currency'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    currency = soup.find_all('h3', limit=20)
    currency_News = {}
    count = 1
    for currency in currency:
        currency_News[count] = currency.text
        count = count + 1
    return currency_News




def Asia():
    url = 'https://www.scmp.com/news/asia'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    asia_news = soup.find_all("h2", class_='article__title', limit=20)
    AsiaNews = {}
    title = 'ASIA'
    count = 1
    news_set = set()  # Set to store unique news items

    for data in asia_news:
        news_text = ' '.join(data.text.split())  # Remove extra spaces
        if news_text not in news_set:  # Check if news item is already in set
            AsiaNews[count] = news_text
            news_set.add(news_text)  # Add news item to set
            count += 1

    return AsiaNews



def Europe():
    url ='https://www.aljazeera.com/europe/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    europe_news=soup.find_all("h3",class_='gc__title',limit=20)
    europeNews = ""

    for data in europe_news:
        europeNews  += data.text + '\n'

    dictAfN = {}
    count = 1
    for news_item in europeNews.strip().split('\n'):
        if news_item.strip():
            cleaned_news_item = unicodedata.normalize('NFKD', news_item).encode('ascii', 'ignore').decode('utf-8')
            dictAfN[count] = cleaned_news_item.strip()
            count += 1

    return dictAfN



def middleEast():
    url = 'https://www.aljazeera.com/middle-east/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    middleEast_news=soup.find_all("h3",class_='gc__title',limit=20)
    middleEastNews = ""

    for data in middleEast_news:
        middleEastNews  += data.text + '\n'

    dictAfN = {}
    count = 1
    for news_item in middleEastNews.strip().split('\n'):
        if news_item.strip():
            cleaned_news_item = unicodedata.normalize('NFKD', news_item).encode('ascii', 'ignore').decode('utf-8')
            dictAfN[count] = cleaned_news_item.strip()
            count += 1

    return dictAfN


def Africa():

    url = 'https://www.aljazeera.com/africa/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    Africa_news = soup.find_all("h3", class_='gc__title', limit=20)
    AfricaNews = ""
    title = 'AFRICA'

    for data in Africa_news:
        AfricaNews += data.text + '\n'

    dictAfN = {}
    count = 1
    for news_item in AfricaNews.strip().split('\n'):
        if news_item.strip():
            cleaned_news_item = unicodedata.normalize('NFKD', news_item).encode('ascii', 'ignore').decode('utf-8')
            dictAfN[count] = cleaned_news_item.strip()
            count += 1
    return dictAfN


def asiaPacific():

    url_asia_pacific = 'https://www.aljazeera.com/asia-pacific/'
    req_asia_pacific = requests.get(url_asia_pacific)
    soup_asia_pacific = BeautifulSoup(req_asia_pacific.content, "html.parser")

    asia_pacific_news = soup_asia_pacific.find_all("h3", class_='gc__title', limit=20)
    dict_asia_pacific = {}
    count = 1
    title_asia_pacific = 'ASIA-PACIFIC'

    for data in asia_pacific_news:
        cleaned_news_item = unicodedata.normalize('NFKD', data.text).encode('ascii', 'ignore').decode('utf-8')
        dict_asia_pacific[count] = cleaned_news_item.strip()
        count += 1

    return dict_asia_pacific


def cricket():
    url = 'https://www.cricbuzz.com/cricket-news/latest-news'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    cric= soup.find_all( class_ = "cb-nws-hdln-ancr text-hvr-underline",limit=20)
    cricket= {}
    count = 1
    title = 'CRICKET'
    for arevedya in cric:
            # print(arevedya.text)
        cricket[count] =arevedya.text
        count = count+1
    return cricket

def football():
    url = 'https://www.livemint.com/sports/football-news'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    foot= soup.find_all('h2',class_='headline',limit=20)

    footballdic= {}
    count = 1

    for arevedya in foot:       
        footballdic[count] =arevedya.text.replace('\n', '')
        count = count+1
        
    return footballdic


def hollywood():
    url = 'https://www.pinkvilla.com/entertainment/hollywood'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    h = soup.find_all('h2', class_='heading', limit=20)

    hollywood = {}
    count = 1

    for a in h:
        hollywood[count] = a.text.strip()
        count += 1

    return hollywood

def bollywood(): 
        url = 'https://www.bollywoodhungama.com/bollywood/'
        req = requests.get(url)
        soup = BeautifulSoup(req.content,"html.parser")

        h3= soup.find_all('h3',itemprop="headline",limit=20)
        bollywood={}
        count = 1
        for h3 in h3:
                
                a=h3.find_all('a')
                # print(a)
            
                for link in a:
                    # print(link.text)
                    bollywood[count] =link.text
                    count = count+1

        return bollywood

def anime():
    url = 'https://www.sportskeeda.com/anime'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    h= soup.find_all( class_ = "news-title",limit=20)
    anime={}
    count = 1
    for a in h:
        
            anime[count]= a.text
            count = count+1

    return anime




def stock():
    url = 'https://www.zeebiz.com/markets/stocks'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    stocks = soup.find_all('h3', limit=20)
    stocks_News = {}
    count = 1
    for stocks in stocks:
        stocks_News[count] = stocks.text
        count = count + 1
    return stocks_News




def ipo_News():
    url = 'https://www.zeebiz.com/markets/ipo'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    ipo = soup.find_all('h3', limit=20)
    ipo_News = {}
    count = 1
    for ipo in ipo:
        ipo_News[count] = ipo.text
        count = count + 1
    return ipo_News


def commoditiesNews():
    # commodities
    url = 'https://www.zeebiz.com/markets/commodities'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    commodities = soup.find_all('h3', limit=10)
    commodities_News = {}
    count = 1
    for commodities in commodities:
        commodities_News[count] = commodities.text
        count = count + 1
    return commodities_News

def personal_Finance_News():
    url = 'https://www.zeebiz.com/personal-finance'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    personal_finances = soup.find_all('h3', limit=20)
    personal_finances_News = {}
    count = 1
    for personal_finances in personal_finances:
        personal_finances_News[count] = personal_finances.text
        count = count + 1
    return personal_finances_News

def currencyNews():
    url = 'https://www.zeebiz.com/markets/currency'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    currency = soup.find_all('h3', limit=20)
    currency_News = {}
    count = 1
    for currency in currency:
        currency_News[count] = currency.text
        count = count + 1
    return currency_News

def cryptcurrency():
    url = 'https://crypto.news/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    cryptoNews = soup.find_all('span', class_="home-latest-news-item__title", limit=5)

    crypto_News = {}
    news_titles = set()
    count = 1
    for news in cryptoNews:
        title = news.get_text(strip=True)
        if title not in news_titles:
            crypto_News[count] =  title
            news_titles.add(title)
            count = count +1
    return crypto_News


def world_Economy():
    url = 'https://www.zeebiz.com/economy-infra/world-economy'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    world_economy = soup.find_all('h3', limit=20)
    world_economy_News = {}
    count = 1
    for world_economy in world_economy:
        world_economy_News[count] = world_economy.text
        count = count + 1
    return world_economy_News

def global_Market_News():
    url = 'https://www.zeebiz.com/markets/global-markets'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    globalMarket = soup.find_all('h3', limit=20)
    global_market_News = {}
    count = 1
    for globalMarket in globalMarket:
        global_market_News[count] = globalMarket.text
        count = count + 1
    return global_market_News

def Terrorism():
    url = 'https://www.bing.com/news/search?q=global+terrorism+news&qs=n&form=QBNT&sp=-1&lq=0&pq=globalterrorism+news&sc=1-20&sk=&cvid=3CE588EFB49A4CF98B37D84E95E2608B&ghsh=0&ghacc=0&ghpl='

    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    terrorismNews = soup.find_all('a', class_="title", limit=5)

    terrorism_News = {}
    news_titles = set()
    count = 1
    for news in terrorismNews:
        title = news.get_text(strip=True)
        if title not in news_titles:
            terrorism_News[count] = title
            news_titles.add(title)
            count = count+1
    return terrorism_News()

def weirdNews():
    url = 'https://www.oneindia.com/topic/shocking'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    weirdNews = soup.find_all('div', class_="cityblock-title", limit=5)
    weird_news = {}
    count = 1
    for weird in weirdNews:
            weird_news[count] =  weird.text
            count = count + 1
    return weird_news

def crimeNews():
    url = 'https://www.indiatoday.in/crime'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    crime_in_india = soup.find_all('h2',limit=5)
    crime_news = {}
    count = 1
    title = 'Crime in IndiA'
    for crime in crime_in_india:
            crime_news[count] = crime.text
            count = count + 1

    return crime_news
