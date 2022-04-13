from pathlib import Path
import openpyxl as xl


workbook_file_name = 'ItemLists.xlsx'
save_file_name = 'test1.xlsx'

# TODO workbook_file_path = ''


def process_workbook(wondrous_sheet_name, roll, prefix, affix, item_type):
    wb = xl.load_workbook(workbook_file_name)
    item_sheet = wb[wondrous_sheet_name]
    position_array = []
    item_name = "None"
    print("process values for generator: " + str(roll) + ' ' + prefix + affix + item_type)  # debugging

    # find positions of acceptable items in spreadsheet
    for i in range(item_sheet.max_row):
        i_loc = i+1  # excel starts at 1 not 0

        if item_sheet.cell(i_loc, 1).value == item_type:
            if item_sheet.cell(i_loc, 2).value == prefix:
                if item_sheet.cell(i_loc, 3).value == affix:
                    position_array.append(i_loc)
    print(position_array)
    last_max_threshold = 0
    for j in range(len(position_array)):
        if last_max_threshold < roll <= item_sheet.cell(position_array[j], 4).value:
            item_name = item_sheet.cell(position_array[j], 5).value
        last_max_threshold = item_sheet.cell(position_array[j], 4).value
    print(item_name)

    return item_name
