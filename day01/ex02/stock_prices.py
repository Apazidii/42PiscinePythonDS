import sys

def lower_dict(d):
   new_dict = dict((str(k).lower(), str(v).lower()) for k, v in d.items())
   return new_dict

def get_stock_price(s):
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
    s = s.lower()

    res = STOCKS.get(COMPANIES.get(s))
    if (res is None):
        print("Unknown company")
    else:
        print(res)



if __name__ == "__main__":
    if (len(sys.argv) == 2):
        get_stock_price(sys.argv[1])
