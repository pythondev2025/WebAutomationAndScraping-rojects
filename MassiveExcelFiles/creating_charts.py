import openpyxl as op
from openpyxl import chart


# loading workbook
wb = op.load_workbook("sample_graph_data.xlsx")
sheet = wb["Sheet1"]

# creating ref object
ref_obj = chart.Reference(sheet, min_col=1, min_row=1, max_row=13, max_col=2)

# creating series object from ref_obj
# ser_obj = chart.Series(ref_obj)
# after checking we gotta know Series has been removed

# creating and adding values into chart object
b_chart = chart.BarChart()
b_chart.title = "Annual Sales"
b_chart.add_data(ref_obj)

# adding chart to the sheet
sheet.add_chart(b_chart, "D15")

# saving sheet
wb.save("sample_graph_data.xlsx")

