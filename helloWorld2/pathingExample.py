from pathlib import Path
import openpyxl as xl

path = Path()
print(path.glob('*'))  # all files and directories
print(path.glob('*.*'))  # all files
print(path.glob('*.py'))  # all files of type

# print all the python files in the directory
for file in path.glob('*.py'):
    print(file)

wb = xl.load_workbook('ExampleLvL15(charSheet)Excel.xlsx')
sheet = wb['Tester']
cell = sheet['a1']
cell2 = sheet.cell(1, 2)
print(cell.value)
print(cell2.value)

for row in range(1, sheet.max_row + 1):
    print(row)