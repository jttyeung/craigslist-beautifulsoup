import urllib
from bs4 import BeautifulSoup

url = 'https://sfbay.craigslist.org/search/sfc/apa'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
rentals = soup.select('li.result-row')


def get_price_and_link():
    """Gets price and link of rentals"""
    num_links = 0

    for rental in rentals:
        rental_link = rental.find('a').get('href')
        price = rental.find('span', class_='result-price').getText()
        # .find() gets the first instance, .select() finds multiple instances and returns a list
        num_links += 1

        print price, 'https://sfbay.craigslist.org' + rental_link

    return num_links

print get_price_and_link()
