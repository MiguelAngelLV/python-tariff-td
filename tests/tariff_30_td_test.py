from tariff_td import HOLY_FRIDAYS, P1, P2, P3, P4, P5, P6, Tariff30TD
from tests import get_date

PRICE1 = 1
PRICE2 = 2
PRICE3 = 3
PRICE4 = 4
PRICE5 = 5
PRICE6 = 6

tariff = Tariff30TD(PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, PRICE6)


def test_p6_hour_period():
    date = get_date("2024-01-02 06:00:00")
    assert tariff.get_period(date) == P6


def test_p6_hour_price():
    date = get_date("2024-01-02 06:00:00")
    assert tariff.get_price(date) == PRICE6


def test_p6_weekend_period():
    date = get_date("2024-01-07 15:00:00")
    assert tariff.get_period(date) == P6


def test_p6_weekend_price():
    date = get_date("2024-01-07 15:00:00")
    assert tariff.get_price(date) == PRICE6


def test_p6_holiday_period():
    date = get_date("2024-01-01 12:00:00")
    assert tariff.get_period(date) == P6


def test_p6_holiday_price():
    date = get_date("2024-01-01 12:00:00")
    assert tariff.get_price(date) == PRICE6


def test_p1_period():
    dates = [
        "2024-01-08 10:00:00",
        "2024-01-08 13:50:00",
        "2024-01-08 18:00:00",
        "2024-01-08 21:50:00",
    ]
    for date in dates:
        assert tariff.get_period(get_date(date))


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
        assert tariff.get_period(get_date(date))


def test_p6_period():
    dates = [
        "2024-01-08 00:00:00",
        "2024-01-08 07:50:00",
    ]
    for date in dates:
        assert tariff.get_period(get_date(date))


def test_january_p1_period():
    date = get_date("2024-01-08 12:00:00")
    assert tariff.get_period(date) == P1


def test_january_p2_period():
    date = get_date("2024-01-08 8:00:00")
    assert tariff.get_period(date) == P2


def test_january_p1_price():
    date = get_date("2024-01-08 12:00:00")
    assert tariff.get_price(date) == PRICE1


def test_january_p2_price():
    date = get_date("2024-01-08 8:00:00")
    assert tariff.get_price(date) == PRICE2


def test_february_p1_period():
    date = get_date("2024-02-01 12:00:00")
    assert tariff.get_period(date) == P1


def test_february_p2_period():
    date = get_date("2024-02-01 8:00:00")
    assert tariff.get_period(date) == P2


def test_february_p1_price():
    date = get_date("2024-02-01 12:00:00")
    assert tariff.get_price(date) == PRICE1


def test_february_p2_price():
    date = get_date("2024-02-01 8:00:00")
    assert tariff.get_price(date) == PRICE2


def test_march_p2_period():
    date = get_date("2024-03-01 12:00:00")
    assert tariff.get_period(date) == P2


def test_march_p3_period():
    date = get_date("2024-03-01 8:00:00")
    assert tariff.get_period(date) == P3


def test_march_p2_price():
    date = get_date("2024-03-01 12:00:00")
    assert tariff.get_price(date) == PRICE2


def test_march_p3_price():
    date = get_date("2024-03-01 8:00:00")
    assert tariff.get_price(date) == PRICE3


def test_april_p4_period():
    date = get_date("2024-04-01 12:00:00")
    assert tariff.get_period(date) == P4


def test_april_p25period():
    date = get_date("2024-04-01 8:00:00")
    assert tariff.get_period(date) == P5


def test_april_p4_price():
    date = get_date("2024-04-01 12:00:00")
    assert tariff.get_price(date) == PRICE4


def test_april_p5_price():
    date = get_date("2024-04-01 8:00:00")
    assert tariff.get_price(date) == PRICE5


def test_may_p4_period():
    date = get_date("2024-05-02 12:00:00")
    assert tariff.get_period(date) == P4


def test_may_p5_period():
    date = get_date("2024-05-02 8:00:00")
    assert tariff.get_period(date) == P5


def test_may_p4_price():
    date = get_date("2024-05-02 12:00:00")
    assert tariff.get_price(date) == PRICE4


def test_may_p5_price():
    date = get_date("2024-05-02 8:00:00")
    assert tariff.get_price(date) == PRICE5


def test_june_p3_period():
    date = get_date("2024-06-03 12:00:00")
    assert tariff.get_period(date) == P3


def test_june_p4_period():
    date = get_date("2024-06-03 8:00:00")
    assert tariff.get_period(date) == P4


def test_june_p3_price():
    date = get_date("2024-06-03 12:00:00")
    assert tariff.get_price(date) == PRICE3


def test_june_p4_price():
    date = get_date("2024-06-03 8:00:00")
    assert tariff.get_price(date) == PRICE4


def test_july_p1_period():
    date = get_date("2024-07-01 12:00:00")
    assert tariff.get_period(date) == P1


def test_july_p2_period():
    date = get_date("2024-07-01 8:00:00")
    assert tariff.get_period(date) == P2


def test_july_p1_price():
    date = get_date("2024-07-01 12:00:00")
    assert tariff.get_price(date) == PRICE1


def test_july_p2_price():
    date = get_date("2024-07-01 8:00:00")
    assert tariff.get_price(date) == PRICE2


def test_august_p3_period():
    date = get_date("2024-08-01 12:00:00")
    assert tariff.get_period(date) == P3


def test_august_p4_period():
    date = get_date("2024-08-01 8:00:00")
    assert tariff.get_period(date) == P4


def test_august_p3_price():
    date = get_date("2024-08-01 12:00:00")
    assert tariff.get_price(date) == PRICE3


def test_august_p4_price():
    date = get_date("2024-08-01 8:00:00")
    assert tariff.get_price(date) == PRICE4


def test_september_p3_period():
    date = get_date("2024-09-03 12:00:00")
    assert tariff.get_period(date) == P3


def test_september_p4_period():
    date = get_date("2024-09-03 8:00:00")
    assert tariff.get_period(date) == P4


def test_september_p3_price():
    date = get_date("2024-09-03 12:00:00")
    assert tariff.get_price(date) == PRICE3


def test_september_p4_price():
    date = get_date("2024-09-03 8:00:00")
    assert tariff.get_price(date) == PRICE4


def test_october_p4_period():
    date = get_date("2024-10-02 12:00:00")
    assert tariff.get_period(date) == P4


def test_october_p5_period():
    date = get_date("2024-10-02 8:00:00")
    assert tariff.get_period(date) == P5


def test_october_p4_price():
    date = get_date("2024-10-02 12:00:00")
    assert tariff.get_price(date) == PRICE4


def test_october_p5_price():
    date = get_date("2024-10-02 8:00:00")
    assert tariff.get_price(date) == PRICE5


def test_november_p2_period():
    date = get_date("2024-11-04 12:00:00")
    assert tariff.get_period(date) == P2


def test_november_p3_period():
    date = get_date("2024-11-04 8:00:00")
    assert tariff.get_period(date) == P3


def test_november_p2_price():
    date = get_date("2024-11-04 12:00:00")
    assert tariff.get_price(date) == PRICE2


def test_november_p3_price():
    date = get_date("2024-11-04 8:00:00")
    assert tariff.get_price(date) == PRICE3


def test_december_p1_period():
    date = get_date("2024-12-05 12:00:00")
    assert tariff.get_period(date) == P1


def test_december_p2_period():
    date = get_date("2024-12-05 8:00:00")
    assert tariff.get_period(date) == P2


def test_december_p1_price():
    date = get_date("2024-12-05 12:00:00")
    assert tariff.get_price(date) == PRICE1


def test_december_p2_price():
    date = get_date("2024-12-05 8:00:00")
    assert tariff.get_price(date) == PRICE2


def test_all_holy_fridays_are_not_holidays():
    for f in HOLY_FRIDAYS:
        date = get_date(f"{f} 12:00:00")
        assert tariff.get_period(date) != P6
