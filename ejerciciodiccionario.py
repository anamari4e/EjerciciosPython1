from optparse import Values


arroz= dict(
    enero=12345,
    febrero=23456,
    marzo=45678,
    abril=123456,
    mayo=12542,
    junio=344434,
    julio=34853,
    agosto=23849,
    septiembre=23424,
    octubre=344232,
    noviembre=131231,
    diciembre=21343,
)

maxi=max(arroz.keys(), key=lambda k:arroz[k])
print('El mes con mayor producción fue: ', maxi,arroz[maxi])

mini=min(arroz.keys(), key=lambda k:arroz[k])
print('El mes con menor producción fue: ', mini,arroz[mini])

prom=tuple(arroz.values())
b=len(prom)
suma=0
for val in prom:
    suma+=val
total=suma/b
print('El promedio es ', total)

for datos in arroz.keys():
    if (arroz[datos]>=total):
        print('El mes',datos, 'es mayor que el promedio')
        
    elif (arroz[datos]<=total):
        print('El mes' ,datos, 'es menor que el promedio')
    






