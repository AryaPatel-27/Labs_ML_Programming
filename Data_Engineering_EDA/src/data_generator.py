from faker import Faker
import random
from datetime import date

# Create Faker object
fake = Faker()


# IT-related positions
POSITIONS = [
    "Software Developer",
    "Data Analyst",
    "Network Administrator",
    "Cybersecurity Analyst",
    "Cloud Engineer",
    "Database Administrator",
    "DevOps Engineer",
    "IT Support Specialist",
    "Systems Administrator",
    "Network Engineer"
]


def generate_employees(number_of_employees=100):
    """
    Generate synthetic employee records with some data-quality issues.
    """

    employees = []

    # Create normal employee records
    for employee_id in range(1, number_of_employees + 1):

        employee = {
            "employee_id": employee_id,
            "name": fake.name(),
            "position": random.choice(POSITIONS),
            "start_date": fake.date_between(
                            start_date=date(2015, 1, 1),
                            end_date=date(2024, 12, 31)
            ),
            "salary": random.randint(60000, 200000)
        }

        employees.append(employee)

    # --------------------------------------------------
    # Add missing values to 20 different records
    # --------------------------------------------------

    # 5 missing names
    for employee_id in range(1, 6):
        employees[employee_id - 1]["name"] = None

    # 5 missing positions
    for employee_id in range(6, 11):
        employees[employee_id - 1]["position"] = None

    # 5 missing start dates
    for employee_id in range(11, 16):
        employees[employee_id - 1]["start_date"] = None

    # 5 missing salaries
    for employee_id in range(16, 21):
        employees[employee_id - 1]["salary"] = None

    # --------------------------------------------------
    # Add inconsistent position names
    # --------------------------------------------------

    employees[20]["position"] = " software developer "
    employees[21]["position"] = "DATA ANALYST"
    employees[22]["position"] = "network administrator"

    # --------------------------------------------------
    # Add a duplicate employee record
    # --------------------------------------------------

    duplicate_employee = employees[23].copy()
    duplicate_employee["employee_id"] = 101

    employees.append(duplicate_employee)

    return employees


if __name__ == "__main__":

    employees = generate_employees(100)

    print("Number of records generated:", len(employees))

    print("\nFirst 5 records:")

    for employee in employees[:5]:
        print(employee)

    # Count missing values
    print("\nMissing values:")

    missing_names = sum(
        employee["name"] is None
        for employee in employees
    )

    missing_positions = sum(
        employee["position"] is None
        for employee in employees
    )

    missing_dates = sum(
        employee["start_date"] is None
        for employee in employees
    )

    missing_salaries = sum(
        employee["salary"] is None
        for employee in employees
    )

    print("Missing names:", missing_names)
    print("Missing positions:", missing_positions)
    print("Missing start dates:", missing_dates)
    print("Missing salaries:", missing_salaries)