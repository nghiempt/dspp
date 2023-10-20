#Import the necessary libraries 
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

# Đọc dữ liệu từ các tệp CSV
actual_data = pd.read_csv('/Users/nghiempt/Corporation/scientific_research/paper_policy/results/times02/3.0_random_origin copy.csv')
predict_data = pd.read_csv('/Users/nghiempt/Corporation/scientific_research/paper_policy/results/times02/ft_3.5_by3.0_origin copy.csv')

# Lấy cột 'incorrect', 'incomplete', 'inconsistent' từ cả hai tệp
actual_incorrect = actual_data['incorrect'].values
actual_incomplete = actual_data['incomplete'].values
actual_inconsistent = actual_data['inconsistent'].values

predict_incorrect = predict_data['incorrect'].values
predict_incomplete = predict_data['incomplete'].values
predict_inconsistent = predict_data['inconsistent'].values

# Tính toán ma trận nhầm lẫn cho từng loại lỗi
confusion_matrix_incorrect = confusion_matrix(actual_incorrect, predict_incorrect)
confusion_matrix_incomplete = confusion_matrix(actual_incomplete, predict_incomplete)
confusion_matrix_inconsistent = confusion_matrix(actual_inconsistent, predict_inconsistent)

# In ma trận nhầm lẫn
print("Confusion Matrix for 'incorrect':")
print(confusion_matrix_incorrect)
print("\nConfusion Matrix for 'incomplete':")
print(confusion_matrix_incomplete)
print("\nConfusion Matrix for 'inconsistent':")
print(confusion_matrix_inconsistent)
