import random




#creat random number

random_number = random.choice("123456789")
maimicde5 = 5
maimarede5 = 5

if int(random_number) <= 5 :  
   x =input("acest numar este mai mic de 5 , alege numarul: ")
if x ==random_number :
      print("BRAVO AI NIMERIT NUMARUL")
else : 
      input("mai incearca! Mai ai 2 incercari:")
if x == random_number :
      print("BRAVO AI NIMERIT NUMARUL")
else : 
 x = input("mai incearca! mai ai o incercare:")
if x == random_number :
   print("BRAVO AI NIMERIT NUMARUL")
else : 
  x = input("mai incearca! Ultima incercare:")
  print("AI GRESIT TOT , PROSTULE , NUMARUL ERA:" + random_number)
  
  
  
  
  if int(random_number) >= 5 : 
     y =input("Numarul este mai mare dechat 5! : ")
  if y == random_number :
      print("BRAVO AI NIMERIT NUMARUL")
  else : y=input("mai incearca! mai ai 3 incercari")
  if y ==  random_number :
        print("BRAVO AI NIMERIT NUMARUL")
  else: y=input("mai incearca! mai ai 2 incercari")
  if y == random_number : 
       print("BRAVO AI NIMERIT NUMARUL")
  else:
    y=input("Mai incearca1 mai ai o incercare")
  if y == random_number :
       print("BRAVO AI NIMERIT NUMARUL")
  else:
      print("PROSTULE , NUMARU ERA:" + random_number)
      
      
          
      
  







