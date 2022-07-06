from datetime import datetime
from typing import Callable, List

from selenium.webdriver.common.by import By

from driver import init_driver
from extract import Row


def scrape_login_records(row_extract_strategy:  Callable[[str],  List[Row]], login: str, until: datetime) -> List[Row]:
    url = f'http://dedimania.net/tm2stats/?do=stat&Mode=ALL&Rank=RANK-1&ReplayOrder=NONE&Login={login}&NickName=&Envir=Stadium&RecOrder=NONE&RecOrder2=DATE-DESC&RecOrder3=RANK-ASC&Challenge=&Author=&UId=&RecMore=RD&Show=RECORDS&Limit=100&Start=1'
    driver = init_driver()
    print('-' * 100)
    print(f'Scrapping {login}')
    driver.get(url)

    idx = 1
    rows = []
    while True:
        s = driver.find_element(By.NAME, 'Start')
        s.clear()
        s.send_keys(str(idx))
        button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        button.click()
        print('.', end='', flush=True)

        rows_from_page = row_extract_strategy(driver.page_source)

        if rows_from_page == []:
            break

        rows.extend(rows_from_page)

        if until is not None and rows_from_page[-1].record_date < until:
            break

        idx += 100
    print('\nDone.\n')

    return rows
