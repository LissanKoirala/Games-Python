# Creator : Lissan Koirala
# Date of Creation : 09/12/2019

import random
import time
from playsound import playsound

def generator(one, two, three, four):
	which = random.randint(1,10)

	if which == 1:
		number = one + two + three + four 
		time = 60
		what = "one + two + three + four"

	if which == 2:
		number = (one - two) + (three - four)
		time = 180
		what = "one - two + three - four"

	if which == 3:
		number = one * two * three * four
		time = 200
		what = "one * two * three * four"

	if which == 4:
		number = (one / two) + (three / four)
		time = 300
		what = "one / two + three / four"

	if which == 5:
		number = one - two - three - four
		time = 200
		what = "one - two - three - four"

	if which == 6:
		number = (one - two) * (three - four)
		time = 300
		what = "one - two * three - four"

	if which == 7:
		number = one / two / three / four
		time = 450
		what = "one / two / three / four"

	if which == 8:
		number = one + two - three * four
		time = 400
		what = "one + two - three * four"

	if which == 9:
		number = one - two - three - four
		time = 240
		what = "one - two - three - four"

	if which == 10:
		number = (one * two) / (three * four)
		time = 400
		what = "one * two / three * four"

	return number, time, what

while True:
	print("\n\n")
	print("-"*119)
	print("Find the provided number Using : | + | - | * | / | and all 4 numbers")
	print("-"*119)
	o = int(input("Enter the First Number : "))
	t = int(input("Enter the Second Number : "))
	th = int(input("Enter the Third Number : "))
	f = int(input("Enter the Fourth Number : "))
	print("-"*119)

	function = generator(o, t, th, f)

	number_to_find = function[0]
	time_to_wait = function[1]
	answer = function[2]

	print("The number that you want to find is", number_to_find, "in %s seconds" %time_to_wait)
	print("-"*119)
	print(".........")
	time.sleep(3)
	print("Now Start!")
	print("-"*119)
	time.sleep(time_to_wait)
	print("The time has finished, Now it's the time to Check your answer")
	playsound("fileexample.mp3") # Keep this file which will play after the time ends
	print("-"*119)
	check = input("Press any key to see the Answer : ")
	print("-"*119)
	print("The Answer was : %s, Congratulations if You Got it Right" %answer)
	print("-"*119)



