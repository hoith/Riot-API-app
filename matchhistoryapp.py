from riotwatcher import LolWatcher, ApiError
import pandas as pd

# golbal variables
val = input("Enter player name: ") 
api_key = 'RGAPI-8c1b98e6-6f83-4f36-8b7e-57ff075ba5b7'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, val)
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])

last_match = my_matches['matches'][0]
match_detail = watcher.match.by_id(my_region, last_match['gameId'])
#match_type = 
i =0
participants = []
participantIdentities=[]
df = pd.DataFrame(participants)
latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')
champ_dict = {}
#for row in par:
 #   print(match_detail['participantIdentities'][i]['player']['summonerName'])
 # participants.append(participants_row)

   # i= i +1

for row in match_detail['participants']:
    participants_row = {}
    match_detail['participantIdentities'][i]['player']['summonerName']
    participants_row['champion'] = row['championId']
    participants_row['spell1'] = row['spell1Id']
    participants_row['spell2'] = row['spell2Id']
    participants_row['win'] = row['stats']['win']
    participants_row['kills'] = row['stats']['kills']
    participants_row['deaths'] = row['stats']['deaths']
    participants_row['assists'] = row['stats']['assists']
    participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
    participants_row['goldEarned'] = row['stats']['goldEarned']
    participants_row['champLevel'] = row['stats']['champLevel']
    participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
    participants_row['item0'] = row['stats']['item0']
    participants_row['item1'] = row['stats']['item1']
    participants.append(participants_row)


usernames=[]
champnames=[]
#print(participantIdentities)
df = pd.DataFrame(participants)
latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')
champ_dict = {}
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_dict[row['key']] = row['id']
for row in participants:
    test = champ_dict[str(row['champion'])]
    champnames.append(test)

for i in range(10):
    dogs = match_detail['participantIdentities'][i]['player']['summonerName']
    usernames.append(dogs)

df = pd.DataFrame(participants)
#print(usernames)
df.insert(loc=0, column='UserName', value=usernames)
#df.insert(loc=1, column='Champion', value=champnames)

#df['username'] = usernames
print(df)
#print(participants)
#print(match_detail['participantIdentities'][0]['player']['summonerName'])