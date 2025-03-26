import datetime

from tariff_td.const import HOLY_FRIDAYS

FRIDAY = 4
FORMAT = "%Y-%m-%d"


def test_all_holy_fridays_are_friday():
    for f in HOLY_FRIDAYS:
        date = datetime.datetime.strptime(f, FORMAT)
        assert date.weekday() == FRIDAY
