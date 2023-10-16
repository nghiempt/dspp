import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Read the actual and predicted CSV files into dataframes
actual_df = pd.read_csv('/Users/nghiempt/Corporation/scientific_research/paper_policy/results/times06/llama_generate.csv')
predict_df = pd.read_csv('/Users/nghiempt/Corporation/scientific_research/paper_policy/results/times06/ft_3.5_byllama.csv')

# Read column names from the CSV file
column_names = list(actual_df.columns)

# Initialize an empty list to store dictionaries with metrics
results = []

# Iterate through each column in the dataframes
for idx, column in enumerate(column_names):
    # Calculate the confusion matrix for the current column
    actual_values = actual_df[column]
    predicted_values = predict_df[column]
    cm = confusion_matrix(actual_values, predicted_values)
    
    # Calculate accuracy, precision, recall, and F1 score
    accuracy = accuracy_score(actual_values, predicted_values)
    precision = precision_score(actual_values, predicted_values)
    recall = recall_score(actual_values, predicted_values)
    f1 = f1_score(actual_values, predicted_values)
    
    # Store metrics in a dictionary along with column name
    metrics = {
        'Column Name': column,
        'Confusion Matrix': cm,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1 Score': f1
    }
    
    # Append the dictionary to the results list
    results.append(metrics)

# Create a DataFrame from the list of dictionaries
results_df = pd.DataFrame(results)

# Set the column name as the index
results_df = results_df.set_index('Column Name')

# Display the DataFrame in Jupyter Notebook
results_df

print(results_df)
