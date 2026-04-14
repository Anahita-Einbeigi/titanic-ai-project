import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =========================
# Ladda data
# =========================
df = pd.read_csv("titanic.csv")

print("\n--- Första rader ---")
print(df.head())

print("\n--- Info ---")
print(df.info())

# =========================
# Data cleaning
# =========================

# Fyll saknade värden
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Ta bort irrelevanta kolumner
df = df.drop(["Name", "Ticket", "Cabin", "PassengerId"], axis=1)

# One-hot encoding
df = pd.get_dummies(df, drop_first=True)

# Kontrollera saknade värden
print("\n--- Saknade värden efter cleaning ---")
print(df.isna().sum())

# =========================
# Visualisering
# =========================

sns.countplot(x="Sex_male", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.show()

# =========================
# Train/test split
# =========================

from sklearn.model_selection import train_test_split

X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# =========================
# Modell 1: Logistic Regression
# =========================

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

model_lr = LogisticRegression(max_iter=1000)
model_lr.fit(X_train, y_train)

y_pred_lr = model_lr.predict(X_test)

print("\n=========================")
print("Logistic Regression Result")
print("=========================")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))

# =========================
# Modell 2: Decision Tree (VG)
# =========================

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=5, random_state=42)
tree.fit(X_train, y_train)

y_pred_tree = tree.predict(X_test)

print("\n=========================")
print("Decision Tree Result")
print("=========================")
print("Accuracy:", accuracy_score(y_test, y_pred_tree))

# =========================
# Modelljämförelse (VG)
# =========================

print("\n=========================")
print("Model Comparison")
print("=========================")

print("Logistic Regression:", accuracy_score(y_test, y_pred_lr))
print("Decision Tree:", accuracy_score(y_test, y_pred_tree))

# =========================
# Extra analys (VG)
# =========================

print("\n--- Viktig insikt ---")
print("Kön och biljettklass verkar vara starka faktorer för överlevnad.")