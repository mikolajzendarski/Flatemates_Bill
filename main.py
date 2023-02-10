from Flat import Bill, Flatmate
from PDFbody import PdfReport

amount = int(input("Enter the bill amount: "))
month_year = str(input("Enter month and year: "))

firstmate = str(input("Enter name of first flatmate: "))
firstmate_days = int(input("Enter amount of days spent in home for first flatmate: "))

secondmate = str(input("Enter name of second flatmate: "))
secondmate_days = int(input("Enter amount of days spent in home for second flatmate: "))

the_bill = Bill(amount, month_year)
john = Flatmate(firstmate, firstmate_days)
marry = Flatmate(secondmate, secondmate_days)

print("John pays: ", john.pays(the_bill, flatmate2=marry))
print("Marry pays: ", marry.pays(the_bill, flatmate2=john))

pdf_report = PdfReport(filename=f"{month_year}.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)

