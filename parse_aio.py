import pandas as pd
xl = pd.ExcelFile(r'C:\Users\lucas.truong\Downloads\AIO2026_v7.xlsx')
df1 = pd.read_excel(xl, 'Module 1')
df2 = pd.read_excel(xl, 'Module 2')
df3 = pd.read_excel(xl, 'Module 3')

with open('aio_m1_m2.txt', 'w', encoding='utf-8') as f:
    f.write('=== MODULE 1 ===\n')
    f.write(df1.to_string())
    f.write('\n=== MODULE 2 ===\n')
    f.write(df2.to_string())
    f.write('\n=== MODULE 3 ===\n')
    f.write(df3.to_string())
