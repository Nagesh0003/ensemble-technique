  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import StandardScaler, LabelEncoder
  from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
  from sklearn.linear_model import LogisticRegression
  from sklearn.tree import DecisionTreeClassifier
  from sklearn.svm import SVC
  from sklearn.metrics import classification_report, accuracy_score, roc_auc_score

  # Step 1: Load the Dataset
  file_path = "breast-cancer.csv"  # Change path if necessary
  data = pd.read_csv(file_path)
  print(data)

  # Step 2: Data Preprocessing
  # Drop unnecessary columns and encode the target variable
  data_cleaned = data.drop(['id'], axis=1)
  data_cleaned['diagnosis'] = LabelEncoder().fit_transform(data_cleaned['diagnosis'])  # Malignant=1, Benign=0

  # Split features and target variable
  X = data_cleaned.drop('diagnosis', axis=1)
  y = data_cleaned['diagnosis']

  # Split the dataset into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

  # Feature Scaling
  scaler = StandardScaler()
  X_train = scaler.fit_transform(X_train)
  X_test = scaler.transform(X_test)

# Step 3: Train Individual Models
# Initialize models
log_reg = LogisticRegression(random_state=42)
dec_tree = DecisionTreeClassifier(random_state=42)
rand_forest = RandomForestClassifier(random_state=42)
grad_boost = GradientBoostingClassifier(random_state=42)
svm = SVC(probability=True, random_state=42)

# Train and store models
models = {
    'Logistic Regression': log_reg,
    'Decision Tree': dec_tree,
    'Random Forest': rand_forest,
    'Gradient Boosting': grad_boost,
    'SVM': svm
}

# Train each model and evaluate performance
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    results[name] = {'Accuracy': acc, 'ROC-AUC': auc}

# Step 4: Create and Train Ensemble Model (Soft Voting)
voting_clf = VotingClassifier(
    estimators=[
        ('Logistic Regression', log_reg),
        ('Decision Tree', dec_tree),
        ('Random Forest', rand_forest),
        ('Gradient Boosting', grad_boost),
        ('SVM', svm)
    ],
    voting='soft'  # 'soft' considers probability scores, 'hard' takes majority vote
)

voting_clf.fit(X_train, y_train)
y_pred_ensemble = voting_clf.predict(X_test)
ensemble_acc = accuracy_score(y_test, y_pred_ensemble)
ensemble_auc = roc_auc_score(y_test, voting_clf.predict_proba(X_test)[:, 1])

# Add ensemble model results
results['Ensemble Model'] = {'Accuracy': ensemble_acc, 'ROC-AUC': ensemble_auc}

# Step 5: Visualize Model Performance
results_df = pd.DataFrame(results).T

plt.figure(figsize=(12, 6))
results_df[['Accuracy', 'ROC-AUC']].plot(kind='bar', rot=45, colormap='viridis')
plt.title('Model Performance Comparison')
plt.ylabel('Score')
plt.xlabel('Model')
plt.grid(axis='y')
plt.legend(loc='lower right')
plt.show()

# Display Classification Report
class_report = classification_report(y_test, y_pred_ensemble, target_names=['Benign', 'Malignant'])
print("\nClassification Report for Ensemble Model:")
print(class_report)

# Display Performance Summary
print("\n==============================")
print("      PERFORMANCE SUMMARY      ")
print("==============================")
print(f" Ensemble Model Accuracy: {ensemble_acc * 100:.2f}%")
print(f"Ensemble Model ROC-AUC: {ensemble_auc:.4f}")
print("==============================\n")

# Step 6: Predict Based on User Input
# Get feature names
feature_names = X.columns.tolist()

def get_user_input():
    """Collect user input for prediction."""
    print("\nEnter values for the following features:")
    user_input = []
    for feature in feature_names:
        value = float(input(f"{feature}: "))
        user_input.append(value)
    return np.array(user_input).reshape(1, -1)

# Get user input
user_input = get_user_input()

# Convert user input to DataFrame before scaling
user_input_df = pd.DataFrame(user_input, columns=feature_names)

# Scale the input
user_input_scaled = scaler.transform(user_input_df)

# Make prediction
prediction = voting_clf.predict(user_input_scaled)
probability = voting_clf.predict_proba(user_input_scaled)[0][1]  # Probability of malignancy

# Display the result
output = "🔴 Malignant (Cancerous)" if prediction[0] == 1 else "🟢 Benign (Non-Cancerous)"

print("\n==============================")
print("      PREDICTION RESULT       ")
print("==============================")
print(f"Predicted Diagnosis: {output}")
print(f"Confidence Score (Malignancy Probability): {probability:.4f}")
print("==============================\n")
