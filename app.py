from config import *


'''
    UPDATE PLAYLISTS
    ~~~~~~~~~~~~~~~~

    Assumes playlists are all the same name
'''

playlist_name = 'Hitmaker'


# for each account -> pull playlists -> if name found get URL -> Update
for account, track in zip(accounts, tracklist):
    # authenticate
    headers = authenticate(account)
    if headers is False:
        skipped_accounts.append(account)
        continue

    # get playlists
    playlists = get_playlists(headers)

    # find playlist URL
    for playlist in playlists:
        p = playlist.get('name')
        if p.get('name') == playlist_name:
            playlist_url = playlist.get('href')
            playlist_url = playlist_url.split('/')[-1]
            break
        else:
            skipped_accounts.append(account)
            continue


    # update playlist
    try:
        r = requests.put(api_url + '/' + api_version + '/me/library/playlists/' + playlist_url + '/tracks', headers=headers, data=tracklist_data)
    except:
        pass

    if r.status_code != 204 or 302:
        print('Error: [' + str(r.status_code) + ']' + str(r.text))

    # if r.status_code == 204:
    #     pass
    # elif r.status_code == 302:
    #     pass
    # else:
    #     print('Error: [' + str(r.status_code) + ']' + str(r.text))



'''
    COMPLETE
'''

print('COMPLETE')
print('\n\n')

if skipped_accounts:
    print('Accounts skipped: ')
    for i in skipped_accounts:
        print(i)

if skipped_tracks:
    print('Tracks skipped: ')
    for i in skipped_tracks:
        print(i)
