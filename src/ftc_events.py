import requests
from bs4 import BeautifulSoup

def get_event_info(event: str, team_number: str):
    info = {}
    url = "https://ftc-events.firstinspires.org/" + event + "/rankings"

    with requests.Session() as s:
        with s.get(url) as page:
            soup = BeautifulSoup(page.content, 'html.parser')
            team_row = soup.find('a', string=team_number).find_parent('tr')

            info['rank'] = team_row.findAll('td')[0].getText()
            info['rp'] = team_row.findAll('td')[2].getText()
    
    return info

def get_rank(event: str, team_number: str):
    return get_event_info(event, team_number)['rank']

def get_ranking_points(event: str, team_number: str):
    return get_event_info(event, team_number)['rp']
