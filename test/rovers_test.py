import unittest

from mars_rovers.rovers import Rovers

class roversTest(unittest.TestCase):



    def test_spin_left(self):
        rovers = Rovers("1 2 N")
        rovers.spin_left()
        self.assertEqual("W",rovers.direction)

    def test_spin_right(self):

        rovers = Rovers("1 2 N")
        rovers.spin_right()
        self.assertEqual("E",rovers.direction)

    def test_move_forward(self):

        rovers = Rovers("1 2 N")
        rovers.move_forward()
        self.assertEqual(3, rovers.y)

    def test_move_to_destination(self):
        rover = Rovers("3 3 E")
        rover.move_to_destination("MMRMMRMRRM")
        self.assertEqual("5 1 E",""+str(rover.x)+" "+str(rover.y)+" "+rover.direction+"")


