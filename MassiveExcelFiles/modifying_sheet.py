import openpyxl as op


wb = op.load_workbook("sample_sheet.xlsx")
sheet = wb.active
sheet.title = "modified_Sheet"
print(sheet.title)
wb.save("sample_sheet_copy.xlsx")

