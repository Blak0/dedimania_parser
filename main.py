from dataclasses import dataclass
from datetime import datetime
from typing import List

from date_filtering import rows_of_month, rows_until_date
from extract import extract_rows
from read_logins import players_from_file
from scrap import scrape_login_records


@dataclass
class RecordCount:
    login: str
    nickname: str
    records_count: int


if __name__ == '__main__':
    year = 2022
    month = 6

    # Read logins.txt
    players = players_from_file("logins.txt")

    login_records_count: List[RecordCount] = []

    for player in players:
        # Get rows from all pages containing records after specified date
        rows = scrape_login_records(
            row_extract_strategy=extract_rows,
            login=player.login,
            until=datetime(year, month, 1)
        )

        # Filter records by month and year
        records = rows_of_month(rows, month, year)

        login_records_count.append(RecordCount(
            player.login, player.nickname, len(records)))
        break
    # Sort users by most records descending
    login_records_count.sort(key=lambda x: x.records_count, reverse=True)

    # Pring filtered out records
    for idx, record in enumerate(login_records_count):
        print(f'{idx+1}. {record.nickname} - {record.records_count}')
