import pandas as pd
import requests
import json

#Make a GET request to the undocumented NHL API's Team's webpage
nhl_teams_url = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

#Place the NHL teams content into a dictionary
nhl_team_dict = json.loads(nhl_teams_url.content)

#Using the teams dictionary, create a Pandas DataFrame
df_teams = pd.DataFrame(nhl_team_dict['teams'])
print(df_teams.head())