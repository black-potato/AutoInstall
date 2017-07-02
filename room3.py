class room3(object):
    def guess(self):
        print "Welcome to room3"
        print "You have two choices,\n\tthrow the bomb\n\tslowly place the bomb"
        action = raw_input("> ")
        if action == "throw the bomb":
            return 'death'
        elif action == "slowly place the bomb":
            return 'room4'
        else:
            print "DOES NOT COMPUTE!"
            return "room3"