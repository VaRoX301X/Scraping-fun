import requests
import csv
from bs4 import BeautifulSoup

def float_or_na(value):
    return float(value if value != 'N/A' else 'nan')


csv_file = open('mal_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['YEAR','SEASON','TYPE','TITLE','SCORE'])

seasons = ['winter','spring','summer','fall']
for i in range(2017, 2019):
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
                csv_writer.writerow(str(i)+","+s+","+typeA+","+title+","+str(score))


csv_file.close()
