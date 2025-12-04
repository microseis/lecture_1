from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")


class Solver():

    def __init__(self):
        print("This is my solver")


def add(a: int, b):
    return a + b


if __name__ == '__main__':
    solver = Solver()
