from datetime import datetime
from typing import List
from extract import Row


def rows_of_month(rows: List[Row], month: int, year: int) -> List[Row]:
    """
    Filters list of rows, leaving rows with specified month (1-12) and year (ex. 2022)
    """
    return [row for row in rows if row.record_date.month == int(month) and row.record_date.year == int(year)]


def rows_until_date(rows: List[Row], until: datetime) -> List[Row]:
    """
    Filters list of rows, leaving rows with record date before or equal to specified date
    """
    return [row for row in rows if row.record_date > until]


def from_to(rows: List[Row], down: datetime, up: datetime):
    """
    Filters list of rows, leaving rows which have record dates between two dates.
    """
    assert down < up, f'Down date is somehow bigger than up: {down} should be lower than {up}'
    return [row for row in rows if down < row.record_date < up]
