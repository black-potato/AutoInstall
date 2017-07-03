from room1 import *
from room2 import *
from room3 import *
from room4 import *
from death import *

class game(object):
    def __init__(self,start):
        print "It's an interesting game!"
        self.start = start
        # obj_room1= room1()
        # obj_room2= room2()
        # obj_room3= room3()
        # obj_room4= room4()
        # obj_death= death()
        # self.map={"room1":obj_room1,
        #           "room2":obj_room2,
        #           "room3":obj_room3,
        #           "room4":obj_room4,
        #           "death":obj_death
        #           }
        self.map={"room1":room1(),
                  "room2":room2(),
                  "room3":room3(),
                  "room4":room4(),
                  "death":death()
                  }
    def play(self):
        obj_next= self.map[self.start]
        while True:
#             class_method = getattr(obj_next,'guess')
#             index_next = class_method()
            index_next = obj_next.guess()
            obj_next = self.map[index_next]
a_game=game('room1')
a_game.play()