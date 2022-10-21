def start_exercice():
    catch_division_by_zero()
    catch_int_conversion_error()
    catch_your_own_exception()

def catch_division_by_zero():
    try:
        5 / 0
    except ZeroDivisionError as e:
        print(f"Pour une division par zéro, le résultat est infini => {e}")



def catch_int_conversion_error():
    try:
        int("a")
    except ValueError as e:
        print(f"Cette valeur ne peut pas être convertie en nombre => {e}")


# équivalent de MyAwesomeException extends Exception
class MyAwesomeException(Exception):
    print(f"Opération impossible: {Exception.__name__}")



# def raise_my_own_exception():
#     raise MyAwesomeException


def catch_your_own_exception():
    exception_caught = False
    try:
        #raise_my_own_exception()
        raise MyAwesomeException
    except MyAwesomeException:
        exception_caught = True
    if not exception_caught:
        print("Error: MyAwesomeException not caught")


def main():
    try:
        start_exercice()
    except MyAwesomeException as a:
        print(f"Et là, ça marche? => {a}")
    except Exception as e:
        print(f"Error: Cette exception ne doit pas être capturée ici : {e}")


if __name__ == "__main__":
    main()
