import requests
from bs4 import BeautifulSoup
import datetime


def float_or_na(value):
    return float(value if value != 'N/A' else 'nan')


seasons = ['winter','spring','summer','fall']
year = datetime.datetime.today().year
for i in range(2017, (year+1)):
    for s in seasons:
        print('------' + s.upper() + '-' + str(i) + '------')
        html = requests.get('https://myanimelist.net/anime/season/'+ str(i) +'/' + s )
        soupMAL = BeautifulSoup(html.text, 'lxml')
        tipoAnimu = soupMAL.findAll('div',
                                    class_='seasonal-anime-list js-seasonal-anime-list js-seasonal-anime-list-key-1 clearfix')
        for t in tipoAnimu:
            divs = t.findAll('div', class_='seasonal-anime js-seasonal-anime')
            for d in divs:
                score = float_or_na(d.find('span', class_='score').text.strip())
                typeA = t.find('div', class_='anime-header').text
                title = d.find('p', class_='title-text').a.text
                if score >= 7.5:
                    print( 
                        typeA +
                        ': ' +
                        title +
                        ' | Score: ' +
                        str(score)
                    )
