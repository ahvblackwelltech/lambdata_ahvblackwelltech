
import pandas as pd
from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint
from IPython.display import display




def changeColumnsName(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', ''))
    return df


class MyDataSplitter():

    def __init__(self, df):
        self.df = df

    def train_validation_test_split(self, features, target,
                                    train_size=0.7, val_size=0.1, 
                                    test_size=0.2, random_state=None, 
                                    shuffle=True):

        X_train_val, X_test, y_train_val, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, shuffle=shuffle)

        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size/(train_size+val_size),
            random_state=random_state, shuffle=shuffle)

        return X_train, X_val, X_test, y_train, y_val, y_test
    
    def dateDivider(self, date_col):
        converted_df  = self.df.copy()
        converted_df['Year'] = pd.DatetimeIndex(converted_df[date_col]).year
        converted_df['Month'] = pd.DatetimeIndex(converted_df[date_col]).month
        converted_df['Day'] = pd.DatetimeIndex(converted_df[date_col]).day
        return converted_df




if __name__ == '__main__':
    df = pd.read_csv('burritos.csv')
    breakpoint()

    print(df.shape)

    
