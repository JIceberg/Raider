import requests
from bs4 import BeautifulSoup

def lookup_team(team):
    values = {}

    url = "http://www.ftcstats.org/2021/index.html"
    with requests.Session() as s:
        with s.get(url) as page:
            soup = BeautifulSoup(page.content, 'html.parser')
            rows = soup.findAll('tr', class_="trow")
            found = False

            for row in rows:
                data = row.findAll('td')
                team_number = data[1].find('a')
                if not team_number:
                    continue
                else:
                    num = int(team_number.getText())
                    if team == num and not found:
                        found = True
                        values['team_name'] = data[2].find('abbr').getText()
                        values['opr'] = data[3].getText()
                        values['rank'] = data[0].getText()

    url = "http://www.ftcstats.org/2021/georgia.html"
    with requests.Session() as s:
        with s.get(url) as page:
            soup = BeautifulSoup(page.content, 'html.parser')
            rows = soup.findAll('tr', class_="trow")
            found = False

            for row in rows:
                data = row.findAll('td')
                team_number = data[1].find('a')
                if not team_number:
                    continue
                else:
                    num = int(team_number.getText())
                    if team == num and not found:
                        found = True
                        values['state_rank'] = data[0].getText()

    return values

def get_rank(team) -> str:
    data = lookup_team(team)
    if 'rank' not in data:
        return "Could not find team!"
    res = data["team_name"] + " is rank " + data["rank"]
    res += " globally with an OPR of " + data["opr"] + "."
    if 'state_rank' not in data:
        return res
    else:
        return res + " In Georgia, the team is rank " + data['state_rank'] + "."


    
