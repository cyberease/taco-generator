from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-taco', methods=['GET', 'POST'])
def your_taco():
    if request.method == 'POST':
        data = request.form
        proteins = data['proteins']
        veggies = data['veggies']
        dairy = data['dairy']
        return render_template('your-taco.html', no_proteins=proteins, no_veggies=veggies, no_dairy_items=dairy)
    else:
        return redirect(url_for('home'))
