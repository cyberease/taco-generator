#from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import random


wDir = '/home/knelson/Documents/Projects/cyberease/taco/'
os.chdir(wDir)
def your_taco(dfIn, proteins, veggies, dairy):
    if dfIn.size == 0:
        dfIngredient = pd.DataFrame(['temp'])
    else:
        dfIngredient = dfIn
    dfIngredient.columns = ['ingredient']
    dfIngredient = dfIngredient[dfIngredient.ingredient != 'temp']
    ingSum = proteins + veggies + dairy
    if ingSum > 0:
        if proteins > 0:
            proteinList = pd.DataFrame(pd.read_csv("proteins.csv"))
            proteinList.columns = ['ingredient']
            pSize = int(proteinList.size)
            i=1
            while i <= proteins:
                rnd = random.randrange(pSize) - 1
                dfIngredient.loc[len(dfIngredient)] = [proteinList.iloc[rnd]['ingredient']]
                proteinList = proteinList[proteinList.ingredient != proteinList.iloc[rnd]['ingredient']]
                proteinList.reset_index(inplace=True)
                i = i + 1  
        if veggies > 0:
            veggieList = pd.DataFrame(pd.read_csv("veggies.csv"))
            veggieList.columns = ['ingredient']
            pSize = int(veggieList.size)
            i=1
            while i <= veggies:
                rnd = random.randrange(pSize) - 1
                dfIngredient.loc[len(dfIngredient)] = [veggieList.iloc[rnd]['ingredient']]
                veggieList = veggieList[veggieList.ingredient != veggieList.iloc[rnd]['ingredient']]
                veggieList.reset_index(inplace=True)
                i = i + 1  
        if dairy > 0:
            dairyList = pd.DataFrame(pd.read_csv("dairy.csv"))
            dairyList.columns = ['ingredient']
            pSize = int(dairyList.size)
            i=1
            while i <= dairy:
                rnd = random.randrange(pSize) - 1
                dfIngredient.loc[len(dfIngredient)] = [dairyList.iloc[rnd]['ingredient']]
                dairyList = dairyList[dairyList.ingredient != dairyList.iloc[rnd]['ingredient']]
                dairyList.reset_index(inplace=True)
                i = i + 1  
    return dfIngredient         
df = pd.DataFrame()
df = your_taco(df,2,2,1)
print(df)

