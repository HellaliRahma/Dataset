import pandas as pd
import os
import csv
import random
from random import randint
from random import uniform

#os.chdir("C:/Users/RAHMA/XCSR_Application/Application")
#
#textdata = pd.read_csv('copie_prop.csv')
#actions_list = textdata['action'].values.tolist()
#num_action = textdata['num_action'].values.tolist()
#sub_action1 = textdata['sub_action1'].values.tolist()
#sub_action2 = textdata['sub_action2'].values.tolist()
#sub_action3 = textdata['sub_action3'].values.tolist()
#temps = textdata['temps'].values.tolist()
#temps_min = textdata['temps_min'].values.tolist()
#temps_max = textdata['temps_max'].values.tolist()
#
#
#textdata1 = pd.read_csv('dataset_for_disabled.csv')
#Date = textdata1['Date'].values.tolist()
#Time = textdata1['Time'].values.tolist()
#Temperature_Comedor_Sensor = textdata1['Temperature_Comedor_Sensor'].values.tolist()
#Temperature_Exterior_Sensor = textdata1['Temperature_Exterior_Sensor'].values.tolist()
#Lighting_Habitacion_Sensor = textdata1['Lighting_Habitacion_Sensor'].values.tolist()
#Humedad_Habitacion_Sensor = textdata1['Humedad_Habitacion_Sensor'].values.tolist()
#Humedad_Exterior_Sensor = textdata1['Humedad_Exterior_Sensor'].values.tolist()
#Meteo_Exterior_Viento = textdata1['Meteo_Exterior_Viento'].values.tolist()
#Day_Of_Week = textdata1['Day_Of_Week'].values.tolist()
#real_action = textdata1['real_action'].values.tolist()
#sub_real_action = textdata1['sub_real_action'].values.tolist()


def afficher_liste_actions_selon_temps():
    file_name = "remplir.csv"
    write_csv = csv.writer(open(file_name,'w'),lineterminator='\n')
    write_csv.writerow(["Date","Time","Temperature_Comedor_Sensor","Temperature_Exterior_Sensor","Lighting_Habitacion_Sensor","Humedad_Habitacion_Sensor","Humedad_Exterior_Sensor","Meteo_Exterior_Viento","Day_Of_Week","real_action","a1","a2","a3","a4","a5","a6","a7","a8","a9","a10"])
    liste_actions=[]
    for i in range(len(Date)):
        print("les actions possible pour l'itération   "+str(i)+"  et le temps  "+str(Time[i]))
        for j in range(len(actions_list)):
#            print(j)
            if temps_min[j] <= Time[i] < temps_max[j]:
                liste_actions.append(num_action[j])
        write_csv.writerow([Date[i],Time[i],round(Temperature_Comedor_Sensor[i],2),round(Temperature_Exterior_Sensor[i],2),round(Lighting_Habitacion_Sensor[i],2),round(Humedad_Habitacion_Sensor[i],2),round(Humedad_Exterior_Sensor[i],2),round(Meteo_Exterior_Viento[i],2),Day_Of_Week[i],liste_actions])
        liste_actions.clear()



def get_actions_by_condition():
    file_name = "dataset.csv"
    write_csv = csv.writer(open(file_name,'w'),lineterminator='\n')
    write_csv.writerow(["Date","Time","Temperature_Comedor_Sensor","Temperature_Exterior_Sensor","Lighting_Habitacion_Sensor","Humedad_Exterior_Sensor","real_action"])
    liste_actions=[]
    for i in range(len(Date)):

        #ouvrir fenetre
        if round(Temperature_Exterior_Sensor[i],2) > round(Temperature_Comedor_Sensor[i],2):
            liste_actions.append(num_action[0])

        #fermer fenetre
        if '17:00'<=Time[i]<='19:30':
            liste_actions.append(num_action[1])

        #Changer la position du lit
        if '07:00'<=Time[i]<='22:30':
            liste_actions.append(num_action[2])

        #Faire la toilette
        if '09:00'<=Time[i]<='10:00':
            liste_actions.append(num_action[3])

        #Changer les vêtements
        if '10:00'<=Time[i]<='11:00':
            liste_actions.append(num_action[4])

        #Prendre petit dejeuner
        if '07:00'<=Time[i]<='09:00':
            liste_actions.append(num_action[5])

        #Deplacer
        if '11:00'<=Time[i]<='12:00':
            liste_actions.append(num_action[6])
            #boire
        if '07:00'<=Time[i]<='22:30':
            liste_actions.append(num_action[7])
            #Ecouter
        if '11:00'<=Time[i]<='12:00':
            liste_actions.append(num_action[8])

            #Voir la television
        if '14:00'<=Time[i]<='16:00':
            liste_actions.append(num_action[9])

            #Regler la temperature
        if round(Temperature_Comedor_Sensor[i],2) < 18.0 or round(Temperature_Comedor_Sensor[i],2) > 20.0:
            liste_actions.append(num_action[10])

            #Prendre le dejeuner
        if '12:00'<=Time[i]<='13:00':
            liste_actions.append(num_action[11])

            #Prendre diner
        if '18:00'<=Time[i]<='20:00':
            liste_actions.append(num_action[12])

            #Dormir
        if '14:00'<=Time[i]<='22:30':
            liste_actions.append(num_action[13])

            #Avoir une couverture supplementaire
        if round(Temperature_Comedor_Sensor[i],2) < 18:
            liste_actions.append(num_action[14])

            #Regler lumiere
        if '19:00'<=Time[i]<='22:30'or round(Lighting_Habitacion_Sensor[i],2) < 40:
            liste_actions.append(num_action[15])

        write_csv.writerow([Date[i],Time[i],round(Temperature_Comedor_Sensor[i],2),round(Temperature_Exterior_Sensor[i],2),round(Lighting_Habitacion_Sensor[i],2),round(Humedad_Habitacion_Sensor[i],2),round(Humedad_Exterior_Sensor[i],2),round(Meteo_Exterior_Viento[i],2),Day_Of_Week[i],random.choice(liste_actions)])
        liste_actions.clear()



def Time_ouvrir_fenetre():
    t1 = randint(7,16)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time


def Time_fermer_fenetre():
    t1 = randint(17,18)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time


def Time_changer_position():
    t1 = randint(17,18)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time

def Time_breakfast():
    t1 = randint(7,8)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time


def Time_breakfast():
    t1 = randint(7,8)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time
def Time_lunch():
    t1 = randint(12,13)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time

def Time_dinner():
    t1 = randint(19,20)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time


def Time_deplacer():
    t1 = randint(11,11)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time

def Time_drink():
    t1 = randint(7,21)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time

def Time_regler_temperature ():
    t1 = randint(7,21)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time


def Time_regler_lumiere ():
    t1 = randint(7,21)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time


def Time_dormir ():
    t1 = randint(14,21)
    t2 = randint(0,59)
    if t1 < 10:
        t1 = "0" + str(t1)
    if  t2 < 10:
        t2 = "0" + str(t2)
    random_time = str(t1) + ":" + str(t2) 
    return random_time



def generate_situation ():
    file_name = "Test2.csv"
    write_csv = csv.writer(open(file_name,'w'),lineterminator='\n')
    write_csv.writerow(["Time","Temperature_Comedor_Sensor","Temperature_Exterior_Sensor","Lighting_Habitacion_Sensor","state_window","state_bed","real_action"])

    for i in range(200):

        #ouvrir fenetre
        #random time+temps entre 7h et 17h
        #choisir temprature exterieur > interieur
        #temp interieur doit être entre 18 et 20
        #random temp chambre
        Time0 = Time_ouvrir_fenetre()
        room_temperature0 = randint(18,20)
        outside_temperature0 = randint(21,26)
        room_lighting0 = randint(40,100)
        state_window0 = round(uniform(0,1),2)#fermée
        state_bed0 = round(uniform(0,3),2)
        real_action0 = 0
        write_csv.writerow([Time0,room_temperature0,outside_temperature0,room_lighting0,state_window0,state_bed0,real_action0])
        
        
        #fermer fenetre
        
        Time1 = Time_fermer_fenetre()
        room_temperature1 = randint(18,20)
        outside_temperature1 = randint(15,17)
        room_lighting1 = randint(30,40)
        state_window1 = round(uniform(1,2),2)#ouverte
        state_bed1 = round(uniform(0,3),2)
        real_action1 = 1
        write_csv.writerow([Time1,room_temperature1,outside_temperature1,room_lighting1,state_window1,state_bed1,real_action1])
          
        
        #changer position
        Time2 = Time_changer_position()
        room_temperature2 = randint(18,20)
        outside_temperature2 = randint(15,17)
        room_lighting2 = randint(40,90)
        state_window2 = round(uniform(0,2),2)
        state_bed2 = round(uniform(0,1),2)#(n'importe quelle position)
        real_action2 = 2
        write_csv.writerow([Time2,room_temperature2,outside_temperature2,room_lighting2,state_window2,state_bed2,real_action2])        
    
    
#        #breakfast(7h 9h)
#        Time3 = Time_breakfast()
#        room_temperature3 = randint(18,20)
#        outside_temperature3 = randint(15,17)
#        room_lighting3 = randint(40,90)
#        state_window3 = round(uniform(0,3),2)
#        state_bed3 = round(uniform(2,3),2)#haut
#        real_action3 = 3
#        write_csv.writerow([Time3,room_temperature3,outside_temperature3,room_lighting3,state_window3,state_bed3,real_action3])
#    
#
#        #lunch(12h 14h )
#        Time4 = Time_lunch()
#        room_temperature4 = randint(18,20)
#        outside_temperature4 = randint(15,17)
#        room_lighting4 = randint(40,90)
#        state_window4 = round(uniform(0,3),2)
#        state_bed4 = round(uniform(2,3),2)#haut
#        real_action4 = 4
#        write_csv.writerow([Time4,room_temperature4,outside_temperature4,room_lighting4,state_window4,state_bed4,real_action4])
#
#        #dinner(19h 21h)
#        Time5 = Time_dinner()
#        room_temperature5 = randint(18,20)
#        outside_temperature5 = randint(15,17)
#        room_lighting5 = randint(40,90)
#        state_window5 = round(uniform(0,3),2)
#        state_bed5 = round(uniform(2,3),2)#haut
#        real_action5 = 5
#        write_csv.writerow([Time5,room_temperature5,outside_temperature5,room_lighting5,state_window5,state_bed5,real_action5])
    
        #deplacer(11h 12h)
        Time6 = Time_deplacer()
        room_temperature6 = randint(18,20)
        outside_temperature6 = randint(15,17)
        room_lighting6 = randint(40,90)
        state_window6 = round(uniform(0,2),2)
        state_bed6 = round(uniform(0,3),2)#n'importe quelle position
        real_action6 = 3
        write_csv.writerow([Time6,room_temperature6,outside_temperature6,room_lighting6,state_window6,state_bed6,real_action6])
        
        #boire(7h 22h)
        Time7 = Time_drink()
        room_temperature7 = randint(18,20)
        outside_temperature7 = randint(15,17)
        room_lighting7 = randint(40,90)
        state_window7 = round(uniform(0,2),2)
        state_bed7 = round(uniform(2,3),2)#haut
        real_action7 = 4
        write_csv.writerow([Time7,room_temperature7,outside_temperature7,room_lighting7,state_window7,state_bed7,real_action7])
    
        #regler temperature pour temp < 18        
        Time8 = Time_regler_temperature()
        room_temperature8 = randint(14,17)
        outside_temperature8 = randint(15,17)
        room_lighting8 = randint(40,90)
        state_window8 = round(uniform(0,2),2)
        state_bed8 = round(uniform(0,3),2)#any position
        real_action8 = 5
        write_csv.writerow([Time8,room_temperature8,outside_temperature8,room_lighting8,state_window8,state_bed8,real_action8])


        #regler temperature pour temp > 20         
        Time8 = Time_regler_temperature()
        room_temperature8 = randint(21,29)
        outside_temperature8 = randint(15,17)
        room_lighting8 = randint(40,90)
        state_window8 = round(uniform(0,2),2)
        state_bed8 = round(uniform(0,3),2)#any position
        real_action8 = 5
        write_csv.writerow([Time8,room_temperature8,outside_temperature8,room_lighting8,state_window8,state_bed8,real_action8])
    
        #regler lumière        
        Time9 = Time_regler_lumiere()
        room_temperature9 = randint(18,20)
        outside_temperature9 = randint(15,17)
        room_lighting9 = randint(30,39)
        state_window9 = round(uniform(0,2),2)
        state_bed9 = round(uniform(0,3),2)#any position
        real_action9 = 6
        write_csv.writerow([Time9,room_temperature9,outside_temperature9,room_lighting9,state_window9,state_bed9,real_action9])
    
        #dormir        
        Time10 = Time_dormir()
        room_temperature10 = randint(18,20)
        outside_temperature10 = randint(15,17)
        room_lighting10 = randint(20,39)
        state_window10 = round(uniform(0,1),2)#ferme
        state_bed10 = round(uniform(0,3),2)#any position
        real_action10 = 7
        write_csv.writerow([Time10,room_temperature10,outside_temperature10,room_lighting10,state_window10,state_bed10,real_action10])
    
    

generate_situation()