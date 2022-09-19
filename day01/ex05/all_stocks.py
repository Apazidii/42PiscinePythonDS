import sys

def lower_dict(d):
   new_dict = dict((str(k).lower(), str(v).lower()) for k, v in d.items())
   return new_dict

def run(ss):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    COMPANIES = lower_dict(COMPANIES)
    STOCKS = lower_dict(STOCKS)
    s = ss.lower()

    res = COMPANIES.get(s)
    if (res is not None):
        print(f"{s.title()} stock price is {STOCKS.get(res)}")
        return
    res = STOCKS.get(s)
    if (res is not None):
        print(f"{s.upper()} is a ticker symbol for {s.title()}")
        return
    print(f"{ss} is an unknown company or an unknown ticker symbol")

def all_stocks(line):
    while ' ' in line:
        line = line.replace(' ', '')
    words = line.split(',')
    if '' in words:
        return
    for word in words:
        run(word)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_stocks(sys.argv[1])
