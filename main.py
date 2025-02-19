from prettytable import PrettyTable
from datetime import date
from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == "__main__":
    table = PrettyTable()
    table.field_names = [date.today(), 'Имя работника', 'Зарплата']
    for _ in range(10):
        table.add_row(['', get_employees(), calculate_salary()])
    print(table)