
import pandas as pd
from pandas_profiling import ProfileReport

''' Change column names: replace 
    spaces with underscores
'''

def changeColumnsName(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', ''))
    return df

''' Train/validate/test 
    split function for 
    a dataframe
'''

def train_validation_test_split(X, y, train_size=0.7, 
                                val_size=0.1, test_size=0.2, 
                                random_state=None, shuffle=True):

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size/(train_size+val_size),
        random_state=random_state, shuffle=shuffle)

    return X_train, X_val, X_test, y_train, y_val, y_test


if __name__ == '__main__':
    df = pd.read_csv('burritos.csv')
    breakpoint()

    print(df.shape)

    
