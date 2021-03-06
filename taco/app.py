from flask import Flask, render_template, request, redirect, url_for, redirect
import pandas as pd
import os
import random
#appPath = '/home/knelson/Documents/Projects/cyberease/taco/'
appPath = os.getcwd()
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
        if int(proteins) + int(veggies) + int(dairy) > 0:
            df = pd.DataFrame()
            df = getIngredients(df, int(proteins), int(veggies), int(dairy))
            return render_template('your-taco.html', no_proteins=proteins, no_veggies=veggies, no_dairy_items=dairy, tables=[df.to_html(classes='data')], titles=df.columns.values)
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))
def getIngredients(dfIn, proteins, veggies, dairy):
    if dfIn.size == 0:
        dfIngredient = pd.DataFrame(['temp'])
    else:
        dfIngredient = dfIn
    dfIngredient.columns = ['ingredient']
    dfIngredient = dfIngredient[dfIngredient.ingredient != 'temp']
    ingSum = proteins + veggies + dairy
    if ingSum > 0:
        if proteins > 0:
            #proteinList = pd.DataFrame(pd.read_csv("proteins.csv"))
            data = [['ingredient'],
                ['carne guisada'],
                ['scrambled eggs'],
                ['bacon'],
                ['ham'],
                ['Spam'],
                ['chicharrones'],
                ['tripas'],
                ['mollejas'],
                ['sausage'],
                ['chorizo'],
                ['carne asada'],
                ['fajitas'],
                ['fried eggs']]
            proteinList = pd.DataFrame(data)
            proteinList.columns = ['ingredient']
            pSize = int(proteinList.size)
            i=1
            while i <= proteins:
                rnd = random.randrange(pSize) - 1
                dfIngredient.loc[len(dfIngredient)] = [proteinList.iloc[rnd]['ingredient']]
                #proteinList = proteinList[proteinList.ingredient != proteinList.iloc[rnd]['ingredient']]
                #proteinList.reset_index()
                i = i + 1  
        if veggies > 0:
            #veggieList = pd.DataFrame(pd.read_csv("veggies.csv"))
            data = [['potatoes'],
                ['nopalitos'],
                ['fresh onions'],
                ['grilled onions'],
                ['fresh tomatoes'],
                ['pico de gallo'],
                ['fresh jalapenos'],
                ['grilled jalapeno'],
                ['cilantro']]
            veggieList = pd.DataFrame(data)
            veggieList.columns = ['ingredient']
            pSize = int(veggieList.size)
            i=1
            while i <= veggies:
                rnd = random.randrange(pSize) - 1
                m=dfIngredient.isin([veggieList.iloc[rnd]['ingredient']]).any()
                m=m.index[m].tolist()
                print(len(m))
                if len(m) == 0:
                    dfIngredient.loc[len(dfIngredient)] = [veggieList.iloc[rnd]['ingredient']]
                    i = i + 1 
                else:
                    i = i 
        if dairy > 0:
            #dairyList = pd.DataFrame(pd.read_csv("dairy.csv"))
            data = [['cheddar cheese'],
                ['monterrey jack cheese'],
                ['sour cream']]
            dairyList = pd.DataFrame(data)
            dairyList.columns = ['ingredient']
            pSize = int(dairyList.size)
            i=1
            while i <= dairy:
                rnd = random.randrange(pSize) - 1
                m=dfIngredient.isin([dairyList.iloc[rnd]['ingredient']]).any()
                m=m.index[m].tolist()
                print(len(m))
                if len(m) == 0:
                    dfIngredient.loc[len(dfIngredient)] = [dairyList.iloc[rnd]['ingredient']]
                    i = i + 1 
                else:
                    i = i   
        return dfIngredient
    else:
        return redirect(url_for('home'))

            
