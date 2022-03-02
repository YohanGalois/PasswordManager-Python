# coding: utf-8
from tkinter import*
import tkinter as tkinter
import tkinter.ttk
import codecs

# creation d'une fenetre
fenetre = Tk()
fenetre.title('prog1bis')
listedecrypt=0
#Fonction de Yohan
     #Cryptage
def cryptage(data):
        fichier=open("date.txt","r")
        ensemble=fichier.readlines()
        month=ensemble[0]
        month=int(month)
        day=ensemble[1]
        day=int(day)
        i=1
        service=data[0]
        lenservice=str(len(service)+1)
        datacrypt=[(lenservice),(service)]
        while (len(data)+1) != len(datacrypt) :
                madp=list(data[i])  
                motdepassebrut= (madp )
                motdepasseascii=[]
                motdepasseasciicrypte=[]
                motdepassecrypteenlettre=[]
                j=0
                k=0
                avanceliste=0
                while (len(motdepasseascii)) < (len(motdepassebrut)) :
                    j=motdepassebrut[avanceliste]
                    k=ord(j)
                    motdepasseascii=motdepasseascii+[k]
                    avanceliste =(avanceliste + 1)
                    j=0
                    k=0
                avanceliste=0
                while (len(motdepasseasciicrypte)) != (len(motdepasseascii)):
                    j=motdepasseascii[avanceliste]
                    k=(j*(day))+(month)
                    motdepasseasciicrypte=motdepasseasciicrypte+[k]
                    avanceliste=(avanceliste + 1)
                    j=0
                    k=0
                avanceliste=0
                while (len(motdepassecrypteenlettre)) < (len(motdepasseasciicrypte)):
                    j=motdepasseasciicrypte[avanceliste]
                    k=chr(j)
                    motdepassecrypteenlettre=motdepassecrypteenlettre+[k]
                    avanceliste=(avanceliste + 1)
                    j=0
                    k=0
                avanceliste=0
                mdp="".join(motdepassecrypteenlettre)
                datacrypt=datacrypt+[mdp]
                datacrypte=" ".join(datacrypt)
                datacrypte=(datacrypte)
                i=i+1
        return(datacrypte)
        #decryptage
def decryptage (datacrypte): 
        fichier=open("date.txt","r")
        ensemble=fichier.readlines()
        month=ensemble[0]
        month=int(month)
        day=ensemble[1]
        day=int(day)
        lenservice=datacrypte[0]
        print (lenservice)
        i=int(lenservice)
        datacrypte=" ".join(datacrypte)
        print(datacrypte)
        while len(datacrypte) != (i) :
                madp=datacrypte
                motdepassecrypteenlettre=madp 
                motdepassecrypteenascii=[]
                motdepassedecrypteenascii=[]
                motdepassedecrypteenlettre=[]
                avanceliste=int(lenservice)
                k=0
                service=[]
                while k != (int(lenservice)-(len(lenservice))+2):
                        l=datacrypte[k]
                        service=service+[l]
                        k=k+1      
                k=0
                l=0
                service=service+[" "]
                while (avanceliste) < (len(motdepassecrypteenlettre)) :
                        j=motdepassecrypteenlettre[avanceliste]
                        k=ord(j)
                        motdepassecrypteenascii=motdepassecrypteenascii+[k]
                        avanceliste = (avanceliste + 1)
                        
                        j=0
                        k=0
                avanceliste=0
                while (len(motdepassedecrypteenascii)) < (len(motdepassecrypteenascii)) :
                        j=motdepassecrypteenascii[avanceliste]
                        k=(int((j-month)/day))
                        if (k) != 1 :
                                l=chr(k)
                        else :
                                l=" "
                        motdepassedecrypteenascii=motdepassedecrypteenascii+[l]
                        avanceliste=(avanceliste + 1)
                        j=0
                        k=0   
                avanceliste=0
                datadecrypt=(service)
                datadecrypt=datadecrypt+motdepassedecrypteenascii
                datadecrypte="".join(datadecrypt)
                datadecrypte =str(datadecrypte)
                datadecrypte=datadecrypte.replace(" "," ",0)
                datadecrypte=list(datadecrypte)
                del datadecrypte[0]
                datadecrypte="".join(datadecrypte)
                i=i+1
        return(datadecrypte)
#Fonctions de Paul
     #Classement dans l'onglet service
def classerservicesalphabe():
     ligne=0
     cla=[]
     liste=[]
     clafinal=[]

     with codecs.open("BaseDeDonnees3.txt", "r",encoding='utf-8') as fichier:
             ensemble=fichier.readlines()

     liste=ensemble[ligne].split(' ')

     while ligne<len(ensemble):
        liste=ensemble[ligne].split(' ')
        cla.append(liste[1])
        ligne=ligne+1
     cla.sort()
     return cla

malistetriee=classerservicesalphabe()
#Inscription dans le fichier texte
def inscription(datacrypte):
        with codecs.open("BaseDeDonnees3.txt", "a",encoding='utf-8') as fichier:
                fichier.write((datacrypte)+"\n")

        fichier.close()


def secondaire():

    panelCombo = tkinter.ttk.Frame(fenetre)
    panelCombo.pack( side='top', fill='x'  )
    valCombo = (malistetriee)
    varCombo = tkinter.StringVar()
    varCombo.set( 'SERVICES' )
    cboCombo = tkinter.ttk.Combobox( panelCombo, values=valCombo, textvariable=varCombo )
    cboCombo.pack( side='left', anchor='w', padx=2, pady=8 )
def recherchemdp(nom):

 ligne=1

 with codecs.open("BaseDeDonnees3.txt","r",encoding='utf-8') as fichier:
         ensemble=fichier.readlines()
         liste=[]

         liste=ensemble[ligne].split(' ')

 while liste[1]!=nom and ligne<len(ensemble):
        liste=ensemble[ligne].split(' ')
        liste[3]=liste[3].rstrip('\n')
        ligne=ligne+1

 return liste
etiquette=Label(fenetre)
etiquette.configure(text='Logiciel de gestion de mots de passe ',fg='red')
etiquette.pack()
bouton = Button(fenetre, text='Services',command=secondaire )
bouton.pack()

#PARTIE LOGIN
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.configure(text='Login',fg='blue')
etiquette.pack()
# creation d'une zone de saisie
texte=StringVar()
saisie=Entry(fenetre)
saisie.configure(textvariable=texte, fg='red')
saisie.pack()
#PARTIE MDP
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.configure(text='Mot de passe',fg='blue')
etiquette.pack()
# creation d'une zone de saisie
texte2=StringVar()
saisie=Entry(fenetre)
saisie.configure(textvariable=texte2, fg='red')
saisie.pack()
#PARTIE SERVICE
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.configure(text='Nom du Service',fg='blue')
etiquette.pack()
# creation d'une zone de saisie
texte3=StringVar()
saisie=Entry(fenetre)
saisie.configure(textvariable=texte3, fg='red')
saisie.pack()
#PARTIE JOUR DE NAISSANCE
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.configure(text='Jour de naissance (JJ)',fg='blue')
etiquette.pack()
# creation d'une zone de saisie
texte4=StringVar()
saisie=Entry(fenetre)
saisie.configure(textvariable=texte4, fg='red')
saisie.pack()
#PARTIE MOIS DE NAISSANCE
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.configure(text='Mois de naissance (MM)',fg='blue')
etiquette.pack()

# creation d'une zone de saisie
texte5=StringVar()
saisie=Entry(fenetre)
saisie.configure(textvariable=texte5, fg='red')
saisie.pack()
# creation d'un bouton
bouton7=Button(fenetre)
bouton7.configure(text='Cliquer',bg='white')
bouton7.pack()
def clic7(event):
     login=texte.get()
     mdp=texte2.get()
     service=texte3.get()
     day=texte4.get()
     month=texte5.get()
     data=[(service),(login),(mdp)]
     print(data)
     datacrypte=cryptage(data)
     print(datacrypte)
     inscription(datacrypte)
     
bouton7.bind("<ButtonPress-1>",clic7)
# creation d'une etiquette
etiquette=Label(fenetre)
etiquette.configure(text='Saisissez le nom du service recherché',fg='blue')
etiquette.pack()

# creation d'une zone de saisie
texte6=StringVar()
saisie=Entry(fenetre)
saisie.configure(textvariable=texte6, fg='red')
saisie.pack()
# creation d'un bouton
bouton8=Button(fenetre)
bouton8.configure(text='Cliquer',bg='white')
bouton8.pack()
etiquette=Label(fenetre)
etiquette.configure(text='Vos informations de connection ',fg='blue')
etiquette.pack()
def clic8(event):
     Nomduservice2=texte6.get()
     liste=recherchemdp(Nomduservice2)
     print (liste)
     listedecrypt=decryptage(liste)
     etiquette45.configure(text=(listedecrypt),fg='blue')
     
bouton8.bind("<ButtonPress-1>",clic8)
etiquette45=Label(fenetre)
etiquette45.configure(text=" ",fg='blue')
etiquette45.pack()
# attente des evenements
fenetre.mainloop()
