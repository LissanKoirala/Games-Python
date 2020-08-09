# Creator : Lissan Koirala
# Date of Creation : 09/03/2019

import random
import time

print("DECISION MAKER")
print("THIS IS THE FINAL ANSWER, YOU HAVE TO ACCEPT THIS!")

time.sleep(1)
print("Computer Thinking...")
time.sleep(0.5)
print("In 3...")
time.sleep(1)
print("In 2...")
time.sleep(1)
print("In 1...")
time.sleep(1)

print("-------------")

x=random.randint(1,4)


one = input("First Option : ")
two = input("Second Option : ")
three = input("Third Option : ")
four = input("Fourth Option : ")
if x == 1:
    print("Final Result:", one)
if x == 2:
    print("Final Result:", two)
if x == 3:
    print("Final Result:", three)
if x == 4:
    print("Final Result:", four)


input()




