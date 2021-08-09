from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

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
        if proteins + veggies + dairy > 0:
            if proteins > 1:
                proteinList = pd.read_csv("proteins.csv")
                i=0
                for i in range (0..proteins):
                    
        return render_template('your-taco.html', no_proteins=proteins, no_veggies=veggies, no_dairy_items=dairy)
    else:
        return redirect(url_for('home'))
