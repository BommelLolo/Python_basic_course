class BuildReports:
    def build_employee_report(self):
        pass

    def build_company_report(self):
        pass


class ReportsPrinter:
    def print_using_local_office_printer(self, report):
        pass


class Employee:
    def get_daily_rate(self):
        return self._daily_rate


class Manager(Employee):
    _daily_rate = 100


class Programmer(Employee):
    _daily_rate = 200


class Director(Employee):
    _daily_rate = 500


class Accountant(Employee):
    _daily_rate = 300


class SalaryCounter:
    def get_salary(self, employee):
        if isinstance(employee, Employee):
            return employee.get_daily_rate() * 365

        raise ValueError


class JsonResponseReader:
    def read_json(self):
        raise NotImplementedError


class TextResponseReader:
    def read_text(self):
        raise NotImplementedError


class XMLResponseReader:
    def read_xml(self):
        raise NotImplementedError


class ExampleDotComReader(TextResponseReader, XMLResponseReader):
    def read_text(self):
        pass

    def read_xml(self):
        pass


class Engine:
    def __init__(self, volume):
        self.volume = volume


class Vehicle:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine


class Truck(Vehicle):
    pass


class Auto(Vehicle):
    pass


if __name__ == '__main__':
    employees = [Manager(), Director(), Programmer()]
    for employee in employees:
        print(SalaryCounter().get_salary(employee))

    mazda = Auto('mazda', Engine(2))
    audi = Auto('audi', Engine(2.4))
    