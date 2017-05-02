from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.shortcuts import redirect
from django.template import loader
from .forms import inscription_form, ConnexionForm,etat_nutri_form, test_aliment_form, questions_sup,commentaire
from .models import Utilisateurs, Test, Aliment, Preference, Commentaire
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django import forms
from django.utils import timezone



class choix_alea () :
    def __init__(self):
        self.choix=[]

        
    def rempli(self):
        self.choix=[]
        for i in range(18):
            self.choix.append(Aliment.select_choix(Aliment))
        self.choix.append(self.choix[1])
        self.choix.append(self.choix[0])
    
    def set_test(self,id_test):
        self.test=id_test;
            
            
            
            
liste_choix=choix_alea()


def index(request):
    return render(request,'polls/accueil.html')

def accueil(request):
    return render(request,'polls/accueil.html')

def question_supp(request):
    form = questions_sup(request.POST or None)
    
    if form.is_valid():
        enceinte=form.cleaned_data['enceinte']
        allaite=form.cleaned_data['allaite']
        
        if request.user.is_authenticated():
            user=Utilisateurs.objects.get(Nom_utilisateur__username__exact=request.user.username)
            user.enceinte=enceinte
            user.allaite=allaite
            user.save()
            send=True
            
    return render(request,'polls/question_sup.html',locals())

            

def inscription(request):
    Reponse=''
    form =inscription_form(request.POST or None)

    if form.is_valid():
        pseudo=form.cleaned_data['Pseudo']
        age=form.cleaned_data['Age']
        Mdp = form.cleaned_data['Mdp']
        Email = form.cleaned_data['Email']
        Age = form.cleaned_data['Age']
        Poids = form.cleaned_data['Poids']
        Taille_centimetre = form.cleaned_data['Taille_centimetre']
        Code_postal=form.cleaned_data['Code_postal']
        Sexe=form.cleaned_data['Sexe']
        Nb_enfants=form.cleaned_data['Nb_enfants']
        Sport=form.cleaned_data['Sport']
        Niveau_etudes=form.cleaned_data['Niveau_etudes']
        Regime_raison=form.cleaned_data['Regime_raison']
        Fumeur=form.cleaned_data['Fumeur']
        alcool=form.cleaned_data['alcool']
        Regime_part = form.cleaned_data['Regime_particulier']
        vegan=False
        veg=False
        lact=False
        glut=False
        porc=False
        if "vegan" in Regime_part :
            vegan=True
        if "végétarien" in Regime_part :
            veg = True
        if "lact_free" in Regime_part :
            lact=True
        if "glut_free" in Regime_part :
            glut=True
        if "porc_free" in Regime_part :
            porc =True
        user=User.objects.create_user(pseudo,Email,Mdp)
        
        Utilisateurs.objects.create(Nom_utilisateur=user
            ,Age=Age,Poids=Poids,Taille_centimetre=Taille_centimetre,Sport=Sport,
            Regime_raison=Regime_raison,Sexe=Sexe, Nb_enfants=Nb_enfants,
            Fumeur=Fumeur,Consommation_alcool=alcool
            ,Niveau_etudes=Niveau_etudes,Code_postal=Code_postal,
            Vegetarien = veg, Vegan=veg, Sans_lactose=lact, Sans_gluten= lact,
            Sans_porc= porc)
        login(request,user)
        send=True
        
        if Sexe=='F':
            Reponse = redirect(question_supp)
        else :
            Reponse =render(request,'polls/inscription.html',locals())
    if Reponse=='':
        Reponse =render(request,'polls/inscription.html',locals())
        
    return Reponse

def etat_nutri(request):
    time=timezone.now()
    if request.user.is_authenticated():
        user=Utilisateurs.objects.filter(Nom_utilisateur__username__exact=request.user.username)[0]
        user_name=user.Nom_utilisateur.username
    try :
        dernier=Test.objects.filter(id_utilisateur__Nom_utilisateur__username__exact=user_name)
        dernier_test=dernier[len(dernier)-1].date_test
        diff=time-dernier_test
        if diff.seconds<14400 and diff.days<1:
            duree=False
        else:
            duree =True   
    except :
        duree=True
    form=etat_nutri_form(request.POST or None)
    if form.is_valid():
        faim = form.cleaned_data['faim']
        soif = form.cleaned_data['soif']
        sensation_estomac= form.cleaned_data['sensation_estomac']
        plaisir_manger = form.cleaned_data['plaisir_manger']
        plaisir_boire = form.cleaned_data['plaisir_boire']
        quantite_manger = form.cleaned_data['quantite_manger']
        quantite_boire = form.cleaned_data['quantite_boire']
        heure_rep=form.cleaned_data['heure_dernier_repas']
        heure_derniere_prise = form.cleaned_data['heure_derniere_prise']
        prochain=form.cleaned_data['prochain_repas']

        nv_test=Test.objects.create(id_utilisateur=user,
                            heure_dernier_repas=heure_rep,heure_derniere_prise_alim=heure_derniere_prise,
                            faim=faim,soif=soif, sensation_estomac=sensation_estomac,
                            plaisir_manger=plaisir_manger,plaisir_boire=plaisir_boire,
                            quantite_manger=quantite_manger
                            ,quantite_boire=quantite_boire,prochain_repas=prochain)
        
        liste_choix.rempli()
        liste_choix.set_test(nv_test)
        send=True

        
    return render(request,'polls/test1.html',locals())


def test_image(request,id_image):
    progression=str(int(int(id_image)*100/20))+"%"
    Reponse=''
    try :
        liste_choix.test
    except:
        Reponse=redirect(accueil)
    if int(id_image)>20 :
        Fini=True
        form2=commentaire(request.POST or None)
        if form2.is_valid():
            comment=form2.cleaned_data['commentaire']
            Fini2=True
            if request.user.is_authenticated():
                Commentaire.objects.create(Test=liste_choix.test,commentaire=comment)
            
            
        Reponse =render(request,'polls/test2.html',locals())
    else :
        if liste_choix.choix==[]:
            liste_choix.rempli()
       
        form=test_aliment_form(liste_choix.choix[int(id_image)-1],request.POST or None)
        if form.is_valid():
            aliment_prefere=form.cleaned_data['choix_alim']
            if liste_choix.choix[int(id_image)-1][0][0]==aliment_prefere :
                aliment_non_prefere=liste_choix.choix[int(id_image)-1][1][0]
            else :
                aliment_non_prefere=liste_choix.choix[int(id_image)-1][0][0]
            if request.user.is_authenticated():
                user_name=Utilisateurs.objects.filter(Nom_utilisateur__username__exact=request.user.username)[0]
                Preference.objects.create(id_utilisateur=user_name,aliment_prefere=aliment_prefere
                                          ,aliment_non_prefere=aliment_non_prefere,
                                          id_Test=liste_choix.test)
            send=True
            if int(id_image)<9:
                id_image="0"+str(int(id_image)+1)
                Reponse=redirect(test_image,id_image)
            else :
                id_image=str(int(id_image)+1)
                Reponse=redirect(test_image,id_image)
    if Reponse=='':
            Reponse=render(request,'polls/test2.html',locals())

        

           
    return Reponse


def connexion(request):


    form = ConnexionForm(request.POST or None)
    if form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
        if user is not None:# Si l'objet renvoyé n'est pas None
            login(request, user)  # nous connectons l'utilisateur


        else: # sinon une erreur sera affichée

            error = True



    return render(request, 'polls/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def reglement(request):
    return render(request,'polls/reglement.html')



    
