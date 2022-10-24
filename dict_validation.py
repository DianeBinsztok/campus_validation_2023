def create_people_by_age():
    return {}


def add_to_dict(people_by_age, name, age):
    people_by_age[name] = age
    return people_by_age


def dict_contains(people_by_age, name):
    # if name in people_by_age:
    #     return True
    return name in people_by_age


def age_of_people(people_by_age, name):
    return people_by_age[name]


def list_people(people_by_age):
    keys_list = []
    for key in people_by_age.keys():
        keys_list.append(key)
    return keys_list


def list_age(people_by_age):
    values_list = []
    for value in people_by_age.values():
        values_list.append(value)
    return values_list


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
    else:
        print("3) add_to_dict (and dict_contains)=> OK")

    if not dict_contains(people_by_age, "Robert Durand"):
        print("Error: dict does not contain Robert Durand")
    else:
        print("3) add_to_dict (and dict_contains)=> OK")

    if age_of_people(people_by_age, "John Doe") != 25:
        print("Error: age of John Doe is not 25")
    else:
        print("4) check dict value for given key => OK")

    if age_of_people(people_by_age, "Robert Durand") != 54:
        print("Error: age of Robert Durand is not 54")
    else:
        print("4) check dict value for given key => OK")

    if list_people(people_by_age) != ["John Doe", "Robert Durand"]:
        print("Error: list of people is not correct")
    else:
        print("5) list_people => OK")

    if list_age(people_by_age) != [25, 54]:
        print("Error: list of age is not correct")
    else:
        print("6) list_age => OK")


if __name__ == "__main__":
    main()
