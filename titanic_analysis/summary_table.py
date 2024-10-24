import pandas as pd

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    # Create lists to store the information
    features = []
    dtypes = []
    unique_values = []
    has_missing = []
    
    # Get information for each feature
    for column in df.columns:
        features.append(column)
        dtypes.append(str(df[column].dtype))
        unique_values.append(df[column].nunique())
        has_missing.append(df[column].isnull().any())
    
    # Create the summary DataFrame
    summary_df = pd.DataFrame({
        'Feature': features,
        'Type': dtypes,
        'Unique_Values': unique_values,
        'Has_Missing': has_missing
    })
    
    return summary_df
