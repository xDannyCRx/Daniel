from mechanize import Browser
import csv
with open('name.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for rows in csvfile:
        browser = Browser()
        browser.open("https://www.tse.go.cr/consulta_persona/consulta_cedula.aspx")
        form = browser.select_form("form1")
        browser["txtcedula"] = rows
        response = browser.submit()
        name = str(rows)
        file = open("'"+name+".html''","w")
        file.write(response.read().decode("UTF-8"))
        file.close()