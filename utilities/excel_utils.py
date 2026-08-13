import openpyxl

def get_data_from_excel(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    total_rows = sheet.max_row
    total_cols = sheet.max_column
    
    data_list = []
    
    # Header row వదిలేసి, 2nd row నుండి డేటా తీసుకుంటాం
    for r in range(2, total_rows + 1):
        row_data = []
        for c in range(1, total_cols + 1):
            row_data.append(sheet.cell(row=r, column=c).value)
        data_list.append(tuple(row_data))
        
    return data_list