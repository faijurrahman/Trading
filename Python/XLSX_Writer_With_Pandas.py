import pandas as pd
import xlsxwriter as xw

#Source: https://xlsxwriter.readthedocs.io/working_with_pandas.html

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45], 'Percentage': [10, 20, 30, 20, 15, 30, 45]})

# Get the dimensions of the dataframe.
(max_row, max_col) = df.shape

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter objects from the dataframe writer object.
# This is equivalent to the following code when using XlsxWriter on its own:
# workbook  = xlsxwriter.Workbook('filename.xlsx')
# worksheet = workbook.add_worksheet()
workbook  = writer.book
worksheet = writer.sheets['Sheet1']




# Apply a conditional format to the required cell range.
# Source: https://xlsxwriter.readthedocs.io/working_with_conditional_formats.html
worksheet.conditional_format(1, max_col, max_row, max_col,
                             {'type': '3_color_scale'})




# Writing Formulas
# Source: https://xlsxwriter.readthedocs.io/working_with_formulas.html
worksheet.write_formula('B10', '=sum(B2:B8)')





# Add some cell formats.
# Source: https://xlsxwriter.readthedocs.io/format.html
cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
worksheet.write('E3', 'Format Test Cell', cell_format)
format1 = workbook.add_format({'num_format': '#,##0.00'})
format2 = workbook.add_format({'num_format': '0%'})
# Set the column width and format.
worksheet.set_column(1, 1, 18, format1)
# Set the format but not the column width.
worksheet.set_column(2, 2, None, format2)





# Add a header format.
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'center',
    'fg_color': '#D7E4BC',
    'border': 2})
# Write the column headers with the defined format.
for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num + 1, value, header_format)




# Data Validation
# Source: https://xlsxwriter.readthedocs.io/working_with_data_validation.html
worksheet.data_validation('E6', {'validate': 'integer',
                                  'criteria': 'between',
                                  'minimum': 1,
                                  'maximum': 100,
                                  'input_title': 'Enter an integer:',
                                  'input_message': 'between 1 and 100'})





# Create a chart object.
chart = workbook.add_chart({'type': 'column'})
# Configure the series of the chart from the dataframe data.
chart.add_series({'values': ['Sheet1', 1, 1, max_row, 1]})
# Insert the chart into the worksheet.
worksheet.insert_chart(12, 3, chart)




# Close the Pandas Excel writer and output the Excel file.
#writer.save()
writer.close()