import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\최희준\\Desktop\\test.xlsx')
ws = wb.Activesheet
ws2 = excel.Worksheets.Add()
ws2 = wb.worksheet('Sheet2')
ws2.name = "shit"
ws.Range('A2:B3').Value = "PER"
ws.Range('A4:B5,A7:B8').Value = "PBR"
ws.Range('A7:B8').Interior.ColorIndex = 10
print(ws.Cells(1,1).Value)
excel.Quit()