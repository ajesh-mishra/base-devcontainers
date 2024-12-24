from sqlmodel import Session

from database import create_db_and_tables, engine
from models.post import Team, Hero


def create_heroes():
    with Session(engine) as session:
        team_z_force = Team(name="Avengers", headquarters="Stark Towers")

        hero_deadpond = Hero(
            name="Ironman", secret_name="Tony Stark", team=team_z_force
        )
        session.add(hero_deadpond)
        session.commit()

        session.refresh(hero_deadpond)

        print("Created hero:", hero_deadpond)
        print("Hero's team:", hero_deadpond.team)


def main():
    create_db_and_tables()
    create_heroes()


if __name__ == "__main__":
    main()
