##import openpyxl
##wb = openpyxl.load_workbook('example.xlsx')
##print(type(wb))
##
##print(wb.get_sheet_names())
##sheet = wb.get_sheet_by_name('Fruits')
##print(sheet)
##print(type(sheet))
##print(sheet.title)
##
##anotherSheet = wb.get_active_sheet()
##print(anotherSheet)

import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Fruits')
print(sheet['A1'])
print(sheet['A1'].value)
a=sheet['A1']
print(sheet['B1'].value)
print(sheet['C1'].value)

print('Date and time:'+ str(a.value) +
      'present in row' + str(a.row) + ' and column' + str(a.column))
