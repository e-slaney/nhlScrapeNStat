import pandas as pd
import requests
import json

#Make a GET request to the undocumented NHL API's Team's webpage
nhl_teams_url = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

#Place the NHL teams content into a dictionary
nhl_team_dict = json.loads(nhl_teams_url.content)

#Using the teams dictionary, create a Pandas DataFrame
df_teams = pd.DataFrame(nhl_team_dict['teams'])
#Aggregate names and ids so user knows which ID to select when choosing a team to learn about.
names_ids = df_teams.groupby('id')['name'].head()

while(True):
    print(names_ids.to_string())
    
    team_request = input("Enter the id of a team you would like to know more about or type \'quit\' to exit the program: ")
    if(team_request == 'quit'):
        exit()
    
    try:
        selected_row = df_teams.loc[[int(team_request)]]

        print('\n')
        print('Team Name: ' + str(selected_row.iloc[0]['name']))
        print('Abbreviation: ' + str(selected_row.iloc[0]['abbreviation']))
        print('Arena: ' + selected_row['venue'].iloc[0]['name'])
        print('First Year of Play: ' + str(selected_row.iloc[0]['firstYearOfPlay']))
        print('Division: ' + str(selected_row['division'].iloc[0]['name']))
        print('Conference: '  + str(selected_row['conference'].iloc[0]['name']))
        print('Active? '  + str(selected_row.iloc[0]['active']))
        print('\n')

    except:
        print("You selected an invalid team id. Try again.")

    print('Type \'y\' if you would like to learn about another team.')
    another_request = input('Type \'n\' if you would like to stop.')
    if another_request == 'n':
        exit()
