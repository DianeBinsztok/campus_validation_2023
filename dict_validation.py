def create_people_by_age():
    return {}



def add_to_dict(people_by_age, name, age):
    people_by_age[len(people_by_age)] = {"name": name, "age": age}
    return people_by_age



def dict_contains(people_by_age, name):
    pass


def age_of_people(people_by_age, name):
    pass


def list_people(people_by_age):
    pass


def list_age(people_by_age):
    pass


def size_of_dict(people_by_age):
    return len(people_by_age)


def main():
    people_by_age = create_people_by_age()
    if not isinstance(people_by_age, dict):
        print("Error: peoples_by_age is not a dict")
    else:
        print("1) create_people_by_age => OK")

    add_to_dict(people_by_age, "John Doe", 25)
    add_to_dict(people_by_age, "Robert Durand", 54)

    if size_of_dict(people_by_age) != 2:
        print("Error: dict size is not 2")
    else:
        print("2) add_to_dict (and size_of_dict)=> OK")

    if not dict_contains(people_by_age, "John Doe"):
        print("Error: dict does not contain John Doe")


    if not dict_contains(people_by_age, "Robert Durand"):
        print("Error: dict does not contain Robert Durand")

    if age_of_people(people_by_age, "John Doe") != 25:
        print("Error: age of John Doe is not 25")

    if age_of_people(people_by_age, "Robert Durand") != 54:
        print("Error: age of Robert Durand is not 54")

    if list_people(people_by_age) != ["John Doe", "Robert Durand"]:
        print("Error: list of people is not correct")

    if list_age(people_by_age) != [25, 54]:
        print("Error: list of age is not correct")


if __name__ == "__main__":
    main()
