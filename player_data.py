import requests
import json
import pandas as pd

#Make a GET request to the undocumented NHL API's Teams webpage
#A GET request to the team's page is made so user's can identify the id
#of the team and player they wish to explore.
try:
    nhl_teams_url = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
except:
    print("The NHL Team Stats API is unavailable at the moment. Try again later.")
    exit()

#Place the NHL teams content into a dictionary
nhl_team_dict = json.loads(nhl_teams_url.content)

#Using the teams dictionary, create a Pandas DataFrame
df_teams = pd.DataFrame(nhl_team_dict['teams'])
#Aggregate names and ids so user knows which ID to select when choosing a team to learn about.
names_ids = pd.DataFrame()
names_ids['id'] = df_teams['id']
names_ids['name'] = df_teams['name']
print(names_ids.to_string(index=False))


user_id = input("Enter the id of a team who has a player you would like to know more about: ")

#Make a GET request to the undocumented selected team webpage
try:
    team_selection_url = requests.get('https://statsapi.web.nhl.com/api/v1/teams/' + str(user_id) + '/roster')
except:
    print("The roster page for the team you selected is unavailable. Try again later.")
    exit()

#Store the nhl players content in a dictionary
nhl_players_dict = json.loads(team_selection_url.content)

#Using the players dictionary, create a Pandas DataFrame
df_players = pd.DataFrame(nhl_players_dict['roster'])

players_ids = pd.DataFrame()
print(df_players['person'].iloc[0]['id'])
'''
players_ids['id'] = df_players['person']
players_ids['name'] = df_players['person']
players_ids['jerseyNumber'] = df_players['jerseyNumber']
players_ids['position'] = df_players['position']
'''
# print(players_ids.to_string(index=False))
