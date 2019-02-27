import requests
from bs4 import BeautifulSoup
print('Input your username:')
profile = input("Username: ")
profile.strip() 
# Main profile
html = requests.get('https://myanimelist.net/profile/' + profile)
MAL2Soup = BeautifulSoup(html.text, 'lxml')
UserFound = MAL2Soup.find('body', class_='page-common profile')

if UserFound != None:
    divAnime = MAL2Soup.find('div', class_='stats anime')
    daysSpent = divAnime.find('div', class_='di-tc al pl8 fs12 fw-b').text
    meanScore = divAnime.find('div', class_='di-tc ar pr8 fs12 fw-b').text
    joinDate = MAL2Soup.find('ul', class_='user-status border-top pb8 mb4').find('span', class_='user-status-data di-ib fl-r').text
    profileAnimeStats = divAnime.find('ul', class_='stats-status fl-l').findAll('span', class_='di-ib fl-r lh10')
    profileAnimeEpStats = divAnime.find('ul', class_='stats-data fl-r').findAll('span', class_='di-ib fl-r')
    #Stats
    print('Profile Stats:')
    print('Spent ' + daysSpent + ' | ' + meanScore + ' | ' + 'Joined on: ' + joinDate)
    print('Anime Stats:')
    print('[Watching] ' + profileAnimeStats[0].text + ' [Completed] ' + profileAnimeStats[1].text + ' [On hold] ' + profileAnimeStats[2].text + ' [Dropped] ' + profileAnimeStats[3].text + ' [Plan To Watch] ' + profileAnimeStats[4].text)
    print('[Total Entries] ' + profileAnimeEpStats[0].text + ' [Rewatched] ' + profileAnimeEpStats[1].text + ' [Total Episodes] ' + profileAnimeEpStats[2].text)
    # All anime
    html = requests.get('https://myanimelist.net/profile/'+profile+'?status=7')
    MAL2Soup = BeautifulSoup(html.text, 'lxml')
    animes = MAL2Soup.findAll('tbody', class_='list-item')
else: print('User not found')
