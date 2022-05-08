import xlwings as xw
from openpyxl import load_workbook

wb2 = load_workbook('file_name') #use openpyxl load file
ws2 = wb2.active
old_comment = str(ws2['A1'].comment) #read A1 comment text
new_comment = old_comment + '\n new row text' #edit comment,add new row

wb = xw.Book('file_name') # use xlwings load file
ws1 = wb.sheets[0]
ws1.range('A1').api.NoteText(new_comment)# renew A1 comment

wb.save('new_file_name') #save new file
wb.close()