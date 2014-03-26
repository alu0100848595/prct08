#! encoding: UTF-8
#! /usr/bin/python 
def aproxpi(fin):
 f=1
 while fin>0 and f==1:
  f+=1
  suma=0
  for i in range (1,fin+1):
   a=float(i-1)/fin
   b=float (i)/fin
   x_i=float(i-0.5)/fin
   fx_i=float (4)/(1+x_i*x_i)
   suma+=fx_i
  aprox=suma/fin
 return aprox
if __name__=="__main__":
 import sys
 if(len(sys.argv)==3):
   p1=int(sys.argv[1])
   p2=int(sys.argv[2])
   l=[]
   for i in range (1,p2+1):
    s=aproxpi(p1+1)
    l=l+[s]
   print l
 else:
  print "Debe introducir dos numeros en la linea de comandos"
  p1=5
  p2=5
  l=[]
  for i in range (1,p2+1):
   s=aproxpi(p1+1)
   l=l+[s]
  print l