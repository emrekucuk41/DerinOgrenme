import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

df = pd.read_csv('data.csv')

df = df.drop(['id', 'Unnamed: 32'], axis=1, errors='ignore')

df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)

y_pred = rf_model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("--- Model Değerlendirme Sonuçları ---")
print(f"Accuracy (Doğruluk):  {accuracy:.4f}  (%{accuracy*100:.2f})")
print(f"Precision (Kesinlik): {precision:.4f}  (%{precision*100:.2f})")
print(f"Recall (Duyarlılık):  {recall:.4f}  (%{recall*100:.2f})")
print(f"F1-Score:             {f1:.4f}  (%{f1*100:.2f})")