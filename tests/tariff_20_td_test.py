import unittest

from tariff_td import Tariff20TD, HOLY_FRIDAYS, P1, P2, P3
from tests import get_date

PRICE1 = 1
PRICE2 = 2
PRICE3 = 3

tariff = Tariff20TD(PRICE1, PRICE2, PRICE3)


def test_p1_period():
    dates = [
        "2024-01-08 10:00:00",
        "2024-01-08 13:50:00",
        "2024-01-08 18:00:00",
        "2024-01-08 21:50:00",
    ]
    for date in dates:
        assert tariff.get_period(get_date(date)) == P1


def test_p2period():
    dates = [
        "2024-01-08 08:00:00",
        "2024-01-08 09:50:00",
        "2024-01-08 14:00:00",
        "2024-01-08 17:50:00",
        "2024-01-08 22:00:00",
        "2024-01-08 23:50:00",
    ]
    for date in dates:
        assert tariff.get_period(get_date(date)) == P2


def test_p3_period():
    dates = [
        "2024-01-08 00:00:00",
        "2024-01-08 07:50:00",
    ]
    for date in dates:
        assert tariff.get_period(get_date(date)) == P3


def test_p3_period_weekend():
    date = get_date("2024-01-07 15:00:00")
    assert tariff.get_period(date) == P3


def test_p3_period_holiday():
    date = get_date("2024-01-01 15:00:00")
    assert tariff.get_period(date) == P3


def test_p1_price():
    date = get_date("2024-01-08 12:00:00")
    assert tariff.get_price(date) == PRICE1


def test_p2_price():
    date = get_date("2024-01-08 15:00:00")
    assert tariff.get_price(date) == PRICE2


def test_p3_price():
    date = get_date("2024-01-08 6:00:00")
    assert tariff.get_price(date) == PRICE3


def test_all_holy_fridays_are_not_holidays():
    for f in HOLY_FRIDAYS:
        date = get_date(f"{f} 12:00:00")
        assert tariff.get_period(date) == P1

def test_get_holiday_day_prices():
    date = get_date("2024-01-06 12:00:00")
    prices = tariff.get_day_prices(date)
    assert all(p == PRICE3 for p in prices)

def test_get_weekend_day_prices():
    date = get_date("2024-01-04 12:00:00")
    prices = tariff.get_day_prices(date)
    for i, p in enumerate(prices):
        if i < 8:
            assert p == PRICE3
        elif i < 10 or 14 <= i < 18 or i >= 22:
            assert p == PRICE2
        else:
            assert p == PRICE1
