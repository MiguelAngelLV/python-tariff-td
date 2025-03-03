from tariff_td import HOLY_FRIDAYS, P1, P2, P3, Tariff20TD
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
