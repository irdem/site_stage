from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from  random import randint


class Utilisateurs(models.Model):
    Nom_utilisateur=models.OneToOneField(User)
    Age = models.PositiveIntegerField()
    Poids = models.PositiveIntegerField()
    Taille_centimetre = models.PositiveIntegerField(default=0)
    Sport = models.CharField(max_length=100,default="Unknown")
    Vegetarien = models.BooleanField(default=False)
    Vegan = models.BooleanField(default=False)
    Sans_lactose= models.BooleanField(default=False)
    Sans_gluten = models.BooleanField(default=False)
    Sans_porc = models.BooleanField(default=False)
    
    
    Choices = [("F",'femme'),("H",'homme')]
    Sexe = models.CharField(choices=Choices, max_length=100)
    
    Choices = [("perte","Perte de poids"),("maintien","Maintien d'un poids stable"),
               ("med","Raisons médicales autres que la perte de poids"),("aucun","Pas de régime suivi")]
    Regime_raison =models.CharField(choices=Choices,max_length=100,default="aucun")
    Nb_enfants =models.IntegerField(default=0)
    
    choix = [("quotidien","au moins 4 fois par semaine"),("hebdo","2 à 3 fois par semaine")
    ,("mensuel","2 à 4 fois par mois"),("rare","1 fois par mois ou moins"),("jamais","jamais")]
    Consommation_alcool =models.CharField(default="none",max_length=100,choices=choix)
    
    Choices = [('reg','Régulier'),('occ','Occasionnel'),('ancien','A arrêté de fumer'),
    ('nf','Non fumeur'),("O","unknown")]
    Help="<p>Régulier : vous fumez au moins une cigarette (ou autre) par jour</p><p> Occasionnel : vous fumez moins d' une cigarette (ou autre) par jour </p>"
    Fumeur =models.CharField(choices=Choices, help_text=Help, default="0",max_length=100)
    
    Choices=[("1","Sans diplôme"),("2","Brevet des collèges"),("3","CAP,BEP"),
             ("4","Bac (général, technologique ou professionnel)")
             ,("5","Bac +2 (BTS ou autre )"),("6","Bac +3/4 (license, maitrise)")
               ,("6", "Bac +5 (Master,diplome d'ingénieur,  école de commerce)")
               ,("7", "Bac +8"),("0","Unknown")
             ]
    Niveau_etudes = models.CharField(choices=Choices, default="0",max_length=100)
    
    Code_postal = models.CharField(max_length=5,default="00000")
    
    enceinte= models.BooleanField(default=False)
    allaite=models.BooleanField(default=False)
    

    def __str__(self):

        return "Profil de {0}".format(self.Nom_utilisateur.username)
    

class Image(models.Model):
    Chemin_image=models.ImageField(upload_to=None, height_field=None,width_field=None,max_length=100)
    
    
    
    

class Test(models.Model):
    id_Test=models.AutoField(primary_key=True)
  
    id_utilisateur=models.ForeignKey(Utilisateurs) 
    heure_dernier_repas=models.TimeField(auto_now=False, auto_now_add=False)
    heure_derniere_prise_alim=models.TimeField(auto_now=False, auto_now_add=False)
    faim =models.IntegerField(default=0)
    soif= models.IntegerField(default=0)
    sensation_estomac =models.IntegerField(default=0)
    plaisir_manger =models.IntegerField(default=0)
    plaisir_boire = models.IntegerField(default=0)
    quantite_manger=models.IntegerField(default=0)
    quantite_boire = models.IntegerField(default=0)
    Choices = [("petit-dej","petit-dejeuner"),("dej","déjeuner"),("snack","goûter/snack/collation"),("diner","diner")]
    prochain_repas = models.CharField(default="none", max_length=100, choices=Choices)
    date_test=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "Test de {0} ".format(self.id_utilisateur.Nom_utilisateur.username) + "fait le {0} ".format(self.date_test)

class Preference(models.Model):
    id_utilisateur=models.ForeignKey(Utilisateurs,on_delete=models.CASCADE)
    aliment_prefere=models.CharField(max_length=100)
    aliment_non_prefere=models.CharField(max_length=100)
    id_Test= models.ForeignKey(Test, on_delete=models.CASCADE)
    heure=models.DateTimeField(default=timezone.now)

class Commentaire(models.Model):
    Test=models.ForeignKey(Test, on_delete=models.CASCADE)
    commentaire=models.TextField(help_text='Vous pouvez insérer un commentaire si vous le souhaitez')

    
class Aliment(models.Model):
    nom_aliment=models.CharField(max_length=100, primary_key=True)
    description=models.TextField()
    groupe=models.CharField(max_length=100,default='none')
    
    def __str__(self):

        return self.nom_aliment
    
    def select_choix(self):
        choix1=self.objects.order_by('?')[0]
        ens2=self.objects.exclude(nom_aliment=choix1.nom_aliment)
        num=randint(0,len(ens2)-1)
        choix2=ens2[num]
        choix=[(choix1.nom_aliment,choix1.nom_aliment),(choix2.nom_aliment,choix2.nom_aliment)]
        
        return choix
    
    