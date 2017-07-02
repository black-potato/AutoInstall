class room1(object):

    def guess(self):
        print "Welcome to room 1"
        print "You have 3 choices:\n\tshoot!\n\tdodge!\n\ttell a joke"
        action = raw_input("> ")
        if action == "shoot!":
            print "die"
            return 'death'
        elif action == "dodge!":
            print "die"
            return 'death'
        elif action == "tell a joke":
            print "Lucky,go to room2"
            return 'room2'
        else:
            print "DOES NOT COMPUTE!"
            return 'room1'