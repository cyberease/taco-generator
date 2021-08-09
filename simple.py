#from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import random


wDir = '/home/knelson/Documents/Projects/cyberease/taco/'
os.chdir(wDir)
def your_taco():
    proteins = int(1)
    veggies = 2
    dairy = 1
    ingSum = proteins + veggies + dairy
    if ingSum > 0:
        if proteins > 0:
            proteinList = pd.read_csv("proteins.csv")
            pSize = int(proteinList.size)
            i=0
            for i in range(0..proteins):
                rnd = random.randrange(pSize)
                print(rnd)
                print(proteinList.loc[rnd])
                i = i + 1            
your_taco()
