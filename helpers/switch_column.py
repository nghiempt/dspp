import pandas as pd

# Read data from CSV file
file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/results/times06/ft_3.5_byllama.csv'
df = pd.read_csv(file_path)

# Switch 'incomplete' and 'incorrect' columns
df['incomplete'], df['incorrect'] = df['incorrect'], df['incomplete']

# Write updated data back to the file
df.to_csv(file_path, index=False)

print("Columns switched and data written back to the file.")
