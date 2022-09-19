import sys
from analytics import *
from config import *
import logging
import json

import requests

def make_report(file):
    logging.basicConfig(filename="analytics.log", format='%(asctime)s %(message)s', encoding='utf-8', level=logging.DEBUG)
    data = Research(file).file_reader()
    analytics = Analytics(data)
    tails, heads = analytics.counts()
    p_tails, p_heads = analytics.fractions()
    analytics = Analytics(analytics.predict_random(num_of_steps))
    sum_tails, sum_heads = analytics.counts()
    report = eval(pattern_str)
    analytics.save_file(report, "report", "txt")


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            make_report(sys.argv[1])
        requests.post(webhook, json.dumps({"text": "The report has been successfully create"}))
    except Exception as e:
        requests.post(webhook, json.dumps({"text": "The report hasn’t been created due to an error"}))
        raise e