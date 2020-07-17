from my_lambda.helper_utility import dateDivider

df = pd.csv_read('burritos.csv')
df_date = df['Date']


print(dateDivider(df_date))
