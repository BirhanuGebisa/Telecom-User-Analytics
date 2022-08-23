import pandas as pd

class DataFrame:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def list_coloumn_names(self) -> pd.DataFrame:
        return self.df.columns
    
    def get_columns_list(self)-> pd.DataFrame:
        return self.df.columns.to_list()
    
    def format_float(value)-> pd.DataFrame:
        return f'{value:,.2f}'

    def show_data_information(self) -> pd.DataFrame:
        return self.df.info()

    def show_data_description(self) -> pd.DataFrame:
        return self.df.describe()

    def show_correlation(self) -> pd.DataFrame:
        return self.df.corr()
    
    def get_null_counts(self)-> pd.DataFrame:
        print(self.df.isnull().sum())

    def skewness(self)-> pd.DataFrame:
        print(self.df.skew())