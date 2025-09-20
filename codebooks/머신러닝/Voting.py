from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report

## 개별 모델 정의
rf = RandomForestClassifier()
nn = MLPClassifier()
lg = lgb.LGBMClassifier()

## 소프트, 하드 보팅 앙상블 모델
soft = VotingClassifier(
estimators = [
    ('random Forest', rf),
    ('Neural Network', nn),
    ('LightGBM', lg)
], voting = 'soft')

hard = VotingClassifier(
estimators = [
    ('random Forest', rf),
    ('Neural Network', nn),
    ('LightGBM', lg)
], voting = 'hard')

## 학습
soft.fit(X_train_scaled, y_train)
hard.fit(X_train_scaled, y_train)

## 예측 및 성능 평가
y_soft = soft.predict(X_test)
y_hard = hard.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_soft))
print(classification_report(y_test, y_soft))
print("Accuracy:", accuracy_score(y_test, y_hard))
print(classification_report(y_test, y_hard))