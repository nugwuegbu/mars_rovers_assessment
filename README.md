# mars_rovers_assessment

#This project is a simple package for solving the Mars Rovers challenge when landed on a rectangular plateau.
                       
                     Challenge
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which
is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get
a complete view of the surrounding terrain to send back to Earth. A rover’s position and location
is represented by a combination of x and y co- ordinates and a letter representing one of the
four cardinal compass points. The plateau is divided up into a grid to simplify navigation.
An example position might be 0, 0, N, which means the rover is in the bottom left corner and
facing North.In order to control a rover, NASA sends a simple string of letters. The possible
letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively,
without moving from its current spot. ‘M’ means move forward one grid point, and maintain the
same Heading. Assume that the square directly North from (x, y) is (x, y+1).
INPUT:
The first line of input is the upper-right coordinates of the plateau, the lower- left coordinates are
assumed to be 0,0. The rest of the input is information pertaining to the rovers that have been
deployed. Each rover has two lines of input. The first line gives the rover’s position, and the
second line is a series of instructions telling the rover how to explore the plateau. The position is
made up of two integers and a letter separated by spaces, corresponding to the x and y
coordinates and the rover’s orientation. Each rover will be finished sequentially, which means
that the second rover won’t start to move until the first one has finished moving.
OUTPUT:
The output for each rover should be its final coordinates and heading.
INPUT AND OUTPUT:
Test Input:
5 5
1 2 N
L M L M L M L M M
3 3 E
M M R M M R M R R M
Expected Output:
1 3 N
5 1 E

            Solution and Approach
In this solution I have first extracted all the objects in the questions so as to implement classes and behaviors of the objects and also ensure seperation of concern
#The major objects here are
1. Rovers
2. Plateau
3. location
4. instructions

#The major attributes in this are :
1. coordinates x and y
2. Directions N,W,S,E
3. instruction letters; L,R,M

#Behaviors

1. SpinLeft
2. SpinRight
3. MoveForward
4. MoveToDestination

#Implementation
I have used TDD to ensure that tests perspectives are included along developemnt and also aid code reference and usage in the future

#Structure
1. mars_rovers module which can be imported into your project in order to use the methods in the class Rovers
2. test 

#Requirements
Python 3.5 and later versions have been tested to work.