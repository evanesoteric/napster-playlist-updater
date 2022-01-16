import requests
import json
import string
import re


'''
    Napster API
'''
api_rate_limit = 5
api_url = 'https://api.napster.com'
api_version = 'v2.2'
oauth_url = api_url + '/oauth/token'

app_id = ''
api_key = ''
api_secret = ''


# pseudo
skipped_accounts = []
skipped_tracks = []
json_tracklist = []


'''
    ACCOUNTS
    ~~~~~~~~

    import and setup accounts
'''
with open('accounts.txt', 'r') as f:
    accounts = f.read().splitlines()

accounts = [i.strip() for i in accounts]
accounts = [i.replace(' ', ':', 1) for i in accounts]
accounts = list(filter(None, accounts))
accounts = [i.translate({ord(c): None for c in string.whitespace}) for i in accounts]



'''
    TRACKLIST
    ~~~~~~~~~

    import and setup tracklist
'''
with open('tracklist.txt', 'r') as f:
    tracklist = f.read().splitlines()

tracklist = [i.strip() for i in tracklist]
tracklist = list(filter(None, tracklist))
tracklist = [i.translate({ord(c): None for c in string.whitespace}) for i in tracklist]


# setup and convert tracklist to json
for i in tracklist:
    if not re.search(r'^tra\.\d+', i)
    skipped_tracks.append(i)
    tracklist.remove(i)
    i = {'id': i}
    json_tracklist.append(i)

json_tracklist = json.dumps(json_tracklist)
tracklist_data = '{"tracks": '+ json_tracklist +'}'


'''
    Authentication
'''
def authenticate(account):
    username, password = account.split(':')
    try:
        params = (api_key, api_secret)
        data = {
            'username': username,
            'password': password,
            'grant_type': 'password'
            }
        r_login = requests.post(url=oauth_url, auth=params, data=data)
        if r_login.status_code == 200:
            tokens = json.loads(r_login.text)
            headers = {
            'Authorization': f"Bearer {tokens['access_token']}",
            'Content-Type': 'application/json',
            }
            status = True  # 'Authenticated'
        else:
            # status = False  # 'Could not be authenticated'
            headers = False
    except:
        # status = False  # 'Could not be authenticated'
        headers = False
    return headers


'''
    Playlists
'''
def get_playlists(headers):
    r = requests.get(url=api_url + '/' + api_version + '/me/library/playlists', headers=headers)
    p = json.loads(r.text)
    playlists = p.get('playlists')
    return playlists
