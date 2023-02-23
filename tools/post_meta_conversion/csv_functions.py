import pandas as pd


def load_csv_data(file_path:str):
    df = pd.read_csv(file_path)
    return df

def get_post_csv_data(csv, column_name:str, column_value:str):
    return csv.loc[csv[column_name] == column_value]