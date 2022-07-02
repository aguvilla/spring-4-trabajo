import csv 
import sys
from datetime import datetime

filterlist = []
newcsv=[["FechaOrigen","FechaDePago","Monto","NroCuenta"]]
argumento = sys.argv
file= argumento[1]
file= open( file, "r")
def fecha(fecha):
    t1 = datetime.fromtimestamp(int(fecha))
    return (t1.strftime("%d/%m/%Y"))
    
if len(argumento)>4:
    dni = argumento[2]
    salida = argumento[3].lower()
    tipo_cheque = argumento[4].upper()
    if len(argumento)>5:
        estado = argumento[5].upper()
        if len(argumento)==7:
            rango_fecha = argumento[6]
            rango_fecha = rango_fecha.split(":")
            fecha1 = int((datetime.strptime(rango_fecha[0], '%d-%m-%Y') ).timestamp())
            fecha2 = int((datetime.strptime(rango_fecha[1], '%d-%m-%Y') ).timestamp())
               
else:
    print ("ERROR EN LOS DATOS INGRESADOS")
    exit()

lineas = csv.reader(file)

for linea in lineas:
    if len(argumento)==6:
        if linea[-3] == dni and linea[-2] == tipo_cheque and linea[-1] == estado:
            filterlist.append(linea)
            
    elif len(argumento)==5 and linea[-3] == dni and linea[-2] == tipo_cheque:
        filterlist.append(linea)
    elif len(argumento)==7 and linea[-3] == dni and linea[-2] == tipo_cheque and fecha1<=int(linea[-5])<=fecha2:
        filterlist.append(linea)
    
for linea in filterlist:
    linea[-4] = fecha(linea[-4])
    linea[-5] = fecha(linea[-5])

file.close()

if filterlist == []:
    print("No se encontraron resultados")
    exit()

for lis in filterlist:
    line = [lis[-5], lis [-4], lis[-6], lis [-8]]
    newcsv.append(line)

if salida == "csv":
    f = open ( dni+ "-" + (datetime.now()).strftime("%d%m%y_%H_%M_%S") +".csv", "w", newline='')
    archivo_csv = csv.writer(f)
    archivo_csv.writerows(newcsv)
    f.close()

elif salida == "pantalla":
    print(newcsv) 