#import interescompuestomensual
print("$"*100)
print("$"*100)
Tasa_Interes_Anual1=input("Seleciona TASA DE INTERES ANUAL EN PORCIENTO : ")
Tasa_Interes_Anual11=float(Tasa_Interes_Anual1)
Tasa_Interes_Anual=Tasa_Interes_Anual11/100
Tasa_Interes_Mensual=Tasa_Interes_Anual/12
Años_Totales1=input("Selecciona CANTIDAD TOTAL DE AÑOS : ")
Años_Totales=float(Años_Totales1)
Meses_Totales=round(Años_Totales*12)
Dolares_por_Mes1=input("Selecciona CANTIDAD DE DOLARES QUE VAS A INVERTIR EN COMPRAR BONOS MENSUALMENTE : ")
Dolares_por_Mes=float(Dolares_por_Mes1)
############################################
############################################
#AñosDeIny1=input("Insertá el AÑO ( puede ser en decimal ) en donde le aplicas un dinero extra de 100 dolares por mes : ")
#AñosDeIny=float(AñosDeIny1)
#MesDe_Inyeccion1=AñosDeIny*12
#MesDe_Inyeccion=round(MesDe_Inyeccion1)
#Dolares_Inyectados1=input("Insertá la cantidad de DOLARES que vas a meter extra : ")
#Dolares_Inyectados=float(Dolares_Inyectados1)
############################################
############################################
Cantidad_Final_CadaMes=[]
Cantidad_Final_CadaMes.append(Dolares_por_Mes*(1+Tasa_Interes_Mensual))

for i in range(1,Meses_Totales+1):
       #if MesDe_Inyeccion==i and MesDe_Inyeccion!=0:       
        # Cantidad_Final_CadaMes[i-1]=Dolares_Inyectados+Cantidad_Final_CadaMes[i-2]
         #Cantidad_Final_CadaMes.append((Cantidad_Final_CadaMes[i-1]+Dolares_por_Mes)*(1+Tasa_Interes_Mensual))
       #else :
         Cantidad_Final_CadaMes.append((Cantidad_Final_CadaMes[i-1]+Dolares_por_Mes)*(1+Tasa_Interes_Mensual))
  

#print(Cantidad_Final_CadaMes)
Cantidad_Total=Cantidad_Final_CadaMes[-1]
############################################
############################################
print("$"*100)
print("$"*100)
print(f"Compramos todos los meses durante {Años_Totales} años , una cantidad de {Dolares_por_Mes} DOLARES en renta fija que promete ganar una tasa de {Tasa_Interes_Anual11} % al año")
print(f"La cantidad de dolares que tendremos al pasar {Años_Totales} AÑOS será de : {round(Cantidad_Total,2)} DOLARES")
print("$"*100)
print("$"*100)
Ganancia_pormes=Cantidad_Total*Tasa_Interes_Mensual
print(f"Ganaríamos por mes pasivamente una cantidad de : {round(Ganancia_pormes,2)} DÓLARES")
print("$"*100)
print("$"*100)
SinInv=Meses_Totales*Dolares_por_Mes
print(f"Si solo ahorramos y no invertimos tendríamos en total {SinInv} DOLARES ")
print("$"*100)
print("$"*100)
#Dif=Cantidad_Total-interescompuestomensual.Ganancia_Total
#print(f"Diferencia entre comprar bonos todos los meses y comprar acumuladamente : {Dif}")