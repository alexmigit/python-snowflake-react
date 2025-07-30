import pandas as pd

def get_data():
    """
    Loads production log, machines, parts, and operators data from CSV files 
    and returns them as a dictionary of DataFrames.
    """
    return {
        "log": pd.read_csv("data/production_log.csv"),
        "machines": pd.read_csv("data/machines.csv"),
        "parts": pd.read_csv("data/parts.csv"),
        "operators": pd.read_csv("data/operators.csv")
    }