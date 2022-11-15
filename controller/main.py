from model.human import Human
from model.logic import Analyst
from util.creator import HumanCreator
from util.convertor import Convertor

def main():
    ls = HumanCreator.create(5)
    print(Convertor.convert_to_string(ls))

    count_adults = Analyst.count_adults(ls)
    count_alives = Analyst.count_alive_people(ls)

    print(f"Count of adults: {count_adults}")
    print(f"Count of alive: {count_alives}")

if __name__ == "__main__":
    main()