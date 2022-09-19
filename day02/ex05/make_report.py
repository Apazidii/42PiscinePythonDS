import sys
from analytics import *
from config import *


def make_report(file):
    data = Research(file).file_reader()
    analytics = Analytics(data)
    tails, heads = analytics.counts()
    p_tails, p_heads = analytics.fractions()
    analytics = Analytics(analytics.predict_random(num_of_steps))
    sum_tails, sum_heads = analytics.counts()
    report = eval(pattern_str)
    analytics.save_file(report, "report", "txt")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        make_report(sys.argv[1])
