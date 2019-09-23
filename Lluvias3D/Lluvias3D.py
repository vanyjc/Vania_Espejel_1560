# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:25:36 2019

@author: Vannie
"""
from Array3D import Array3D
import xlrd

precipitaciones = Array3D(32,12,35)

for anio in range(1985,2020,1):

    archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
    hoja=archivo.sheet_by_index(0)
    
    for r in range(precipitaciones.get_num_rows()):
        for c in range(precipitaciones.get_num_cols()):
            precipitaciones.set_item(r,c,anio-1985,hoja.cell_value(r+2,c+1))  
#FIN DEL ALMACENAMIENTO
            
print("ESTADOS:")
arch = xlrd.open_workbook(filename="./Precipitacion/"+'1985Precip.xls')
h = arch.sheet_by_index(0)
for i in range(0,32,1):
    print(f"{i+1}.- {h.cell_value(i+2,0)}")
    

cond=True
error=True
while cond==True:
    while error == True:
        an = int(input("¿Qué año(1985-2019)?: "))
        est = int(input("¿Qué estado?(1-32): "))
        mes = int(input("¿Qué mes?(1-12): "))
        if an<1985 or an>2019 or est<1 or est>32 or mes<1 or mes>12:
            error=True
            print("Un dato es invalido. Intentelo de nuevo.")
        else:
            error=False
        
    print(f"El promedio de centímetros cúbicos de lluvia fué de: {precipitaciones.get_item(est-1,mes-1,an-1985)}")
    
    respuesta=input("¿Desea realizar otra operacion? s/n: ")
    if respuesta == 's':
        cond=True
    else:
        cond=False

    
    
    
    
    
    
