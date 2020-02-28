"""
Calculate resistor values to use in parallel
"""
import numpy as np
dtype = np.longdouble


def parallel_res(a, b):
        if (a==0):
                return b
        if (b==0):
                return a
        x = 1.0/a + 1.0/b
        return 1.0/x


#Initalize arrays with the resistor values and multipliers
ten_tol = np.array([ 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82], dtype=dtype)
multiplier = np.array([0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000], dtype=dtype)

#Initalize empty array for all the possible resistors
ten_values = np.zeros(109, dtype=dtype)

#Change these two values!
goal_val = 100
goal_tolerance = 0.01 #default at 1%
print("Finds the resistor combos to get the desired resistance within 1%")
print("What is your desired resistance?")
goal_val = float(input())

print("What is your desired tolerance value?")
goal_tolerance = float(input())

#Calculate the high and low acceptable values
goal_plus = goal_val +  (goal_val * goal_tolerance)
goal_minus = goal_val - (goal_val * goal_tolerance)

#Calculates all possible resistors
k = 0
for i in range(len(multiplier)):
        for j in range(len(ten_tol)):
                ten_values[k] = multiplier[i] *ten_tol[j]
                k += 1
#print ten_values


#Runs through each possibility and checks tolerance
for i in range(109):
        k =0
        for j in range(109):
                if (j+k < 108):
                        test =  parallel_res(ten_values[i], ten_values[j+k])
