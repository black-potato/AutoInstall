from sys import exit
from random import randint

class room4(object):
    def guess(self):
        print "Welcom to room 4 and it is the last room"
        print "Guess a number from 1 to 5"
        good_pod = randint(1, 5)
        print "Help you to win, the number is %d"%good_pod
        guess = raw_input("[pod #]> ")
        if int(guess) != good_pod:
            return 'death'
        else:
            print " You won!"
            exit(0)