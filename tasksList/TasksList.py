class TasksList(list):
    def __init__(self):
        self.list = []

    def add(self, task):
        self.list.append(task)

    def length(self):
        return len(self.list)

    def contains(self, task):
        return task in self.list

    def uppercase(self):
        new_list = TasksList()
        for item in self.list:
            new_list.add(item.upper())
            if len(self.list) > 10:
                break
        return new_list

