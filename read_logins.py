from dataclasses import dataclass
from typing import List


@dataclass
class Player:
    tag: str
    nickname: str
    login: str


def players_from_file(file_name: str) -> List[Player]:
    with open(file_name, 'r') as f:
        logins = [line.strip() for line in f.readlines()]

        logins = [login.split(' ') for login in logins]
    logins = [Player(login[0], login[1], login[2][1:-1]) for login in logins]
    return logins
