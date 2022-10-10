import json
from dataclasses import dataclass, field


def get_wc_data() -> list[dict]:
    data = json.load(open("worldcupdata.json", "r"))
    return data


@dataclass
class Winner:
    country: str
    year: int
    competition: str


def show_wc_data(wc_data: list[Winner]):
    def format_competition(competition: str):
        return "Fifa Women's World Cup" if competition == "women" else "Fifa Men's World Cup"

    for winner in wc_data:
        print(f"{winner.country} won {format_competition(winner.competition)} in {winner.year}")


if __name__ == '__main__':
    data: list[dict] = get_wc_data()
    winners: list[Winner] = [Winner(country=w['country'], year=int(w['year']), competition=w['competition'])
                             for w in data]

    show_wc_data(winners)

