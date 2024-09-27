import pandas as pd
import numpy as np

file_path = "data/raw/"

def load_data(file_path):
    """
    Load CSV data from the given file path.
    
    :param file_path: Path to the CSV file containing transaction data.
    :return: DataFrame with the loaded data.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
    except Exception as e:
        print(f"Error loading data: {e}")
        raise
    return df

def clean_data(df):
    """
    Clean the DataFrame by handling missing values and correcting types.
    For this project, we establish a standard naming convention for columns in a typical csv file containing transactional data, however we understand that this varies greatly based on the source of the data, and future reserach will hopefully allow us to accurately be able to receive this data from any source. 

    :param df: DataFrame to clean.
    :return: Cleaned DataFrame.
    """
    # Drop rows with missing values
    df = df.dropna()
    
    # You may want to convert some columns to appropriate dtypes if necessary
    # df['some_column'] = df['some_column'].astype('float64')
    
    # Example: Remove outliers based on a certain threshold
    # df = df[df['transaction_amount'] <= threshold]

    print("Data cleaned successfully.")
    return df

def feature_engineering(df):
    """
    Perform feature engineering to create new features for model training.
    
    :param df: DataFrame with existing features.
    :return: DataFrame with engineered features.
    """
    # Example: Create a new feature for the log of the transaction amount
    df['log_transaction_amount'] = np.log1p(df['transaction_amount'])

    # Example: Convert transaction time to datetime and extract features
    df['transaction_time'] = pd.to_datetime(df['transaction_time'])
    df['hour'] = df['transaction_time'].dt.hour
    df['day_of_week'] = df['transaction_time'].dt.dayofweek

    print("Feature engineering completed.")
    return df

def preprocess_data(file_path):
    """
    Load, clean, and engineer features for the data.
    
    :param file_path: Path to the CSV file containing transaction data.
    :return: A DataFrame containing the processed data.
    """
    df = load_data(file_path)
    df = clean_data(df)
    df = feature_engineering(df)
    return df

if __name__ == "__main__":
    processed_data = preprocess_data('data/transaction_data.csv')
    print(processed_data.head())  # Display the first few rows of the processed data
