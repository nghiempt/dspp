import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Read the actual and predicted CSV files into dataframes
actual_df = pd.read_csv('/Users/nghiempt/Corporation/scientific_research/paper_policy/_checklist/times02/generate_by_gpt3.0.csv')
predict_df = pd.read_csv('/Users/nghiempt/Corporation/scientific_research/paper_policy/_checklist/times01/origin_m100.csv')

# Initialize an empty dictionary to store confusion matrices and metrics
results = {}

# Iterate through each column in the dataframes
for column in actual_df.columns:
    # Calculate the confusion matrix for the current column
    actual_values = actual_df[column]
    predicted_values = predict_df[column]
    cm = confusion_matrix(actual_values, predicted_values)
    
    # Calculate accuracy, precision, and recall
    accuracy = accuracy_score(actual_values, predicted_values)
    precision = precision_score(actual_values, predicted_values)
    recall = recall_score(actual_values, predicted_values)
    
    # Store the confusion matrix and metrics in the results dictionary
    results[column] = {
        'Confusion Matrix': cm,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall
    }

# Print the results
for column, metrics in results.items():
    print(f"Metrics for '{column}':")
    print("Confusion Matrix:")
    print(metrics['Confusion Matrix'])
    print(f"Accuracy: {metrics['Accuracy']:.2f}")
    print(f"Precision: {metrics['Precision']:.2f}")
    print(f"Recall: {metrics['Recall']:.2f}")
    print()
