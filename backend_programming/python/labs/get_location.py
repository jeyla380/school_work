#The main program:  p has been defined and code to read in the x and y coordinates (integers) for point p is also provided.

#Instructions:
#1) Output p.
#2) Read in the number of steps the be taken:
    #forwards along the x-axis
    #forwards along the y-axis
    #backwards along both axes every 3rd iteration
#3) Define a dynamic programming algorithm that advances and retreats the required number of steps along the x and y axes and determines the closest point to p. After each iteration, calculate the distance between point p and the current location using the distance function:
#d = sqrt((x_p - x_1)^2 + (y_p - y_1)^2)
#Count the number of iterations.
#4) Output the final arrival point (the point closest to p), the distance between the arrival point and p, and the number of iterations taken.


import math

# Point class
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


# Main program
# Read in x and y for Point P
p = Point()
p.x = int(input())
p.y = int(input())

# Read in num of steps to be taken in X and Y directions
x_steps = int(input())
y_steps = int(input())

# Read in num of steps to be taken (backwards) every 3 steps
backward_steps = int(input())

# Write dynamic programming algorithm
#distance formula = sqrt((x2 - x1)^2 + (y2 - y1)^2)
#origin: (0,0), x forward = x_steps, y forward = y_steps from origin & compare distance of each point to point p 

count = 0 

x1 = 0 #origin
y1 = 0

x2 = p.x
y2 = p.y

first_points = []
point_distances = []

while count <= 10:
    #finds the x1 and y1
    if(count == 0):
        x1 = 0
        y1 = 0
        
    else:
        x1 = x1 + x_steps
        y1 = y1 + y_steps
        
        #every 3rd iteration
        if(count % 3 == 0):
            x1 = x1 - backward_steps
            y1 = y1 - backward_steps
         
                 
    #if the (x2, y2) is bigger than (x1, y1) it switches the x2 and x1 so the distance equation runs properly    
    if((x2 <= x1) and (y2 <= y1)):
        x = x1 - x2
        y = y1 - y2
    else:
        x = x2 - x1
        y = y2 - y1
    
    
    x_squared = x * x
    y_squared = y * y
    
    distance = math.sqrt(x_squared + y_squared)
    
    
    first_points.append(tuple((x1,y1)))
    point_distances.append(distance)
    
    #print("First point: (" + str(x1) + "," + str(y1) + ")") 
    #print("Second point: (" + str(p.x) + "," + str(p.y) + ")") 
    #print("Distance: " + str(distance))
    #print("")
    
    count += 1


closest_distance_index = point_distances.index(min(point_distances))
#print(closest_distance_index)
#print(first_points[closest_distance_index])
#print(point_distances[closest_distance_index])

# Output
print("Point P: (" + str(p.x) + "," + str(p.y) + ")")
print("Arrival point: (" + str(first_points[closest_distance_index][0]) + "," + str(first_points[closest_distance_index][1]) + ")")
print("Distance between P and arrival: {:.6f}".format(point_distances[closest_distance_index]))
print("Number of iterations: " + str(closest_distance_index))
