from dataclasses import dataclass
from datetime import datetime
from scrap import scrape_login_records
from extract import extract_rows
from date_filtering import rows_until_date


@dataclass
class LoginRecord:
    login: str
    records_count: int


if __name__ == '__main__':
    date = '2022-01-01'

    with open('logins.txt', 'r') as f:
        logins = [line.strip() for line in f.readlines()]

    until_date = datetime.strptime(date, '%Y-%m-%d')

    print(
        f'\nScrapping between {datetime.now().strftime("%Y-%m-%d")} and {until_date.strftime("%Y-%m-%d")} (included)')

    login_records_count = []

    for login in logins:
        # Get rows from all pages containing records after specified date
        rows = scrape_login_records(
            row_extract_strategy=extract_rows,
            login=login,
            until=until_date
        )

        # Filter records scored before date that weren't filtered on last page
        records = rows_until_date(rows, until=until_date)

        login_records_count.append(LoginRecord(login, len(records)))

    login_records_count.sort(key=lambda x: x.records_count, reverse=True)

    for record in login_records_count:
        print(f'User {record.login} - {record.records_count} first places')
