from openpyxl import load_workbook
import pandas as pd

def get_df_by_range(excel_file: str
        , excel_sheet: str, excel_range: str
        , excel_header: str) -> pd.DataFrame:
    workbook = load_workbook(excel_file)
    sheet = workbook[excel_sheet]
    #workbook = load_workbook('db\\jee-mains.xlsx')
    #sheet = workbook['jee-mains']

    # Specify range (e.g., A1:C10)
    data = sheet[excel_range] #Range by Single Row
    #data = sheet['A1:C10'] #Range by Row, Column
    #data = sheet['A1:C1'] #Range by Single Row
    #data = sheet['A1:A10'] #Range by Single Column
    rows = [[cell.value for cell in row] for row in data]
    columns = [cell.value for cell in sheet[excel_header][0]]
    #columns = [cell.value for cell in sheet['A1:C1'][0]] #Header by multi column
    #columns = [cell.value for cell in sheet['A1:A1'][0]] #Header by single column
    df = pd.DataFrame(rows, columns=columns)
    return df
'''Example Usage
excel_file = 'db\\jee-mains.xlsx'
excel_sheet = 'jee-mains'
excel_range = 'A2:H10'  # Example range
excel_header = 'A1:H1'  # Example header range
print(get_df_by_range(excel_file, excel_sheet
        , excel_range, excel_header))
'''