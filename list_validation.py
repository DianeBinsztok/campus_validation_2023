from tasksList.TasksList import TasksList
from tasksList import say

def create_task_list():
    return TasksList()


def add_to_list(list_task: TasksList, task):
    list_task.add(task)


def size_of_list(list_task: TasksList):
    return list_task.length()


def list_contains(list_task: TasksList, task):
    return list_task.contains(task)


def upper_task_in_tasklist(list_task: TasksList):
    return list_task.uppercase()


def main():
    say("Hello")
    list_task = create_task_list()

    if not isinstance(list_task, list):
        print("Error: list_task is not a list")
    else:
        print("1) create_task_list => OK")

    add_to_list(list_task, "task1")
    add_to_list(list_task, "task2")
    if size_of_list(list_task) != 2:
        print("Error: list size is not 2")
    else:
        print("2) add_to_list => OK")

    if not list_contains(list_task, "task1"):
        print("Error: list does not contain task1")
    else:
        print("3) list_contains for task1 => OK")

    if not list_contains(list_task, "task2"):
        print("Error: list does not contain task2")
    else:
        print("3) list_contains for task2 => OK")

    task_list_upper = upper_task_in_tasklist(list_task)

    if not list_contains(task_list_upper, "TASK1"):
        print("Error: list does not contain TASK1")
    else:
        print("4) upper_task_in_tasklist for TASK1 => OK")

    if not list_contains(task_list_upper, "TASK2"):
        print("Error: list does not contain TASK2")
    else:
        print("4) upper_task_in_tasklist for TASK2 => OK")

    if size_of_list(task_list_upper) != 2:
        print("Error: list size is not 2")
    else:
        print("5) size_of_list(task_list_upper) => OK")


if __name__ == "__main__":
    main()
