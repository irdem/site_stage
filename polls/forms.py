# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:59:34 2017

@author: irene_qwewxh7
"""

from django import forms
from django.contrib.auth.models import User
import floppyforms
from suit.widgets import SuitTimeWidget



  

class Slider(floppyforms.RangeInput):
    min = 0
    max = 100
    step = 1
    template_name = 'polls/slider.html'
    

    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }

    
class etat_nutri_form(floppyforms.Form):
    faim=floppyforms.IntegerField(widget=Slider, label = "Avez-vous faim ? ")
    def clean_faim(self):
        faim = self.cleaned_data['faim']
        if not 0 <= faim <= 100:
            raise forms.ValidationError("Enter a value between 0 and  100")

        return faim
    
    soif=floppyforms.IntegerField(widget=Slider, label = "Avez-vous soif ? ")
    def clean_soif(self):
        soif = self.cleaned_data['soif']
        if not 0 <= soif <= 100:
            raise forms.ValidationError("Enter a value between 0 and  100")

        return soif
    
    sensation_estomac= floppyforms.IntegerField(widget=Slider, label = "Avez-vous la sensation d'avoir l'estomac rempli ? ")
    plaisir_manger =floppyforms.IntegerField(widget=Slider, label = "Eprouveriez du plaisir à manger maintenant ? ")
    plaisir_boire =floppyforms.IntegerField(widget=Slider, label = "Eprouveriez du plaisir à boire maintenant ? ")
    quantite_manger =floppyforms.IntegerField(widget=Slider, label = "Quelle quantité seriez-vous capable de manger en ce moment ? ")
    quantite_boire =floppyforms.IntegerField(widget=Slider, label = "Quelle quantité seriez-vous capable de boire en ce moment ? ")

    choix=[("00:15","00:15"),("00:30","00:30"),("00:45","00:45"),("01:00","01:00"),("01:30","01:30"),
           ("02:00","02:30"),("03:00","03:00"),("03:30","03:30"),("04:00","04:00"),("04:30","04:30"),
           ("05:00","05:00"),("06:00","06:00"),("07:00","07:00"),("08:00","08:00"),("09:00","09:00"),
           ("10:00","10:00"),("11:00","11:00"),("12:00","12:00")]
    heure_dernier_repas =floppyforms.ChoiceField(choices=choix,label="A combien de temps remonte votre dernier repas (hors snack)-format hh:mm ?")
    heure_derniere_prise =floppyforms.ChoiceField(choices=choix,label="A combien de temps remonte votre dernière prise alimentaire (snack compris)-format hh:mm?")
    
    Choices = [("petit-dej","petit-dejeuner"),("dej","déjeuner"),("snack","goûter/snack/collation"),("diner","diner")]
    prochain_repas = floppyforms.ChoiceField(widget= floppyforms.RadioSelect(), choices=Choices, label = "Quel est le prochain repas que vous pensez prendre ?")
    

class inscription_form(forms.Form):
    Pseudo = forms.CharField(max_length=100)
    Mdp = forms.CharField(max_length=32,min_length=6,label="Mot de passe",widget=forms.PasswordInput)
    mdp2= forms.CharField(max_length=32,min_length=6,label="Repetez le mot de passe",widget=forms.PasswordInput)
    Email = forms.EmailField(label="Votre adresse mail")
    
    Code_postal =forms.CharField(max_length=5)
    
    Choices=[("1","Sans diplôme"),("2","Brevet des collèges"),("3","CAP,BEP"),
             ("4","Bac (général, technologique ou professionnel)")
             ,("5","Bac +2 (BTS ou autre )"),("6","Bac +3/4 (license, maitrise)")
               ,("6", "Bac +5 (Master,diplome d'ingénieur,  école de commerce)")
               ,("7", "Bac +8")
             ]
    Niveau_etudes = forms.ChoiceField(choices=Choices,widget=forms.RadioSelect(),
                                      label= "Quel est votre plus haut diplôme obtenu ?")

    Choices = [("F",'Femme'),("H",'Homme')]
    Sexe = forms.ChoiceField (choices=Choices, widget= forms.RadioSelect())
    Age = forms.IntegerField(min_value=1, max_value=120)
    Poids = forms.IntegerField(min_value=0,max_value=200)
    Taille_metre = forms.DecimalField(label='Taille en mètre',min_value=0, max_value=2.30,max_digits=3)
    Nb_enfants = forms.IntegerField(label="Combien d'enfants avez-vous ?",min_value=0)
    Choices = [("Faible","Moins d'une heure par semaine "),( "Moyenne","Une à trois heures par semaine"),
                ("Forte","Plus de quatre heures par semaine")]
    Sport = forms.ChoiceField(choices =Choices, widget=forms.RadioSelect(),
                              label= "Quelle est votre durée de pratique sportive par semaine ?")

    Choix = [("vegan","Végan"),
             ("végétarien","Végétarien"),
             ('lact_free','Sans lactose'),
             ('glut_free','Sans gluten'),
             ('porc_free','Sans porc'),("Aucun","Aucun de ceux là")]
    Regime_particulier =forms.MultipleChoiceField(required=False,
                                                  widget=forms.CheckboxSelectMultiple,
                                                  choices=Choix, label= "Suivez-vous l'un ou plusieurs de ces régimes ?")
    
    choix = [("perte","perdre du poids"),("maintien","ne pas prendre de poids"),
               ("med"," des raisons médicales autres que la perte de poids"),("aucun","je ne suis pas de régime")]
    Regime_raison = forms.ChoiceField (widget=forms.RadioSelect()
    , choices=choix
    ,label="Suivez-vous un régime pour :")
    
    
    choix = [('reg','Régulier (vous fumez au moins une cigarette (ou autre) par jour)'),('occ',"Occasionnel (vous fumez moins d' une cigarette (ou autre) par jour)")
    ,('ancien',"j'ai arrêté de fumer"),
    ('nf','je ne fume pas')]
    Fumeur = forms.ChoiceField (widget=forms.RadioSelect()
    , choices=choix
    ,label="Etes-vous fumeur :")
    
    choix = [("quotidien","au moins 4 fois par semaine"),("hebdo","2 à 3 fois par semaine")
    ,("mensuel","2 à 4 fois par mois"),("rare","1 fois par mois ou moins"),("jamais","jamais")]
    alcool =forms.ChoiceField(widget=forms.RadioSelect()
    , choices=choix
    ,label='A quelle fréquence vous arrive-t-il de consommer des boissons alcoolisées ( vin, bière, cidre ou autre alcool) ?')
    
    reglement= forms.BooleanField(label="Je reconnais avoir pris connaissance du règlement et l'accepte ", required=True)
    
    def clean_Pseudo(self):
        Pseudo=self.cleaned_data['Pseudo']
        if Pseudo in [x.username for x in User.objects.all()]:
            raise forms.ValidationError("Cet identifiant est déjà utilisé")
        return Pseudo

    def clean_Email(self):
        Email=self.cleaned_data['Email']
        if Email in [x.email for x in User.objects.all()]:
            raise forms.ValidationError("Cet email est déjà enregistré...")
        return Email
        
    def clean_Age(self):
        Age=self.cleaned_data['Age']
        if Age<=0:
            raise forms.ValidationError("Merci d'entrer un nombre positif")
        return Age
    
    def clean_Poids(self):
        Poids=self.cleaned_data['Poids']
        if Poids<=0:
            raise forms.ValidationError("Merci d'entrer un nombre positif")
        return Poids
    
    def clean_Code_postal(self):
        Code_postal=self.cleaned_data['Code_postal']
        if len(Code_postal)<5 :
            raise forms.ValidationError("le code postal doit faire 5 chiffres")
        try :
            int(Code_postal)
        except :
            raise forms.ValidationError("le code postal doit faire 5 chiffres")
        
        return Code_postal 

    def clean_Nb_enfants(self):
        Nb_enfants=self.cleaned_data['Nb_enfants']
        if Nb_enfants<0 :
            raise forms.ValidationError("Merci d'entrer un nombre positif ou nul ")
        return Nb_enfants
    
    def clean(self):
        cleaned_data=super(inscription_form,self).clean()
        
        Mdp=self.cleaned_data.get('Mdp')
        mdp2=self.cleaned_data.get('mdp2')
        if Mdp != mdp2:
            raise forms.ValidationError("Les deux mots de passe entrés sont différents")
        return cleaned_data
    
    
class ConnexionForm(forms.Form):

    username = forms.CharField(label="Nom d'utilisateur", max_length=30)

    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
class test_aliment_form(forms.Form):
    
    def __init__(self,choix,*args,**kwargs):
        super(test_aliment_form,self).__init__(*args,**kwargs)
        self.fields['choix_alim']=forms.ChoiceField(widget=forms.RadioSelect(), choices=choix,label="Choisissez l'aliment que vous souhaitez manger")
        

class questions_sup(forms.Form):
    enceinte=forms.BooleanField(label="Etes-vous enceinte ?",required=False)
    allaite=forms.BooleanField(label="Allaitez-vous actuellement ?",required=False)


    
