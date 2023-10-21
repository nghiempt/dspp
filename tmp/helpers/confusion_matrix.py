import pandas as pd
from sklearn.metrics import confusion_matrix

# Read the actual and predicted CSV files into dataframes
actual_df = pd.read_csv('/Users/nghiempt/Corporation/scientific_research/paper_policy/evaluation/case_03_gpt3.0/csv/actual.csv')
predict_df = pd.read_csv('/Users/nghiempt/Corporation/scientific_research/paper_policy/evaluation/case_03_gpt3.0/csv/predict.csv')

# Initialize an empty dictionary to store confusion matrices
confusion_matrices = {}

# Iterate through each column in the dataframes
for column in actual_df.columns:
    # Calculate the confusion matrix for the current column
    actual_values = actual_df[column]
    predicted_values = predict_df[column]
    cm = confusion_matrix(actual_values, predicted_values)
    
    # Store the confusion matrix in the dictionary
    confusion_matrices[column] = cm

# Print the confusion matrices
for column, cm in confusion_matrices.items():
    print(f"Confusion Matrix for '{column}':")
    print(cm)
