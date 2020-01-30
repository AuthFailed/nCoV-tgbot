import requests
from bs4 import BeautifulSoup as Soup

def get_main_info():
    page = requests.get("https://wuhanpneumonia.ru/")
    if page.status_code == 200:
        soup = Soup(page.text, "html.parser")
        infected = soup.find("h3", attrs={"class": "text-warning"}).contents[0]
        possible = soup.find("h3", attrs={"class": "text-primary"}).contents[0]
        deaths = soup.find("h3", attrs={"class": "text-danger"}).contents[0]
        recovered = soup.find("h3", attrs={"class": "text-success"}).contents[0]
        table = get_table_cities()
        quarantine = table[len(table)-1][1]
        death_rate = round(float(int(deaths)/int(infected)*100), 2)
        date = soup.find('b').contents[0]
        info_array = {
            'Infected' : infected,
            'Possible' : possible,
            'Deaths' : deaths,
            'Death_Rate' : death_rate,
            'Recovered' : recovered,
            'Quarantine' : quarantine,
            'Quarantined_Cities' : len(table),
            'Date' : date
        }
        return info_array
    else:
        raise Exception("Нет соединения!")


def get_table_cities():
    page = requests.get("https://wuhanpneumonia.ru/")
    if page.status_code == 200:
        soup = Soup(page.text, "html.parser")
        data = []
        table = soup.find('table', attrs={'id': 'sortable-table-1',
                                          'class': 'table table-hover'})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]) # Get rid of empty values
        return data
    else:
        raise Exception("Нет соединения!")

def disease_forecast():
    page = requests.get("https://wuhanpneumonia.ru/2019-ncov-prognoz/")
    if page.status_code == 200:
        soup = Soup(page.text, "html.parser")
        data = []
        table = soup.find('table', attrs={'id': 'sortable-table-1',
                                          'class': 'table table-hover'})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]) # Get rid of empty values
        data.reverse()
        return data
    else:
        raise Exception("Нет соединения!")
