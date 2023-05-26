import xlsxwriter
from main import array

def writer(parametr):
    book = xlsxwriter.Workbook(r"C:\Users\ymnuc\Desktop\bambytoys.xlsx")
    page = book.add_worksheet("bambytoys_gaga")

    row = 1
    column = 0

    #задаем название колонок
    page.write(0, 0, "N")
    page.write(0, 1, "Name")
    page.write(0, 2, "Price")
    page.write(0, 3, "Volume")
    page.write(0, 4, "Picture")

    # устанавливает ширину колонки
    page.set_column("A:A", 10)
    page.set_column("B:B", 50)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)
    page.set_column("E:E", 50)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column +4, item[4])
        row +=1
    book.close()


writer(array)
