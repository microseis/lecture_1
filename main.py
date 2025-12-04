from dotenv import load_dotenv
import os

load_dotenv()


class Solver():
    """Очень важный класс."""

    def __init__(self):
        print("This is my solver")


def add(a: int, b: int):
    return a + b


if __name__ == '__main__':
    solver = Solver()
    database_url = os.getenv("DATABASE_PASSWORD")
    print(database_url)
