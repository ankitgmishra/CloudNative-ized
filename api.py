
from flask import Blueprint, redirect, render_template, request, jsonify,session, url_for
import ipl
from tinydb import TinyDB, Query

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import newsApi as news

# from auth import login_manager,login_required,login_user,
db = TinyDB('users.json')

api = Blueprint('api', __name__)

limiter = Limiter(key_func=get_remote_address)


# @api.route('/api_limit_page')
@api.errorhandler(429)
def api_limit_page(e):
    # daybalance = request.args.get('daybalance')
    return render_template('api_limit_page.html',daybalance=session["rate_limit_day"])


@api.route('/api/teams',methods=['GET'])
@limiter.limit("3 per hour;72 per day")
def teams():
    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    teams = ipl.teamsAPI()
    return jsonify(teams)


@api.route('/api/teamvteam')
@limiter.limit("3 per hour;72 per day")
def teamvteam():
    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response =ipl.teamVteamAPI(team1,team2)
    print(response)
    return jsonify(response)



@api.route('/api/teamrecord')
@limiter.limit("3 per hour;72 per day")
def teamrecord():
    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})


    team = request.args.get('team')
    response =ipl.teamRecord(team)
    print(response)
    return jsonify(response)

@api.route('/api/batsmanrecord')
@limiter.limit("3 per hour;72 per day")
def batsmanrecord():
    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})


    batter = request.args.get('batter')
    response = ipl.batsmanrecord(batter)
    return jsonify(response)

@api.route('/api/seasonwinner')
@limiter.limit("3 per hour;72 per day")
def seasonwinner():
    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})


    SeasonWinner= ipl.seasonwinner()
    return jsonify(SeasonWinner)

@api.route('/api/venues')
@limiter.limit("3 per hour;72 per day")
def venue():
     
    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    venues = ipl.venues()
    return jsonify(venues)

@api.route('/api/teamatvenue')
@limiter.limit("3 per hour;72 per day")
def teamvenue():
     
    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    team = request.args.get('team')
    venue = request.args.get('venue')
    teamatvenue = ipl.teamatvenue(team,venue)
    return jsonify(teamatvenue)

@api.route('/api/batsmanruns')
@limiter.limit("3 per hour;72 per day")
def batsmanruns():

    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    batsman = ipl.allbatsmanstats()
    return jsonify(batsman)

@api.route('/api/noofsix')
@limiter.limit("3 per hour;72 per day")
def noofsix():

    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    noofsix = ipl.noofsix()
    return jsonify(noofsix)

@api.route('/api/powerhitters')
@limiter.limit("3 per hour;72 per day")
def powerhittersoflast5overs():

    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    powerhitter = ipl.powerhitters()
    return jsonify(powerhitter)

@api.route('/api/batsman-runs-against-all-teams')
@limiter.limit("3 per hour;72 per day")
def batsmanvsall():

    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    batsman = request.args.get('batsman')
    batsman= ipl.batsmanvsall(batsman)
    return jsonify(batsman)





#  News 




@api.route('/api/')
@limiter.limit("3 per hour;72 per day")
def get_news():
    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})



    select = request.args.get('news')
    if select == 'technology':
        techNews = news.TechNews()
        return jsonify(techNews)
    elif select == 'crime':
        crimeNews = news.crimeNews()
        return jsonify(crimeNews)
    elif select == 'usa':
        us_News = news.UnitedStates_News()
        return jsonify(us_News)
    elif select == 'india':
        india_News = news.IndiaNews()
        return jsonify(india_News)
    elif select == 'health':
        health_news = news.HealthNews()
        return jsonify(health_news)
    elif select == 'currency':
        currency_news = news.currencyNews()
        return jsonify(currency_news)
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)


@api.route('/api/news/')
@limiter.limit("3 per hour;72 per day")
def get_region_news():
    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    region = request.args.get('region')
    if region == 'asia':
        AsiaNews = news.Asia()
        return jsonify(AsiaNews)
    elif region == 'europe':
        EuropeNews = news.Europe()
        return jsonify(EuropeNews)
    elif region == 'middle-east':
        middleEast = news.middleEast()
        return jsonify(middleEast)
    elif region == 'africa':
        Africa = news.Africa()
        return jsonify(Africa)
    elif region == 'asia-pacific':
        asiaPacific = news.asiaPacific()
        return jsonify(asiaPacific)
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)


@api.route('/api/news/sports/')
@limiter.limit("3 per hour;72 per day")
def get_sports_news():

    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})
    select = request.args.get('sport')
    if select == 'all':
        sports_news = news.SportsNews()
        return jsonify(sports_news)
    elif select == 'cricket':
        cricket = news.cricket()
        return jsonify(cricket)
    elif select == 'football':
        football = news.football()
        return jsonify(football)
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)

@api.route('/api/news/entertainment/')
@limiter.limit("3 per hour;72 per day")
def get_entertainment_news():

    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})
    select = request.args.get('entertainment')
    if select == 'anime':
        anime = news.anime()
        return jsonify(anime)
    elif select == 'bollywood':
        bollywood = news.bollywood()
        return jsonify(bollywood)
    elif select == 'hollywood':
        hollywood = news.hollywood()
        return jsonify(hollywood)
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)


@api.route('/api/news/financial-assets/')
@limiter.limit("3 per hour;72 per day")
def financialAssets():
    select = request.args.get('asset')
    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    
    if select == 'stock':
        stock = news.stock()
        return jsonify(stock)
    elif select == 'ipo':
        ipo= news.ipo_News()
        return jsonify(ipo)
    elif select == 'commodities':
        commodities = news.commoditiesNews()
        return jsonify(commodities)
    elif select == 'personal-finance':
        personalFinance = news.personal_Finance_News()
        return jsonify(personalFinance)
    elif select == 'currency':
        currency = news.currencyNews()
        return jsonify(currency)
    elif select == 'cryptocurrency':
        cryptocurrency= news.cryptcurrency()
        return jsonify(cryptocurrency)   
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)


@api.route('/api/news/world/')
@limiter.limit("3 per hour;72 per day")
def world():

    api_key = request.args.get('api_key')
    user = db.get(Query().api_key == api_key)
    if user:
        rate_limit_hour = user.get('rate_limit_hour', 0)
        rate_limit_day = user.get('rate_limit_day', 0)
    else:
        return jsonify({'error': 'Invalid API key!'}), 401
    
    print("User API Key: ----------- ", api_key)
    
    # Decrement the values
    rate_limit_hour -= 1
    rate_limit_day -= 1

    # Update the values in the session
    session["rate_limit_hour"] = rate_limit_hour
    session["rate_limit_day"] = rate_limit_day



    # Update the values in the TinyDB
    db.update({'rate_limit_hour': rate_limit_hour, 'rate_limit_day': rate_limit_day})

    select = request.args.get('world')
    if select == 'world-economy':
        worldEconomy= news.world_Economy()
        return jsonify(worldEconomy)
    elif select == 'global-market':
        globalMarket= news.global_Market_News()
        return jsonify(globalMarket)
    elif select == 'geopolitics':
        geopolitics= news.GeopoliticsNews()
        return jsonify(geopolitics)
    elif select == 'terrorism':
        terrorism= news.Terrorism()
        return jsonify(terrorism)
    elif select == 'weird':
        weird= news.weirdNews()
        return jsonify(weird)
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)
