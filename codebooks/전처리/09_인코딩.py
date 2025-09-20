## 순서형들은 int형으로 되어 있으므로 라벨인코딩하지 않았다.
df1 = pd.get_dummies(data = df1, columns = ['sex', 'pstatus', 'guardian'], drop_first = True)
df1.info()