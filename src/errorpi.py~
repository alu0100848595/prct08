#! encoding: UTF-8
#! /usr/bin/python 
import modulopi
import math
PI=  3.1415926535897931159979634685441852
def error(nro_intervalos, nro_test, umbral):
  j=0
  for i in range (nro_test):
    s=modulopi.aproxpi(nro_intervalos)
    valor=abs(s-PI)
    if valor>=umbral:
      j+=1
  por_error=j/nro_test
  por_error=por_error*100
  return por_error
    
n=int(raw_input("introduzca el numero de intervalos:"))
t=int(raw_input("introduzca el numero de test:"))
u=float(raw_input("introduzca el valor del umbral:"))

v=error(n,t,u)
print "Hay un porcentaje de error de %d"%(v)

