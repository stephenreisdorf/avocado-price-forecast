import pandas as pd

def extract_and_transform():
    avocado_df = pd.read_csv("data/avocado.csv")
    avocado_df.set_index("Date", inplace=True)
    avocado_df.sort_index(inplace=True)
    avocado_df.drop('Unnamed: 0', axis="columns", inplace=True)
    return avocado_df
