# @author : Wangs_official
import os
import pandas as pd
from openpyxl import Workbook

with open("main.xlsx", "w") as f:
    f.close()
folder_path = '../../Desktop/文档/编程项目/CodemaoEduAutoReg/xls/'
main_wb = Workbook()
main_ws = main_wb.active
row_count = 1
for filename in os.listdir(folder_path):
    if filename.endswith('.xls'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_excel(file_path, skiprows=3)
        for index, row in df.iterrows():
            main_ws.append(row.tolist())
            row_count += 1
output_file = './main.xlsx'
main_wb.save(output_file)
print(f'数据已成功写入到 {output_file}')
