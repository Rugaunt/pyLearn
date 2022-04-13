from pathlib import Path
import openpyxl as xl


workbook_file_name = 'ItemLists.xlsx'
save_file_name = 'test1.xlsx'
# wondrous_sheet_name = 'WondrousItems'
# TODO workbook_file_path = ''


def process_workbook(wondrous_sheet_name, roll, prefix, affix, item_type):
    wb = xl.load_workbook(workbook_file_name)
    item_sheet = wb[wondrous_sheet_name]
    position_array = []
    item_name = "None"
    # find positions of acceptable items in spreadsheet
    for i in item_sheet.max_row:
        if item_sheet.cell(i, 1).value == item_type and item_sheet.cell(i, 2) == prefix and item_sheet.cell(i, 3) == affix:
            position_array.append(i)

    for j in len(position_array):
        if roll <= item_sheet.cell(position_array[j], 4).value:
            item_name = item_sheet.cell(position_array[j], 5).value

    # chart = BarChart()
    # chart.add_data(values)
    # history_sheet.add_chart(chart, 'd4')
    # wb.save(workbook_file_name)

    return item_name
