import pandas as pd

# Đọc hai tệp CSV
df1 = pd.read_csv('/Users/nghiempt/Corporation/scientific_research/paper_policy/results/times01/manual_100.csv')
df2 = pd.read_csv('/Users/nghiempt/Corporation/scientific_research/paper_policy/results/times01/origin_m100.csv')



# Tìm các phần tử giống nhau và khác nhau
common_elements = pd.merge(df1, df2, how='inner')
different_elements = pd.concat([df1, df2]).drop_duplicates(keep=False)

# In 5 dòng đầu của kết quả
print("Các phần tử giống nhau (5 dòng đầu):")
print(common_elements.head())

print("\nCác phần tử khác nhau (5 dòng đầu):")
print(different_elements.head())
