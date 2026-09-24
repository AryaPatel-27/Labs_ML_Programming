from data_generator import generate_employees
from database import insert_employees


employees = generate_employees(100)

print("Generated records:", len(employees))

insert_employees(employees)