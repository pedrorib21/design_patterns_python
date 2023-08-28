# High level classes or modules should not depend directly on low level modules
# Instead they should depend on abstractions (interfaces)

from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name) -> None:
        self.name = name


class RelationShipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationShipBrowser):
    def __init__(self) -> None:
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    # def __init__(self, relationships) -> None:
    # HIGH LEVEL MODULE ACESSING LOW LEVEL MODULE (BAD!)
    # relations = relationships.relations
    # for r in relations:
    #     if r[0].name == "John" and r[1] == Relationship.PARENT:
    #         print(f"John has a child called {r[2].name}")

    # BETTER SOLUTION
    # We can easily change the Relationships class
    # For instance saving a db or in a dict instead of a class
    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p} ")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
