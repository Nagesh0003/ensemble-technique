# ensemble-technique
# **Breast Cancer Prediction Using Ensemble Learning**

## **Overview**

This project implements an **ensemble machine learning approach** to predict breast cancer diagnosis based on **biopsy data**. Multiple machine learning models are trained and evaluated individually, and then combined using a **Voting Classifier** to improve prediction accuracy. The goal is to distinguish between **Malignant (cancerous) and Benign (non-cancerous) tumors**.

## **Technologies Used**

- Python
- Pandas & NumPy (for data manipulation)
- Matplotlib (for visualization)
- Scikit-Learn (for machine learning algorithms)

## **Dataset**

The dataset used is the **Breast Cancer Wisconsin (Diagnostic) Dataset**. It consists of various features extracted from digitized images of breast mass biopsies.

## **Project Workflow**

### **1. Data Preprocessing**

- Load dataset using Pandas.
- Drop unnecessary columns (e.g., ID).
- Encode the target variable (Malignant = 1, Benign = 0).
- Split dataset into **training (80%)** and **testing (20%)** sets.
- Normalize feature values using **StandardScaler**.

### **2. Training Individual Models**

The following models are trained individually to analyze their performance:

- **Logistic Regression** (Linear model for classification)
- **Decision Tree Classifier** (Tree-based model for feature splits)
- **Random Forest Classifier** (Ensemble of decision trees)
- **Gradient Boosting Classifier** (Boosting algorithm to improve weak models)
- **Support Vector Machine (SVM)** (Finds optimal decision boundary)

### **3. Ensemble Learning with Voting Classifier**

To improve accuracy, we combine the above models using **Soft Voting**, where models contribute based on their probability scores.

### **4. Performance Evaluation**

Each model's performance is evaluated using:

- **Accuracy Score** (Correct predictions/Total predictions)
- **ROC-AUC Score** (How well the model differentiates between classes)
- **Classification Report** (Precision, Recall, and F1-Score for each class)

### **5. Visualization**

A **bar chart** is generated comparing the accuracy and ROC-AUC scores of all models.

### **6. User Input & Prediction**

The model allows users to **input biopsy features manually**, and predicts whether the tumor is **Malignant or Benign** along with a **confidence score**.

## **Usage**

- Run the script to train models and evaluate their performance.
- Enter user input when prompted to get a cancer diagnosis prediction.
- Analyze the generated bar chart for model comparison.

## **Results**

- The ensemble model achieved the highest accuracy and ROC-AUC score compared to individual models.
- Soft voting improved the overall classification performance by leveraging the strengths of multiple models.

## **Future Improvements**

- Implement more advanced ensemble techniques (e.g., Stacking, Bagging).
- Incorporate deep learning (Neural Networks) for improved accuracy.
- Deploy as a **web-based application** for user-friendly access.

## **Author**

**Nagesh U S**





