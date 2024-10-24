import pandas as pd

def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': ['Age', 'Fare'],
            'discrete': ['SibSp', 'Parch']
        },
        'categorical': {
            'nominal': ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'],
            'ordinal': ['Pclass']
        }
    }
    return feature_types

