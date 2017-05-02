# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:37:02 2017

@author: irene_qwewxh7
"""

import pandas as pd
from polls.models import Aliment

location= r'C:\Users\irene_qwewxh7\Documents\Stage\objectif_200.csv'
conso=pd.read_csv(location,encoding = "ISO-8859-1",sep=';')


index=pd.MultiIndex.from_arrays

def remplissage_base(conso):
    for i in range(len(conso)) :
        nom=conso.ORIGFDNM[i]
        groupe=str(conso.ORIGGPCD[i])
        description='/'
        aliment=Aliment(nom_aliment=nom,description=description,groupe=groupe)
        aliment.save()