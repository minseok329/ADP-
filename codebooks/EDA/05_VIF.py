# VIF 계수를 보기 전에 문자형 변수 -> 수치형으로 인코딩하자
df = pd.get_dummies(df,drop_first=True)

# 다중공산성을 보자
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif["variable"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif)