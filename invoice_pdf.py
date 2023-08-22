import os
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice


# Choosing English as the document language
os.environ["INVOICE_LANG"] = "en"
client = Client('CompanyClient')
provider = Provider('TestProvider', bank_account='123-456-789', bank_code='2023')

creator = Creator('Test User')

invoice = Invoice(client, provider, creator)

invoice.add_item(Item(26, 250, description="Test1"))
invoice.add_item(Item(14, 450, description="Test2"))
invoice.add_item(Item(10, 300, description="Test3"))
invoice.add_item(Item(5, 350, description="Test4"))

invoice.currency = "EUR"
invoice.number = "10393069"

docu = SimpleInvoice(invoice)
docu.gen('invoice_test2.pdf', generate_qr_code=True)  # We can put QR code by setting the #qr_code parameter to 'True'
# docu.gen('invoice_test2.xml')  # docu.gen("invoice_test3.xml") # We can also generate an XML file of this invoice


os.environ["INVOICE_LANG"] = "pl"

client = Client('Mon Wis')
provider = Provider('CoffeeLover', bank_account='7011600000000217458623', bank_code='2023')

creator = Creator('CoffeeLover Member')
invoice = Invoice(client, provider, creator)

invoice.add_item(Item(5, 925.00, description="Acaia New Pearl Black- Waga- Pitch Black"))
invoice.add_item(Item(10, 49.90, description="Acaia Pearl Protective Film- Folia Zabezpieczająca- 6 sztuk"))
invoice.add_item(Item(10, 719.99, description="Fellow Stagg EKG- Czajnik Elektryczny- Czarny Mat"))
invoice.add_item(Item(15, 86.99, description="Motta- gumowa mata tampingowa"))
invoice.add_item(Item(30, 159.00, description="Motta- Dzbanek do mleka- czarny- 500ml"))
invoice.add_item(Item(3, 1529.00, description="Comandante- Młynek C40 MK4 Nitro Liquid Amber"))

invoice.currency = "PLN"
invoice.number = "2023-08-177631"

docu = SimpleInvoice(invoice)
docu.gen('invoice_test3.pdf', generate_qr_code=True)
# docu.gen('invoice_test3.xml')


import easygui
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


# Data which we are going to be displayed in a tabular format:
tableData = [
    ["Date", "Description", "Units", "Price (EUR)"],

    ["01/07/2023", "Acaia New Pearl Black Scale- Pitch Black", "20", "250.00"],

    ["01/07/2023", "Acaia Pearl Protective Film", "15", "10.00"],

    ["01/08/2023", "Fellow Stagg EKG Kettle- Matt Black", "35", "289.00"],

    ["01/08/2023", "Comandante C40 MK4 Coffee Grinder- Nitro Liquid Amber", "10", "249.00"],

    ["Signature", "", "", "_________________"],

]

# Creating a Document structure with A4 size page
output_path = easygui.filesavebox(title='Save file to: ',
                                  default='D:\\python\\pycharm pro\\pycharm projects\\'
                                          + 'test-invoice1' + '.pdf',
                                  filetypes="*.pdf")
docu = SimpleDocTemplate(output_path, pagesize=A4)
# docu = SimpleDocTemplate("test_invoice.pdf", pagesize=A4)

styles = getSampleStyleSheet()

doc_style = styles["Heading1"]
doc_style.alignment = 1

title = Paragraph("TEST INVOICE", doc_style)

style = TableStyle([
    ("BOX", (0, 0), (-1, -1), 1, colors.black),
    ("GRID", (0, 0), (4, 4), 1, colors.dimgray),
    ("BACKGROUND", (0, 0), (3, 0), colors.dimgray),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
])

# Creates a table object using the Table() to pass the table data and the style object
table = Table(tableData, style=style)

# We have to build the actual pdf merging all objects together
docu.build([title, table])

exit()
