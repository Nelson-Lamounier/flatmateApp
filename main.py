from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flatmate

app = Flask(__name__)

class HomePage(MethodView): # Inherit from flask class(open source)
  
  def get(self):
    return render_template('index.html')

class BillFormPage(MethodView):
  
  def get(self):
    bill_form = BillForm()
    return render_template('form_page.html', billform=bill_form)

class ResultsPage(MethodView):
  
  def post(self):
    """Gather the data from the widget"""
    billform = BillForm(request.form)
    amount = billform.amount.data #Variable equal the widget of the form - data is a property of the user inputted that return it
    period = billform.period.data

    """         
    name1 = billform.name1.data
    days_in_house10 = billform.days_in_house1

    name2 = billform.name2.data
    days_in_house20 = billform.days_in_house2         
    
    """
 

    the_bill = flatmate.Bill(float(amount), period)
    flatmate1 = flatmate.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
    flatmate2 = flatmate.Flatmate(billform.name2.data, float(billform.days_in_house2.data))

    """Returns the amount to be paid - The calculation happens while return the values"""

    return render_template('results.html', 
                            name1=flatmate1.name, 
                            amount1=flatmate1.pays(the_bill, flatmate2), 
                            name2=flatmate2.name, 
                            amount2=flatmate2.pays(the_bill, flatmate1))

class BillForm(Form): # Inherit from wfform class(open source)
  amount = StringField("Amount: ", default= "100")
  period = StringField("Period: ", default= "September 2023")

  name1 = StringField("Name: ", default= "John")
  days_in_house1 = StringField("How many days: ", default= 20)

  name2 = StringField("Name: ", default= "Marry")
  days_in_house2 = StringField("How many days: ", default= 12)

  button = SubmitField("Calculate")

  """Calling the class HomePage/BillFormPage/ResultsPage"""

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug= True)

