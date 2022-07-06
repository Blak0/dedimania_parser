from datetime import datetime
from typing import List
from extract import Row


def rows_this_month(rows: List[Row]):
    current_year = datetime.now().year
    current_month = datetime.now().month
    return [row for row in rows if row.record_date.month == current_month and row.record_date.year == current_year]


def rows_until_date(rows: List[Row], until: datetime):
    return [row for row in rows if row.record_date > until]
