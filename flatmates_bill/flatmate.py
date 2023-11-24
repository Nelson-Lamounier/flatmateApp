from fpdf import FPDF
import webbrowser
import os
from flatmates_bill.reports import PdfReport

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