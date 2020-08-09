# Creator : Lissan Koirala
# Date of Creation : 13/03/2019

import random
import time

words = ['False','else','import','pass','None','break','except','in','True','class','finally','is','return','and','continue','for','lambda','try','as','def','from','while','assert','del','global','not','with','elif','if','or','list','string','float','integer']


print(" \n ")
print("-"*100)
print("Guess some Python Words and Win - Just Simple as That!")
print("-"*100)
length = len(words) - 1
r = 0
w = 0

for i in range(3):
  x = random.randint(1,length)
  real_answer = words[x]
  answer = input("Your Guess : ")
  print("-"*100)
  if answer == real_answer:
    print("Hurray You Got it Right!")
    print("-"*100)
    r =+ 1

  else:
    print("Your are Wrong, Try Again!")
    print("-"*100)
    print("The Right Answer was : ",real_answer)
    print("-"*100)
    w += 1

print("The Game ends here! :)")
print("-"*100)
print("Your got",r," Guesses right :)","\nYou got",w," Guesses Wrong :(")
print("-"*100)
print("This Game will close in :")
t = 10
for i in range(10):
  print("-",t)
  time.sleep(1)
  t -= 1

