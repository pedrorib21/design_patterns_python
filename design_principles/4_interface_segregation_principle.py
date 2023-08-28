# People dont need to implement more than they need to

# Dont put too much info in an interface
# YAGNI - You aint going to need it

import abc


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        pass  # ok

    def fax(self, document):
        pass  # noop

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan!")


# BETTER SOLUTION


class Printer:
    @abc.abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abc.abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(cocument)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass

class MultiFunctionDevice(Printer, Scanner):
    @abc.abstractmethod
    def print(self, document):
        pass

    @abc.abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner) -> None:
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.print(document)

