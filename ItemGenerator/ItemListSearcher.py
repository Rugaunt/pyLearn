from pathlib import Path
import openpyxl as xl


workbook_file_name = 'ItemLists.xlsx'
save_file_name = 'test1.xlsx'
# wondrous_sheet_name = 'WondrousItems'
# TODO workbook_file_path = ''


def process_workbook(wondrous_sheet_name, roll, prefix, affix):
    wb = xl.load_workbook(workbook_file_name)
    item_sheet = wb[wondrous_sheet_name]


    history_sheet = wb['Tester']
    print('losing 5 hitpoints!')
    change_hitpoints(-5, char_sheet, wb, history_sheet)
    values = Reference(history_sheet,
                       min_row=2,
                       max_row=history_sheet.max_row,
                       min_col=3,
                       max_col=3
                       )

    # chart = BarChart()
    chart.add_data(values)
    history_sheet.add_chart(chart, 'd4')
    wb.save(workbook_file_name)