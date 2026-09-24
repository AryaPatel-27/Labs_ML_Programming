import pandas as pd


def clean_employee_data(df):
    """
    Clean the employee dataset.
    """

    df = df.copy()

    # Remove extra spaces from text columns
    df["name"] = df["name"].str.strip()
    df["position"] = df["position"].str.strip()

    # Standardize position names
    position_corrections = {
        "software developer": "Software Developer",
        "Software developer": "Software Developer",
        "data analyst": "Data Analyst",
        "Data analyst": "Data Analyst",
        "network engineer": "Network Engineer",
        "Network engineer": "Network Engineer",
        "cloud engineer": "Cloud Engineer",
        "Cloud engineer": "Cloud Engineer",
        "cybersecurity analyst": "Cybersecurity Analyst",
        "Cybersecurity analyst": "Cybersecurity Analyst",
        "DATA ANALYST": "Data Analyst",
        "network administrator": "Network Administrator"
    }

    df["position"] = df["position"].replace(position_corrections)

    # Remove records with missing important values
    df = df.dropna(
        subset=["name", "position", "start_date", "salary"]
    )

    # Remove duplicate rows
    df = df.drop_duplicates()

    return df