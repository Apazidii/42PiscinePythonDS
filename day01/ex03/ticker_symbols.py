import sys


def lower_dict(d):
   new_dict = dict((str(k).lower(), str(v)) for k, v in d.items())
   return new_dict

def get_stock_price(s):
    s = s.lower()
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

    COMPANIES = {v: k for k, v in COMPANIES.items()}
    COMPANIES = lower_dict(COMPANIES)
    STOCKS = lower_dict(STOCKS)

    name = COMPANIES.get(s)
    price = STOCKS.get(s)
    if (name is None):
        print("Unknown ticker")
    else:
        print(name, price)



if __name__ == "__main__":
    if (len(sys.argv) == 2):
        get_stock_price(sys.argv[1])
