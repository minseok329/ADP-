from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
import lightgbm as lgb
from sklearn.metrics import accuracy_score, classification_report

X = df1.drop('absences', axis = 1)
y = df1['absences']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 24, stratify = y)

sc = StandardScaler()
X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()
X_train_scaled = sc.fit_transform(X_train_scaled)
X_test_scaled = sc.transform(X_test_scaled)

rf = RandomForestClassifier()
nn = MLPClassifier()
lg = lgb.LGBMClassifier()

rf.fit(X_train_scaled, y_train)
nn.fit(X_train_scaled, y_train)
lg.fit(X_train_scaled, y_train)

y_rf = rf.predict(X_test_scaled)
y_nn = nn.predict(X_test_scaled)
y_lg = lg.predict(X_test_scaled)

print("Accuracy:", accuracy_score(y_test, y_rf))
print("Accuracy:", accuracy_score(y_test, y_nn))
print("Accuracy:", accuracy_score(y_test, y_lg))

print(classification_report(y_test, y_rf))
print(classification_report(y_test, y_nn))
print(classification_report(y_test, y_lg))