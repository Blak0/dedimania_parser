from dataclasses import dataclass
from datetime import datetime, time
from bs4 import BeautifulSoup


@dataclass
class Row:
    login: str
    nickname: str
    rank: int
    mode: str
    record: str
    max_rank: int
    cps: int
    mapcps: str
    challenge: str
    envir: str
    record_date: datetime
    account: str


def extract_rows(page_html: str):
    rows = []
    soup = BeautifulSoup(page_html, "lxml")

    table = soup.select_one('form[name="stats"] > table:nth-child(2)')

    rows_tags = table.select('tr.tabl:nth-child(even)')

    for row_tag in rows_tags:
        cols = row_tag.select('td:nth-child(n+3):nth-child(-n + 16)')
        cols = row_tag.text.strip().splitlines()
        new_row = Row(
            login=cols[0],
            rank=int(cols[2]),
            nickname=cols[1],
            mode=cols[3],
            record=cols[4],
            max_rank=cols[6],
            cps=cols[7],
            mapcps=cols[8],
            challenge=cols[9],
            envir=cols[10],
            record_date=datetime.strptime(cols[11], '%Y-%m-%d %H:%M:%S'),
            account=cols[12],
        )

        rows.append(new_row)

    return rows
