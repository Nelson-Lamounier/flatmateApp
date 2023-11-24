
from flatmates_bill.flatmate import Flatmate, Bill
from flatmates_bill.reports import PdfReport
from fpdf import FPDF

amount = int(input("What is the amount: "))
period = input("What is the period: E.g December 2023: ")
user1 = input("What is the names:")
days1 = int(input(f"How many days in the house {user1}:"))
user2 = input("what is the name:")
days2 = int(input(f"How many days in the house {user2}:"))
the_bill = Bill(amount=amount, period="April 2023")
user_1 = Flatmate(name=user1, days_in_house=days1)
user_2 = Flatmate(name=user2, days_in_house=days2)

print(f"{user1} total bill: ", user_1.pays(bill=the_bill, flatmate=user_2))
print(f"{user2} total bill:", user_2.pays(bill=the_bill, flatmate=user_1))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=user_1, flatmate2=user_2, bill=the_bill)