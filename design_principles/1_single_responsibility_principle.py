# You don't want to overload your objects with lots of responsibilities

# A class should only have one reason to change
# Separation of Concerns


class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        return "\n".join(self.entries)

    # THIS IS A PROBLEM
    # Now the jounal is also responsible for persistency
    # Imagine we have several save multiple classes

    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


# GOOD SOLUTION
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close


j = Journal()
j.add_entry("I cried today")
j.add_entry("I ate a bug")
print(j)

file = "temp.txt"
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
