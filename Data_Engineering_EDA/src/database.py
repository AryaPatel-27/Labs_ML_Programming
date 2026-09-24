import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv


# Find the .env file in the project folder
project_folder = Path(__file__).resolve().parent.parent
env_file = project_folder / ".env"

load_dotenv(env_file)


def connect_to_database():
    """
    Connect to the Neon PostgreSQL database.
    """

    connection_string = os.getenv("DATABASE_URL")

    if connection_string is None:
        raise ValueError("DATABASE_URL was not found.")

    connection = psycopg2.connect(connection_string)

    return connection


def insert_employees(employees):
    """
    Insert employee records into the employees table.
    """

    connection = connect_to_database()

    cursor = connection.cursor()

    query = """
        INSERT INTO employees
        (employee_id, name, position, start_date, salary)
        VALUES (%s, %s, %s, %s, %s)
    """

    employee_records = []

    for employee in employees:
        employee_records.append(
            (
                employee["employee_id"],
                employee["name"],
                employee["position"],
                employee["start_date"],
                employee["salary"]
            )
        )

    cursor.executemany(query, employee_records)

    connection.commit()

    cursor.close()
    connection.close()

    print(f"{len(employee_records)} employee records inserted successfully.")


if __name__ == "__main__":

    connection = connect_to_database()

    print("Successfully connected to Neon PostgreSQL!")

    connection.close()

    print("Database connection closed.")