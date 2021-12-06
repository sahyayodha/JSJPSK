import math
pembatas="--------------------"
print("JP, JS, SK") 
print("BY: NEOZA")
print(pembatas)

type=str(input("TYPE[JS|JP|SK] : "))
print(pembatas)

if type.lower()=="sk" or type.lower()=="skala" :
  jssk=int(input("JS[Jarak Sebenarnya] : "))
  jpsk=int(input("JP[Jarak Peta] : "))
  sksk=jssk/jpsk
  print("SK[Skala] :", sksk)
  print(pembatas)

elif type.lower()=="jp" or type.lower()=="jarak peta" :
  jsjp=int(input("JS[Jarak Sebenarnya] : "))
  skjp=int(input("SK[Skala] : "))
  jpjp=jsjp/skjp
  print("JP[Jarak Peta] :", jpjp)
  print(pembatas)

elif type.lower()=="js" or type.lower()=="jarak sebenarnya" :
  jpjs=int(input("JP[Jarak Peta] : "))
  skjs=int(input("SK[Skala] : "))
  jsjs=jpjs*skjs
  print("JS[Jarak Sebenarnya :", jsjs)
  print(pembatas)

else :
  print("ERROR")
  print(pembatas)
