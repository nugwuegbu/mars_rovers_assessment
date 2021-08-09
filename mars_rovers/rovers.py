####################################
#Mars Rovers Challenge using Python
#By Ugwuegbu Nnamdi
#nugwuegbu089@gmail.com
###################################

#Rovers object characterize by two attributes: position and location defined in cordinates (x,y,z)
#(x,y,z)  x and y are horizontal and vertical coordinates on cartesian plane, z is the direction
#z can be defined as z:direction in {N=North,E=East,W=West,S=South}

#Plateau is a grid where (0,0,N) signifies x=0, y =0, N =North direction
#Instructions L,R,M corresponding Left Spin , Right Spin and Move Forward

######################  Actions ######
#SpinLeft
#SpinRight
#StepForward
#MoveToLocation or MoveToDestination
######################################


from dataclasses import dataclass
from re import match


@dataclass
class Rovers():

    #initialize position
    x = 0
    y = 0
    direction = "N"

    def __init__(self,location):
        #split by whitespace
        location = location.split()

        self.x = int(location[0])
        self.y = int(location[1])
        self.direction = location[2]

    def spin_left(self):

        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "W":
            self.direction = "S"
        else:
            raise ValueError(" bad input , only values in set {N,W,S,E} allowed")



    def spin_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "W":
            self.direction = "N"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"
        else:
            raise ValueError(" bad input , only values in set {N,W,S,E} allowed")


    def move_forward(self):

        if self.direction == "N":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1
        else:
            raise ValueError(" bad input , only values in set {N,W,S,E} allowed")



    def move_to_destination(self,instructions_stream):
        #Rover's  series of instructions of how to move e.g LMLMLMLMM designated instructions_stream
        # rover_instruction = []
        # rover_instruction = list(instructions_stream)

         #loop through L,R,M in instruction
        for i in range(len(instructions_stream)):
            if instructions_stream[i] == "L":
                self.spin_left()
            elif instructions_stream[i] == "R":
                self.spin_right()
            elif instructions_stream[i] == "M":
                self.move_forward()

            else:
                raise ValueError("illegal argument")
            # print(instructions_stream[i])



