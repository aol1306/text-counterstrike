#!/usr/bin/python
import random
import time

uname_id = 0
pwner_id = 0
score = 0

def random_id():
	return random.randint(1,99)

try:
	print "Welcome to text-only Counter-Strike! (created by 1306 - aol1306.pl)"
	print "Choose your nick:"
	uname = raw_input()
	print "Your nick is: %s" % uname

	while True:
		print "What do you want to do, %s?" % uname
		raw_input()
		time.sleep(1)
		print "You see an enemy!"
		print "What do you want to do, %s?" % uname
		raw_input()
		
		# find pwner id
		pwner_id = random_id()
		while pwner_id == uname:
			pwner_id = random_id()
	
		time.sleep(1)
		print "You have been pwned by user_%d" % pwner_id
		score -= 1
		time.sleep(1)
		print "Time for another round!"
		print "Your score = %d" % score
		time.sleep(1)
		print
except KeyboardInterrupt:
	print
	print "See you later!"
