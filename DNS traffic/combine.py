import pandas as pd

path_to_excel_file = 'C:\\Users\\Dell\\Downloads\\New CSV_2022\\Bell_DNS Dataset\\dataset.csv'  # Điền đường dẫn đến file Excel của bạn
data = pd.read_csv(path_to_excel_file)

data['Combined_Columns'] = data['hehe'] + '.' + data['haha']

output_file = 'combined_values.txt'  # Tên file xuất ra
data['Combined_Columns'].to_csv(output_file, sep='\t', index=False, header=False)  # Xuất ra file văn bản, cách nhau bởi tab (\t)
