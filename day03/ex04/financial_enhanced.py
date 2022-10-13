#!/dgalactu/bin/python3
import bs4
import sys
import os
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time


def run(ticket, field):
    url = f"https://finance.yahoo.com/quote/{ticket}/financials?p={ticket}"

    html = urlopen(Request(url=url, headers={'User-Agent': 'Student42'})).read()
    soup = BeautifulSoup(html, 'html.parser')

    if soup.title.string == 'Symbol Lookup from Yahoo Finance':
        raise Exception('Invalid ticker')

    r = soup.find_all(attrs={'data-test': 'fin-row'})
    rows = list(map(lambda x: x.find(class_='Va(m)').get_text(), r))

    if field not in rows:
        raise Exception('Invalid field')
    res = r[rows.index(field)].find_all('span')

    return tuple(map(lambda x: x.get_text(), res))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(run(sys.argv[1], sys.argv[2]))
    else:
        print("invalid number of arg")

