def calculate_f1_score(confusion_matrix, cl):
    # Calculate precision, recall, and F1 score from the confusion matrix
    true_positive = confusion_matrix[1][1]
    false_positive = confusion_matrix[0][1]
    false_negative = confusion_matrix[1][0]

    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    
    # Calculate F1 score
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    print("_______" + str(cl) + "_______")
    print("Precision: " + str(precision))
    print("Recall: " + str(recall))
    print("F1 score: " + str(f1_score))
    print("______________________\n\n") 

# Example confusion matrix
confusion_matrix_icr = [[1, 15], [1, 83]]  # Format: [[true negative, false positive], [false negative, true positive]]
confusion_matrix_icm = [[1, 15], [1, 83]]  # Format: [[true negative, false positive], [false negative, true positive]]
confusion_matrix_ics = [[1, 15], [1, 83]]  # Format: [[true negative, false positive], [false negative, true positive]]

# Calculate F1 score
f1_score_icr = calculate_f1_score(confusion_matrix_icr, "incorrect")
f1_score_icm = calculate_f1_score(confusion_matrix_icm, "incomplete")
f1_score_ics = calculate_f1_score(confusion_matrix_ics, "inconsistent")
