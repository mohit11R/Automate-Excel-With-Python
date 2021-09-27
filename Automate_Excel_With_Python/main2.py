from openpyxl import Workbook, load_workbook

# Creating Workbook objects
wb = Workbook()
ws = wb.active

ws.title = 'Data'


# Adding values in sheet
ws.append(['CPP','Python','Data Science','Web Dev'])
ws.append(['CPP','Python','Data Science','Web Dev'])
ws.append(['CPP','Python','Data Science','Web Dev'])
ws.append(['CPP','Python','Data Science','Web Dev'])
ws.append(['End','Is','Here'])
wb.save('testing.xlsx')

 