from app.knights.knight_info import KNIGHTS
from app.fights.battle_prep import prepare_knights
from app.fights.battle import battle


def main() -> None:
    knights = prepare_knights(KNIGHTS)
    results = battle(knights)
    print(results)


if __name__ == "__main__":
    main()
