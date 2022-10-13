import os, sys
import pytest
import re
from financial import run


def test_total_revenue():
    assert run('MSFT', 'Total Revenue')[0].lower() == 'Total Revenue'.lower()


def test_is_tuple():
    assert isinstance(run('MSFT', "Total Revenue"), tuple)


def test_invalid_ticker_error():
    # connection error check failed; url comparison ok
    with pytest.raises(Exception, match='Invalid ticker', ):
        run('MMMMMM', "Total Revenue")
