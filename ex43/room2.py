from random import randint

class room2(object):
    def guess(self):
        print "Good job!Now you get access to room2"
        print "Get the bomb. The code is 3 digits."
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = raw_input("[keypad]> ")
        guesses = 0
        print "I'll tell you a secret %s" %code
        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
        if guess == code:
           print "Con! you get the code! "
           return 'room3'
        else:
            print "die"
            return 'death'