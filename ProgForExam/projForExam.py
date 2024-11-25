"""
Task 1: Data Types, Input/Output, Arithmetic Operations, and the math

Module A rescuer must reach a drowning person as quickly as possible to prevent his death. 
Since the rescuer is on the shore and the drowning person is in the water, the rescuer must 
cover part of the distance on the sand and the rest by swimming. The direction of movement 
chosen by the rescuer determines the total distance he must cover, since the speed of movement 
in the water is less than the speed of movement on land by a certain constant value. 
You need to write a program that would calculate the time it takes the rescuer to reach the drowning person. 
The notations used and the geometric construction illustrating the problem are shown in Figure 1.


"""

import math

# 1. input d1 in yards
d1 = float( input("Enter the shortest distance from the lifeguard to the water's edge, 𝑑1 (in yards): " ) ); 
d1 = 8;
d1 = d1 * 3 / 5280;
# 2. input d2 in feet
d2 = float( input("Enter the shortest distance from a drowning person to the shore, 𝑑2 (in feet): " ) );
d2 = 10;
d2 = d2 / 5280;
# 3. input h in yards
h = float( input("Enter the lateral offset between the rescuer and the drowning person, ℎ (in yards): " ) );
h = 50;
h = h * 3 / 5280;
# 4. input v_sand in mph 
v_sand = float( input("Enter the speed of the rescuer on the sand, v_sand (mph): " ) );
v_sand = 5;
v_sand = 5 / 3600;
# 5. input n
n = float( input("Enter the deceleration coefficient of the rescuer when moving in water, n : ") );
n = 2;
# 6. input theta1 in (degrees)
theta1 = float( input("Enter the direction of the rescuer's movement on the sand, theta1 (degrees): ") );
theta1 = 39.413;
theta1_rad = math.radians(theta1);

print('\n\nd1 = ', d1 , 'in miles');
print('d2 = ', d2 , 'in miles');
print('h = ', h, 'in miles');
print('v_sand = ', v_sand, 'in mph');
print('n = ', n);
print('theta1_rad = ', theta1, 'in radians');


x = d1 * math.tan(theta1_rad);

L1 = math.sqrt( math.pow(x,2) + math.pow(d1, 2));
L2 = math.sqrt( math.pow((h-x),2) + math.pow(d2, 2));

t = 1/v_sand*(L1+n*L2);


#print('\n\ntime = ', t);

print(f'\n\nIf the rescuer starts moving at an angle theta1 equal to {int(theta1)} degrees, \nhe will reach the drowning person in {round(t,1)} seconds\n\n\nThank you.');


"""
filename = "chipmunk.jpg"
im = Image.open(filename)

print('\n********************')
print("Here's the information about", filename)
print(im.format, im.size, im.mode)

gray_im = im.convert('L')
scaled = gray_im.resize((128, 128))
print("After converting to gray scale and resizing,")
print("the image information has changed to")
print(scaled.format, scaled.size, scaled.mode)

scaled.show()
scaled.save(filename + "_scaled.jpg")
"""