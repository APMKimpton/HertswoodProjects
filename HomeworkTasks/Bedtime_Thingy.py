#Imports
import time
import string
	# Variables
loop1 = True
	
while loop1:
	name = input ("What is your child's name?")
	if string.digits == True:
		print ("That is not a valid name, please enter one you scrub")
	else:
		age = int(input ("How old is "+name+"?"))	

		#Procedure

		if age < 7:
			print (name, "should go to bed at 6pm")
			time.sleep(5)
		elif age <11:
			bedtime = age - 1
			print (name, "should go to bed at",str(bedtime))
			time.sleep(5)
		else:
			print (name, "can go to bed at 10pm")
			time.sleep(5)
	