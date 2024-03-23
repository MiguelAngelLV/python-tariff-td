from datetime import datetime

FORMAT = "%Y-%m-%d %H:%M:%S"


def get_date(date: str):
    """
    Parse a string date to timezone.

    @param date
    @return: timezone.
    """
    return datetime.strptime(date, FORMAT).astimezone()
