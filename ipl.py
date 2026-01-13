# ipl.py
# EDA, Data analysis logic lives here (PRODUCTION SAFE)

import pandas as pd
import numpy as np
from functools import lru_cache

# =========================
# DATA SOURCES
# =========================

IPL_MATCHES_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQG9rp1Zzv4WcMBI1M9tAE_qJWKz2MCfH8UPTni2WMTjJqC7ew1gHnDjoBPHsuV9eF-9ECOZRR3lPFA/pub?gid=1361615103&single=true&output=csv"

BATSMAN_RUN_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRwgITbG6BjnxnNvxkj8YKJem6EIJjaejYK4KHMRbI5eHaYDVDP5RSv5OLd0rN1wWRrTE4EqYuUqb3a/pub?gid=655438454&single=true&output=csv"

DELIVERIES_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEJnmI-E6FluLo5khJ8JNuO9gYS0d3gZ0F1mY7zNca3ozajy26OTKAsoHjvyVdyI1CJHKGdrVidtrI/pub?gid=586204712&single=true&output=csv"


# =========================
# LAZY LOADERS (CACHED)
# =========================

@lru_cache(maxsize=1)
def get_matches():
    return pd.read_csv(IPL_MATCHES_URL)

@lru_cache(maxsize=1)
def get_batsman_run():
    return pd.read_csv(BATSMAN_RUN_URL)

@lru_cache(maxsize=1)
def get_deliveries():
    return pd.read_csv(DELIVERIES_URL)


# =========================
# APIs
# =========================

def teamsAPI():
    matches = get_matches()
    teams = list(set(matches['Team1']) | set(matches['Team2']))
    return {"teams": teams}


def teamVteamAPI(team1, team2):
    matches = get_matches()
    valid_teams = set(matches['Team1']) | set(matches['Team2'])

    if team1 not in valid_teams or team2 not in valid_teams:
        return {"Message": "Invalid Team Name..."}

    tempdf = matches[
        ((matches['Team1'] == team1) & (matches['Team2'] == team2)) |
        ((matches['Team1'] == team2) & (matches['Team2'] == team1))
    ]

    total_matches = tempdf.shape[0]
    wins = tempdf['WinningTeam'].value_counts()

    response = {
        "total_matches": str(total_matches),
        team1: str(wins.get(team1, 0)),
        team2: str(wins.get(team2, 0)),
        "draw": str(total_matches - (wins.get(team1, 0) + wins.get(team2, 0)))
    }

    return response


def teamRecord(team):
    matches = get_matches()
    valid_teams = set(matches['Team1']) | set(matches['Team2'])

    if team not in valid_teams:
        return {"Message": "Invalid Team Name..."}

    df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)]

    matches_played = df.shape[0]
    matches_won = (df['WinningTeam'] == team).sum()
    nr = df['WinningTeam'].isnull().sum()
    loss = matches_played - (matches_won + nr)
    titles = df[(df.MatchNumber == 'Final') & (df.WinningTeam == team)].shape[0]

    return {
        "total matches played": str(matches_played),
        "total matches won": str(matches_won),
        "No result": str(nr),
        "Total matches Lost": str(loss),
        "Title Won": str(titles)
    }


def seasonwinner():
    matches = get_matches()
    winners = matches[matches["MatchNumber"] == "Final"][["Season", "WinningTeam"]]
    return winners.set_index("Season").to_dict()


def venues():
    matches = get_matches()
    venues = matches[['City', 'Venue']].drop_duplicates().set_index('City')
    return venues.to_dict()


def teamatvenue(team, venue):
    matches = get_matches()

    played = matches[
        (matches['City'] == venue) &
        ((matches['Team1'] == team) | (matches['Team2'] == team))
    ]

    if played.empty:
        return {"Message": "Invalid team or venue"}

    won = played[played['WinningTeam'] == team].shape[0]
    total = played.shape[0]

    return {
        "Match Played At this Venue": total,
        "Match Won": won,
        "Loss": total - won,
        "Win Percentage": round((won / total) * 100, 2)
    }


def allbatsmanstats():
    batsman_run = get_batsman_run()
    batsman_run['batting_rank'] = batsman_run['batsman_run'].rank(ascending=False)

    return (
        batsman_run
        .sort_values('batting_rank')
        [['batter', 'batsman_run']]
        .set_index('batter')
        .to_dict()
    )


def batsmanvsall(batsman):
    deliveries = get_deliveries()
    filtered = deliveries[deliveries['batsman'] == batsman]

    if filtered.empty:
        return {"Message": "Invalid Batsman Name"}

    return filtered.groupby('bowling_team')['batsman_runs'].sum().to_dict()
