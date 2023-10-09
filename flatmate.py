from fpdf import FPDF
import webbrowser
import os
class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weigh = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        to_pay = bill.amount * weigh
        return to_pay

class PdfReport:
    """
    Create a PDF file that contains data about the flatmates such as their name, amount due and period of the bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flamates Bill", border=1, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate2),2)), border=1, ln=1)# Insert name and due amount of the first flatmate

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill, flatmate1),2)), border=1, ln=1)


        pdf.output(self.filename)

        webbrowser.open('file://' + os.path.realpath(self.filename))

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