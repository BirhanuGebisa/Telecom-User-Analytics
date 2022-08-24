import pandas as pd
import numpy as np
# Function to calculate missing values by column


class Data_preprocess():

    def __init__(self, df: pd.DataFrame) -> None:
        
        self.df = df

     #clean the drop value columns 
    def drop_duplicate_row(self) -> pd.DataFrame:
        droped = self.df[self.df.duplicated()].index
        return self.df.drop(index=droped, inplace=True)

    def convert_to_datetime(self, df)-> pd.DataFrame:
        df['Start'] = pd.to_datetime(df['Start'])
        df['End'] = pd.to_datetime(df['End'])
        return df
    #convert to numberic values
    def convert_to_numbers(self) -> pd.DataFrame:
        self.df = self.df.apply(pd.to_numeric, errors='coerce')
        return self.df

     #drop the missing value of rows
    def drop_rows(self, columns)-> pd.DataFrame:
        self.df.drop(columns, axis=1, inplace=True)

    def drop_columns(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        for col in columns:
            df.drop(col, axis=1, inplace=True)
        return df

    #fill numeric with mean and media 
    def fill_numerical_column(self, column)-> pd.DataFrame:
        for col in column:
            skewness = self.df[col].skew() 
            if((-1 < skewness) and (skewness < -0.5)):
                self.df[col] = self.df[col].fillna(self.df[col].mean()) 
            else:
                self.df[col] = self.df[col].fillna(self.df[col].median())
    
    #fix outlier columns
    def fix_outlier(df, column)-> pd.DataFrame:
        df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])
        
        return df[column]

    #handle missing value of categorical data with mode
    def fill_categorical_columns(self, column)-> pd.DataFrame:
        for col in column:
            mode = self.df[col].mode()[0]
            self.df[col] = self.df[col].fillna(mode)
    
      #clean missing value the percentage is greater than 30 percent
    def get_column_based_missing(self):
        col_null = self.df.isnull().sum()
        total_entries = self.df.shape[0]
        missing_percentage = []
        for col_missing_entries in col_null:
            value = str(
                round(((col_missing_entries/total_entries) * 100), 2)) + " %"
            missing_percentage.append(value)

        missing_df = pd.DataFrame(col_null, columns=['total_missing_values'])
        missing_df['missing_percentage'] = missing_percentage
        return missing_df

    #convert the bytes to megabytes
    def convert_bytes_to_megabytes(self, column):
        megabyte = 1*10e+5
        Total_MB = []
        for i in column.values:
            i = i / megabyte
            Total_MB.append(i)

        return Total_MB


