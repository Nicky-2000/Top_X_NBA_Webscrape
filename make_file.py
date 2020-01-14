import bs4
import lxml
import requests
import csv


# def make_csv(year, season_type, entries):
def make_csv (year_value, season_type, entry, csv_writer):

    web_page = requests.get(f'https://www.espn.com/nba/stats/player/_/season/{year_value}/seasontype/{season_type}/table/offensive/sort/avgPoints/dir/desc')
    stat_soup = bs4.BeautifulSoup(web_page.text, 'lxml')
    seas = ''
    if season_type == 2:
        seas = 'Regular Season'
    elif season_type == 3:
        seas = 'Post Season'
    # Make sub headers in csv file
    csv_writer.writerow([f'{year_value} {seas} top {entry} players'])

    csv_writer.writerow(['#', 'Player Name', 'Points Per Game', 'Rebounds Per Game', ' Assists Per Game'])

    # PRINTS THE PLAYER COLUMN ON THE SCREEN
    player_col = stat_soup.find('tbody')
    # count = 0
    # print (player_col.prettify())

    # player_names is a list of all the <a> tags which store the players name. players_name[index].text gives name string
    player_names = player_col.find_all('a')

    PN = []
    for player in player_names:
        PN.append(player.text)

    # Data table is a closer tag to all the table elements (stat values and column headers)
    data_table = stat_soup.find('div', class_='Table__Scroller')

    row_data = data_table.find_all('tr', class_='Table__TR Table__TR--sm Table__even')

    num_of_entry = entry

    row_data = row_data[0:num_of_entry]

    num = 0

    for player_row in row_data:
        list_of_row = player_row.find_all('td')

        ppg = list_of_row[3].text
        rpg = list_of_row[13].text
        apg = list_of_row[14].text
        name = player_names[num].text
        num += 1

        csv_writer.writerow([num, name, ppg, rpg, apg])