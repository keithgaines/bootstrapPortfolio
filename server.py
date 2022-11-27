from flask import Flask, render_template, FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
import requests

class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")


app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    form = ContactForm()
    if requests.method == 'POST':
        return 'Form posted.'
    elif requests.method == 'GET':
        return render_template('contact.html,' form=form)


@app.route('/pythonPortfolio.html')
def python():
    return render_template('pythonPortfolio.html')

@app.route('/webPortfolio.html')
def web():
    return render_template('webPortfolio.html')

if __name__ == "__main__":
    app.run(debug=True)
