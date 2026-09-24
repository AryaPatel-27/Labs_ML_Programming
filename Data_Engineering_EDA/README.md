# Data Engineering and Exploratory Data Analysis

## Project Overview

This project demonstrates a basic Data Engineering and Exploratory Data Analysis (EDA) workflow using Python, PostgreSQL, Pandas, and data visualization libraries.

Synthetic employee data is generated using Faker, stored in a Neon PostgreSQL database, retrieved using Python, cleaned and transformed using Pandas, and analyzed using different visualizations.

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Faker
- PostgreSQL
- Neon Database
- psycopg2
- Matplotlib
- Seaborn
- Scikit-learn
- python-dotenv

## Project Structure

```text
Data_Engineering_EDA/
│
├── notebook/
│   └── Data_Engineering_EDA.ipynb
│
├── src/
│   ├── database.py
│   ├── data_generator.py
│   ├── data_cleaning.py
│   └── insert_data.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## 1. Database Setup

A PostgreSQL database was created using Neon.

The `employees` table contains the following fields:

- `employee_id` - Unique employee ID
- `name` - Employee name
- `position` - IT-related job position
- `start_date` - Employee start date
- `salary` - Employee salary

## 2. Synthetic Data Generation

The Faker library was used to generate 100+ synthetic employee records.

The generated data includes:

- Employee names
- IT job positions
- Start dates between 2015 and 2024
- Salaries between $60,000 and $200,000

Some missing values, inconsistent position names, and duplicate-like data were also introduced to demonstrate data cleaning.

## 3. Data Collection

Python connects to the Neon PostgreSQL database using `psycopg2`.

The employee records are retrieved from PostgreSQL and loaded into a Pandas DataFrame for analysis.

## 4. Data Cleaning

The employee dataset was cleaned by:

- Removing extra spaces from text
- Correcting inconsistent job position names
- Handling missing values
- Removing duplicate employee records

## 5. Data Transformation

The `start_date` column was converted to a Pandas datetime format.

A new `start_year` column was extracted from the employee start date to make yearly analysis easier.

## 6. Feature Engineering

Additional features were created, including:

- `start_year`
- `years_of_service`
- `salary_level`

These features provide additional information for analysis.

## 7. Feature Scaling

Min-Max Scaling was applied to the salary column using Scikit-learn.

This created a `salary_scaled` feature with values between 0 and 1.

## 8. Exploratory Data Analysis

The dataset was explored using:

- `head()`
- `info()`
- `describe()`
- `isnull().sum()`
- Average salary calculations
- Employee counts by position
- Employee counts by start year

## 9. Data Visualization

A grouped bar chart was created to compare:

**Average Salary by Position and Start Year**

This visualization helps compare salary values across different IT positions and employee start years.

## 10. Additional Dataset and Data Integration

A second synthetic dataset was created containing department information such as:

- Department name
- Location
- Annual budget

Employee positions were mapped to departments, and the employee and department datasets were merged using Pandas.

## 11. Advanced Visualization

A heatmap was created to display:

**Average Salary by Department and Start Year**

The heatmap provides an easy way to compare average salary values across multiple departments and years.

## Conclusion

This project demonstrates an end-to-end data engineering and EDA workflow. Data was generated, stored in a cloud PostgreSQL database, collected using Python, cleaned, transformed, and enhanced with new features.

The project also demonstrates dataset integration, feature scaling, exploratory analysis, and data visualization.

The employee and department data used in this project are synthetic, so the results demonstrate data analysis techniques rather than real-world salary trends.

## Installation

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

## Running the Project

1. Create and activate a Python virtual environment.
2. Install the packages from `requirements.txt`.
3. Configure the Neon PostgreSQL database connection.
4. Run the Python scripts inside the `src` folder as required.
5. Open `notebook/Data_Engineering_EDA.ipynb`.
6. Run the notebook cells from top to bottom.

## Security

Database credentials are stored in a `.env` file.

The `.env` file and virtual environment are excluded from GitHub using `.gitignore`.
