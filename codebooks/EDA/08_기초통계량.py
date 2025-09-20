df1.info()

df1[['age']].describe().T

for i in df1.columns:
    print(df1[i].value_counts())