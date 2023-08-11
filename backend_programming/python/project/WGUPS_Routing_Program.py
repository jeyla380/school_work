#!/usr/bin/env python
# coding: utf-8

# # WGUPS Routing Program
# 
# <hr>
# 
# ### Scenario:
# The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has **three trucks**, **two drivers**, and **an average of 40 packages to deliver** each day. Each package has specific criteria and delivery requirements.
# 
# Your task is to determine an algorithm, write code, and present a solution where all 40 packages (listed in the attached “WGUPS Package File”) will be delivered on time while meeting each package’s requirements and **keeping the combined total distance traveled under 140 miles for both trucks**. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you made while writing your scripts.
# 
# Keep in mind that the supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has been delivered and at what time the delivery occurred.
# 
# 
# ### Assumptions:
# - Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
# - The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
# - There are no collisions.
# - Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
# - Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 
# - The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).
# - There is up to one special note associated with a package.
# - The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
# - The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.
# - The day ends when all 40 packages have been delivered.
# 
# **EOD = End of Day
# 

# <br>
# 
# ## A. Identify a Self-Adjusting Algorithm
# <hr>

# I chose the Nearest Neighbor algorithm to help optimize the delivery time by finding the nearest addresses. The algorithm will essentially go through the list of all addresses (starting at Western Governors University as the HUB), compare the distances, and find all the unvisited nearest neighbors. It will repeat this process until all addresses have been visited.

# <br>
# 
# ## B. Overview of Program
# <hr>

# ### 1. Nearest Neighbor Algorithm Logic Through Psuedocode

# This program will find the nearest location (based on mileage) to find the quickest route for each truck. A function is created to allow the flexibility to insert data based on each truck.

# ``` 
# START
# 
# Function best path for each truck
#     
#     Pass In: Truck dictionary, 
#              Truck distances,
#              Truck csv (DataFrame of truck distances),
#              Truck pathway (empty list for addresses),
#              Truck address miles (miles between each location)
#     
#     
#     Number of addresses:= length of (Truck csv)
#     Visited?:= [List of "False"] * Number of addresses
#     Path:= [Empty List]
#     Distance:= 0
#     Current location:= 0
#     
#     Current location is added to [Path List]
#     Current location in Visited? is TRUE
#     
#     
#     WHILE length of (Path) < Number of addresses
#         Nearest address is None
#         Nearest distance is infinity
#         
#         
#         FOR variable X in the range of (Number of addresses)
#         
#         
#             IF variable X of Visited? is FALSE
#                 Distance:= Float(variable X of Current location of Distance)
#                 
#                 
#                 IF Distance < Nearest distance
#                     Nearest address:= variable X
#                     Nearest distance:= Distance
#                 
#                 ENDIF
#             
#             ENDIF
#         
#         ENDFOR
#         
#         Nearest distance is added to [Truck address miles List]
#         Current location:= Nearest address
#         Current location is added to [Path List]
#         Current location in Visited? is TRUE
#         
#     ENDWHILE
#     
#     Distance:= the sum of Truck address miles rounded to one decimal
#     Float(Path's 0 index of Path's last index of Distance) is added to [Truck address miles List]
#     
#     
#     Name of location:= [Empty List]
#     
#     FOR Column name of Truck csv's column values
#         Column name is added to [Name of location List]
#     
#     ENDFOR
#     
#     
#     FOR variable X in Path
#         Pathway address name:= variable X of Name of location
#     
#     ENDFOR
#     
#     
#     FOR both variable X and variable Y of both Path and Pathway address name
#         variable Y is added to [Truck pathway List]
#     
#     ENDFOR
#     
#     
#     Pass Out: Truck address miles
#               Truck pathway
#               
#               PRINT "Optimized Truck Path: Path"
#               
#               PRINT "Total Distance: Distance"
#               
#               PRINT "Best Path for Truck:"
#               PRINT "Location of variable X in Path - variable Y of Pathway address name"
# 
# Endfunction
# 
# END
# 
# ```

# ### 2. Programming Environment for Project

# The programming environment I used is Jupyter Notebook as it allows me to split up my code (but still allows it to run properly) and visualize the code I've programmed. It also is very easy to read as either a `.ipynb` or `.pdf`, but can also be transferred and saved as a `.py` file.

# ### 3. Evaluate Space-Time Complexity in Entire Program

# This will be broken down by each section and then the overall program.
# 
# - **Part C: O(n) + O(1) = O(n)**
#     - The first section contains the `WGUPS_Package_File.csv` and the `WGUPS_Distance_Table.csv`. The first file `WGUPS_Package_File.csv` time complexity is O(1) due to the fact the variables being assigned are fixed, while `WGUPS_Distance_Table.csv` time complexity is O(n) + O(1), which is O(n) because the operation is repeated with for-loop n times.
#     - The second section of Part C is filling in the missing values. The time complexity for this second section is O(n2) because the operation contains a nested for-loop.
# - **Part E: O(n) + O(n2) + O(1) + O(n2) + O(n2) = O(n2)**
#     - The class Hash Table has functions within that are all O(1) with the exception of the print function. The print function contains a for-loop which means the content within isn't fixed (the variables will change with each iteration). This means that the Hash Table is O(n) + O(1) = O(n)
#     - The first part of the second section involves loading the trucks manually, which contains changing variables. This means that manually loading the truck is O(n). The second part contains code for each truck (not a function, but has the ability to be) that takes the Hash Table data, and turns it into a dictionary that is easy to read and pull data from. The code's time complexity is: O(n) + O(n2) + O(n2) + O(n) + O(n) + O(n) = O(n2).
#     - The `.csv` files created for each individual truck is O(1) as the variables are fixed.
#     - The Nearest Neighbor Algorithm is a function (not the code underneath the image) that is intended to take the length of the truck `.csv` file, then take the indexes of the length and run it through the algorithm to determine the nearest neighbors for each truck. With doing so, the time complexity is O(n2).
#     - The function created to get the packages sent out and delivered to each location contains variables that are not fixed, they go through at least two for-loops, which mean the function's time complexity is O(n2).
# - **Part F: O(n2)**
#     - The look up function relies on the user input to find the package they want. To create this function, it involves a while-loop, a for-loop, and multiple if-else statements. This means that this function is O(n2).
# - **Part G: O(n4)**
#     - This function is the most complex as it requires taking data from previous functions and extracting a dictionary from a dictionary, and extracting the data from there. This function's time complexity is O(n4).
#     
# The overall time complexity of the entire program is **O(n4)**, also known as a Polynomial Time Complexity.

# ### 4. Adaptability

# Both the self-adjusting algorithm (Nearest Neighbor) and the self-adjusting data structure (Hash Table) are both fairly scalable. The algorithm shouldn't have any issue being able to compile and run additional data as the algorithm takes the location data from the packages to run. The data structure ideally shouldn't have any issues, but it depends on the information of the packages. Truck one takes packages that need to be delivered by 10:30am (more specifically 9:00am and 10:30am), truck two and truck three have the packages divided between them (unless the packages suggest specific trucks) by having truck two contain the rest of the even packages, and truck three containing the odd. Therefore, with the self-adjusting data structure, there may be some trucks that contain a lot more packages than the others.

# ### 5. Software Efficiency and Maintainability

# The time complexity of the entire program is a Polynomial Time Complexity. For more detail about this, please reference Section 3 above.
# 
# The program is also fairly easy to maintain, especially the bottom half where most of the program uses functions that pass in certain variables. However, the upper half of the program may be a bit more difficult as the upper half focuses on separating the packages based on each truck as well as making the package information easier to pull data from; so the upper half of the program does not involve functions. This means that if anything ever has to be repaired, the upper part of the program will need to checked over to ensure everything ties in correctly as compared to the bottom half.

# ### 6. Strengths and Weaknesses of Self-Adjusting Data Structures

# **Strengths:**
# 1. One of the most important strengths of a self-adjusting data structure is that it's self-adjusting. This theoretically means more (or less) data can be integrated with the data structure and will still work regardless as it's able to adjust to the different amount of variables.
# 2. Both the key, and the value of the data structure can contain different types of data types such as strings, integers, floats, etc., including lists (but lists can only be a value, not key).
# 
# 
# **Weaknesses:**
# 1. Collisions can occur if there are multiple keys that are the same variable which would cause multiple values to be constantly overwritten until the last key (of the same variable) occurs.
# 2. If the size of the data structure is too small, multiple variables will be moved into a single bucket causing the efficiency of the self-adjusting data structure to worsen.

# <br>
# 
# ## C. Write Program to Deliver All Packages
# <hr>

# ### 1. Organize and Read Files

# In[2]:


import pandas as pd
pd.set_option('display.max_colwidth', 0)

import re
import math
import datetime
import itertools
import copy
from dateutil import parser


# #### WGUPS Package File

# In[3]:


package_file = pd.read_csv('WGUPS_Package_File.csv')
package_file.head(10)


# When viewing `WGUPS_Package_File.csv`, it is completely unorganized and untidy. Therefore, the `.csv` needs to be fixed so the data can be used properly.
# - Remove unnecessary titles.
# - Replace column names from NaN.
# - Remove columns titled as NaN (but not all columns that contain NaN).
# - Rename columns so `\n` is removed.

# In[4]:


#remove unnecessary titles
new_package_file = package_file.iloc[6:]
new_package_file = new_package_file.reset_index(drop = True)

#replace column names from NaN
new_package_file.columns = new_package_file.iloc[0]


# In[5]:


new_package_file = new_package_file.iloc[1:]


# In[6]:


#remove columns titled as NaN
new_package_file = new_package_file.dropna(axis = 1, how = 'all')

#rename columns
new_package_file = new_package_file.rename(columns = {'Package\nID': 'Package ID', 
                                   'Delivery\nDeadline': 'Delivery Deadline', 
                                   'Mass\nKILO': 'Mass KILO', 
                                   'page 1 of 1PageSpecial Notes': 'Special Notes'})

#remove any whitespace
new_package_file.columns = new_package_file.columns.str.strip()


# In[7]:


#organized WGUPS_Package_File.csv
new_package_file.head(40)


# #### WGUPS Distance File

# In[8]:


distance_file = pd.read_csv('WGUPS_Distance_Table.csv')
distance_file.head(10)


# The `WGUPS_Distance_Table.csv` is unorganized (similar to `WGUPS_Package_File.csv`), and needs to be cleaned and organized.
# - Remove unnecessary titles.
# - Replace column names from NaN.
# - Remove NaN column (2nd column).
# - Remove columns titled as NaN (but not all columns that contain NaN).
# - Rename columns and rows so `\n` is removed.

# In[9]:


#remove unnecessary titles
new_distance_file = distance_file.iloc[6:]
new_distance_file = new_distance_file.reset_index(drop = True)

#replace column names from NaN
new_distance_file.columns = new_distance_file.iloc[0]
new_distance_file = new_distance_file.iloc[1:]


# In[10]:


#remove second column
new_distance_file = new_distance_file.drop(new_distance_file.columns[1], axis = 1)


# In[11]:


new_distance_file.head()


# In[12]:


column_names = list(new_distance_file.columns.values)
new_column_names = []

#O(n) + O(1)
for names in column_names:
    if "\n " in names:
        new_column_names.append(names.replace("\n ", " "))
    else:
        new_column_names.append(names.replace("\n", " "))
print(new_column_names)


# In[13]:


#rename columns so `\n` is removed
new_distance_file.columns = new_column_names


# In[14]:


new_distance_file = new_distance_file.rename(columns = {'Western Governors University 4001 South 700 East,  Salt Lake City, UT 84107': 
                                                        'Western Governors University 4001 South 700 East'})


# In[15]:


#rename rows so `\n` is removed
row_names = list(new_distance_file['DISTANCE BETWEEN HUBS IN MILES'])
new_row_names = []

#O(n) + O(1)
for names in row_names:
    if "\n " in names:
        new_row_names.append(names.replace("\n ", " "))
    else:
        new_row_names.append(names.replace("\n", " "))
print(new_row_names)


# In[16]:


new_distance_file['DISTANCE BETWEEN HUBS IN MILES'] = new_row_names


# In[17]:


new_distance_file['DISTANCE BETWEEN HUBS IN MILES'].replace({'Western Governors University 4001 South 700 East,  Salt Lake City, UT 84107': 
                                                        'Western Governors University 4001 South 700 East'}, inplace = True)


# In[18]:


new_distance_file = new_distance_file.set_index(['DISTANCE BETWEEN HUBS IN MILES'])


# In[19]:


new_distance_file.head()


# In[20]:


distance_file_csv = new_distance_file


# In[21]:


new_distance_file = new_distance_file.to_numpy()


# ### 2. Fill in the `NaN` and Replace Values

# In[22]:


print(new_distance_file)


# In[23]:


new_row = []

#O(n^2)
#goes through each list in new_distance_file (total of 27)
for i in range(0, len(new_distance_file)):
    #print(i)
    #goes through each number in each list and adds to new_row list
    for row in new_distance_file:
        new_row.append(row[i])
    #each list will become the new_row list, and then the new_row list is cleared so it's empty for the next loop
    new_distance_file[i] = new_row
    new_row.clear()


# In[24]:


print(new_distance_file)


# In[25]:


distance_file_csv[:] = new_distance_file


# In[26]:


distance_file_csv.head()


# <br>
# 
# ## D. Identify a Self-Adjusting Data Structure
# <hr>

# I chose to create a hash table for creating the packages (key), and the information that comes with it (value). However, after separating and loading the packages into the different trucks, I created dictionaries and loaded the package ID as the key and the rest of the information as a list, which was the value. The dictionaries I used for each truck were then used for the Nearest Neighbor Algorithm.

# ### 1. Explain the Data Structure

# The Hash Table is able to store the package information by adding it to a bucket using a calculated index (there may be multiple packages in a bucket, but it depends on the size of the array). The `key` is the first value, and `value` is the second value after choosing an object.
# 
# ```
# hashtable = HashTable()
# hashtable.add(key, value)
# ```
# 
# In this program, the key and value of the Hash Table houses the package information. The package ID is the key, and the rest of the data is put into a list for the value. Each truck was also created as an object to house the Hash Table for the packages, which are manually loaded onto each truck.
# 
# ```
# truckone = HashTable()
# trucktwo = HashTable()
# truckthree = HashTable()
# ```
# 
# The Hash Table gives the option of printing the data, or searching for the data. Due to the size of the array used, there were multiple packages in one bucket (or essentially a list within a list). The print function doesn't pass in anything, so it's easier to view the packages. For example, by printing `item[x][y][z]` when there are three lists within a list would allow each package to be viewed. 
# 
# The search function essentially does the same thing as the print function, but passes in the package's ID (i.e 20, 1, 5) as the key. However, the difference from printing is that it doesn't look as nice when printed out, so the code after manually loading the truck is able to take the information from the Hash Table and organize it into a form that is easy to read and pull data from. Essentially the Hash Table simply holds the data until it is transformed and placed into a readable data structure.

# <br>
# 
# ## E. Hash Table
# <hr>

# ### 1. Create the Hash Table & Package Class

# In[27]:


class Package:
    
    #initialize the Truck
    def __init__(self, ID, address, delivery_deadline, weight_in_kilo, status, loaded_at, delivered_at):
        self.ID = ID
        self.address = address
        self.delivery_deadline = delivery_deadline
        self.weight_in_kilo = weight_in_kilo
        self.status = status
        self.loaded_at = loaded_at
        self.delivered_at = delivered_at
        
    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.address, self.delivery_deadline, self.weight_in_kilo, 
                                   self.status, self.loaded_at, self.delivered_at)


# In[118]:


#NEED TO FIX

class HashTable:
    
    #initialize the hashtable
    def __init__(self):
        #size of the array
        self.size = 48
        #array, sets each cell to [None]
        self.map = [None] * self.size

        
    #calculates index of key
    def _get_hash(self, key):
        hash = 0
        
        for character in str(key):
            #ord() is the unicode of the character(s) in the key
            hash = hash + ord(character)
        #returns the index
        return hash % self.size
    
    
    def add(self, key, value):
        key_index = self._get_hash(key)
        key_value = [key, value]
        
        #adds to the list if empty
        if self.map[key_index] is None:
            #at the index, the key, value pair is added
            self.map[key_index] = list([key_value])
            return True
        #if the list isn't empty
        else:
            #check if key already exists
            for pair in self.map[key_index]:
                #if key exists, update the value
                if pair[0] == key:
                    pair[1] = value
                    return True
            #if the key doesn't exist, add the new key, value pair to list
            self.map[key_index].append([key_value])
            return True
    

    #gets the value of the key that was searched
    def search_value(self, key):
        key_index = self._get_hash(key)
        
        #locate the cell of list/array when not empty
        if self.map[key_index] is not None:
            #for pair in self.map[key_index]:
                #finds the value that matches the key
                #if pair[0] == key:
                    #return pair[1]
                    
            if len(self.map[key_index]) == 1:
                return self.map[key_index][0][1]
            elif len(self.map[key_index]) == 2:
                return [self.map[key_index][0][1], self.map[key_index][1][0][1]]
            else:
                return [self.map[key_index][0][1], self.map[key_index][1][0][1], self.map[key_index][2][0][1]]
        
        #if the cell is empty, return None
        return None
    
    
     #gets the key that was searched
    def search_key(self, key):
        key_index = self._get_hash(key)
        
        if self.map[key_index] is not None:
            
            if len(self.map[key_index]) == 1:
                return self.map[key_index][0][0]
            elif len(self.map[key_index]) == 2:
                return [self.map[key_index][0][0], self.map[key_index][1][0][0]]
            else:
                return [self.map[key_index][0][0], self.map[key_index][1][0][0], self.map[key_index][2][0][0]]
            
        
            #for i in range(len(self.map[key_index])):
                #return self.map[key_index][i]
                
            #if len(self.map[key_index]) == 1:
            #    for i in range(len(self.map[key_index])):
             #       return self.map[key_index][i][0]
                #return self.map[key_index][0][0]
            
            #elif len(self.map[key_index]) == 2: #[1] is replacing [0] data, need to make it so when returning, 
                                                #[1] doesn't replace [0]
              #  for i in range(len(self.map[key_index])):
               #     if self.map[key_index][i][0] == self.map[key_index][1][0]:
                 #       continue
                #    else:
                #        return self.map[key_index][1][0][0]
            #else:
            #    for i in range(len(self.map[key_index])):
             #       if self.map[key_index][0]:
              #          return self.map[key_index][0][0]
               #     elif self.map[key_index][1]:
                #        return self.map[key_index][1][0][0]
                 #   else:
                  #      return self.map[key_index][2][0][0]
            
            
        return None
    
            
    
    def print(self):
        #prints out every cell that isn't empty
        #O(n)
        for item in self.map:
            if item is not None:
                if len(item) == 1:
                    print(str(item[0]))
                    print()
                elif len(item) == 2:
                    print(str(item[0]))
                    print(str(item[1][0]))
                    print()
                else:
                    print(str(item[0]))
                    print(str(item[1][0]))
                    print(str(item[2][0]))
                    print()


# After creating a HashMap (in this case a HashTable), the data from the `WGUPS_Package_File.csv` can be added into the HashTable to organize the data based on key, value sets. For this program, the "Package ID" will be the key, while the rest of the data: `["Address", "City", "State", "Zip", "Delivery Deadline", "Mass KILO"]` will be the value due to the `Package` class.
# 
# **"Delivery Status" will be added to the Package class

# In[29]:


hashtable = HashTable()

#O(n)
for index, row in new_package_file.iterrows():
    p_ID = row['Package ID']
    p_address = row['Address']
    p_delivery_deadline = row['Delivery Deadline']
    p_weight = row['Mass KILO']
    p_status = 'LOADED ON TRUCK - IN HUB'
    p_loaded_at = datetime.time(8)
    p_delivered_at = datetime.time(0)
    
    p = Package(p_ID, p_address, p_delivery_deadline, p_weight, p_status, p_loaded_at, p_delivered_at)
    #print(p)
    
    hashtable.add(p_ID, p)
hashtable.print()


# ### 2. Load the Trucks

# Now that the HashTable function works properly, the trucks can now be loaded manually with the data. Let's separate the boxes by putting 20 boxes in one truck, and 20 boxes in the other truck.
# 
# Remember the assumptions:
# - Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
# - The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
# - There are no collisions.
# - Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
# - Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 
# - The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).
# - There is up to one special note associated with a package.
# - The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
# - The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.
# - The day ends when all 40 packages have been delivered.
# 
# Also, remember the Special Notes:

# In[30]:


for index, row in new_package_file.iterrows():
    if str(row['Special Notes']) != "nan":
        print("Package " + str(row['Package ID']) + ": " + str(row['Special Notes']))


# In[31]:


for index, row in new_package_file.iterrows():
    print("Package " + str(row['Package ID']) + ": " + str(row['Delivery Deadline']))


# In[32]:


#separate the boxes and add them into the separate trucks (hashtables)
truck_one = HashTable()
truck_two = HashTable()
truck_three = HashTable()

#O(n)
#range needs to start at 1 and end at 40 since package ID goes from 1-40
for i in range(1, len(new_package_file) + 1):
    new_package_file['Package ID'][i] = int(new_package_file['Package ID'][i])
    
    p_ID = new_package_file['Package ID'][i]
    p_address = new_package_file['Address'][i]
    p_delivery_deadline = new_package_file['Delivery Deadline'][i]
    p_weight = new_package_file['Mass KILO'][i]
    p_status = 'LOADED ON TRUCK - IN HUB'
    p_loaded_at = datetime.time(8)
    p_delivered_at = datetime.time(0)
    
    p = Package(p_ID, p_address, p_delivery_deadline, p_weight, p_status, p_loaded_at, p_delivered_at)
    #print(p)
    
    if new_package_file['Delivery Deadline'][i] == "10:30 AM" or new_package_file['Delivery Deadline'][i] == "9:00 AM": #14 packages in truck one
        
        np_ID = new_package_file['Package ID'][i]
        np_address = new_package_file['Address'][i]
        np_delivery_deadline = new_package_file['Delivery Deadline'][i]
        np_weight = new_package_file['Mass KILO'][i]
        np_status = "LOADED ON TRUCK - IN HUB"
        np_loaded_at = datetime.time(9, 5)
        np_delivered_at = datetime.time(0)
                
        np = Package(np_ID, np_address, np_delivery_deadline, np_weight, np_status, np_loaded_at, np_delivered_at)
        
        
        if new_package_file['Package ID'][i] == 6 or new_package_file['Package ID'][i] == 25:
            truck_three.add(np_ID, np)
        
        else:
            truck_one.add(p_ID, p)
    
    else: 
        if new_package_file['Package ID'][i] != truck_one.search_key(i):
            
            np_ID = new_package_file['Package ID'][i]
            np_address = new_package_file['Address'][i]
            np_delivery_deadline = new_package_file['Delivery Deadline'][i]
            np_weight = new_package_file['Mass KILO'][i]
            np_status = "LOADED ON TRUCK - IN HUB"
            np_loaded_at = datetime.time(9, 5)
            np_delivered_at = datetime.time(0)
                
            np = Package(np_ID, np_address, np_delivery_deadline, np_weight, np_status, np_loaded_at, np_delivered_at)
            
            if new_package_file['Package ID'][i] == 9:
                truck_three.add(np_ID, np)
            elif new_package_file['Package ID'][i] == 25:
                truck_three.add(np_ID, np)
            elif new_package_file['Package ID'][i] == 28:
                truck_three.add(np_ID, np)
            elif new_package_file['Package ID'][i] == 30:
                truck_three.add(np_ID, np)
            elif new_package_file['Package ID'][i] == 31:
                truck_three.add(np_ID, np)
            elif new_package_file['Package ID'][i] == 32:
                truck_three.add(np_ID, np)
            elif new_package_file['Package ID'][i] == 3:
                truck_two.add(p_ID, p)
            elif new_package_file['Package ID'][i] == 18:
                truck_two.add(p_ID, p)
            elif new_package_file['Package ID'][i] == 36:
                truck_two.add(p_ID, p)
            elif new_package_file['Package ID'][i] == 38:
                truck_two.add(p_ID, p)
            elif new_package_file['Package ID'][i] == 19:
                truck_one.add(p_ID, p)
            else:
                if new_package_file['Package ID'][i] % 2 == 0:
                    truck_two.add(p_ID, p) 
                else:
                    truck_three.add(p_ID, p)


# Create a dictionary for each truck to make it easier to keep track of the packages. The key of the packages will be the Package ID, while the values will be a list of the different information.

# #### Truck One

# In[33]:


truck_one_key = []
truck_one_values = []

#O(n)
for i in range(40):
    #print(truck_one.search_key(i))
    #print(truck_one.search_value(i))
    truck_one_key.append(truck_one.search_key(i))
    truck_one_values.append(truck_one.search_value(i))


# In[34]:


truck_one_key_list = []

#O(n2)
for i in range(len(truck_one_key)):
    if truck_one_key[i] != None:
        #checks that truck_one_key[i] is a list
        if isinstance(truck_one_key[i], list):
            #print(truck_one_key[i])
            for j in range(len(truck_one_key[i])):
                #print(truck_one_key[i][j])
                if truck_one_key[i][j] not in truck_one_key_list:
                    truck_one_key_list.append(truck_one_key[i][j])
        else:
            #print(truck_one_key[i])
            if truck_one_key[i] not in truck_one_key_list:
                truck_one_key_list.append(truck_one_key[i])

#print(truck_one_key_list)


# In[35]:


truck_one_values_list = []

#O(n2)
for i in range(len(truck_one_values)):
    if truck_one_values[i] != None:
        #checks that truck_one_values[i] is a list
        if isinstance(truck_one_values[i], list):
            #print(truck_one_values[i])
            for j in range(len(truck_one_values[i])):
                #print(truck_one_values[i][j])
                if truck_one_values[i][j] not in truck_one_values_list:
                    truck_one_values_list.append(truck_one_values[i][j])
        else:
            #print(truck_one_values[i])
            if truck_one_values[i] not in truck_one_values_list:
                truck_one_values_list.append(truck_one_values[i])

#print(truck_one_values_list)


# In[36]:


new_truck_one_values_list = []

#O(n)
for i in range(len(truck_one_values_list)):
    #print(truck_one_values_list[i])
    truck_one_values_list[i] = str(truck_one_values_list[i]).split(", ")
    new_truck_one_values_list.append(truck_one_values_list[i])
    #print(new_truck_one_values_list[i])


# In[37]:


truck_one_dict = {}

#O(n)
for i in range(len(truck_one_values_list)):
    truck_one_dict[truck_one_key_list[i]] = new_truck_one_values_list[i]

#O(n)
for key, value in truck_one_dict.items():
    print(key, value) 
    
truck_one_dict_copy = copy.deepcopy(truck_one_dict)


# In[38]:


#truck_one.print()


# #### Truck Two

# In[39]:


#Truck Two

truck_two_key = []
truck_two_values = []

for i in range(40):
    #print(truck_two.search_key(i))
    #print(truck_two.search_value(i))
    truck_two_key.append(truck_two.search_key(i))
    truck_two_values.append(truck_two.search_value(i))


# In[40]:


truck_two_key_list = []

for i in range(len(truck_two_key)):
    if truck_two_key[i] != None:
        if isinstance(truck_two_key[i], list):
            #print(truck_two_key[i])
            for j in range(len(truck_two_key[i])):
                #print(truck_two_key[i][j])
                if truck_two_key[i][j] not in truck_two_key_list:
                    truck_two_key_list.append(truck_two_key[i][j])
        else:
            #print(truck_two_key[i])
            if truck_two_key[i] not in truck_two_key_list:
                truck_two_key_list.append(truck_two_key[i])
        
#print(truck_two_key_list)


# In[41]:


truck_two_values_list = []

for i in range(len(truck_two_values)):
    if truck_two_values[i] != None:
        if isinstance(truck_two_values[i], list):
            #print(truck_two_values[i])
            for j in range(len(truck_two_values[i])):
                #print(truck_two_values[i][j])
                if truck_two_values[i][j] not in truck_two_values_list:
                    truck_two_values_list.append(truck_two_values[i][j])
        else:
            #print(truck_two_values[i])
            if truck_two_values[i] not in truck_two_values_list:
                truck_two_values_list.append(truck_two_values[i])
        
#print(truck_two_values_list)


# In[42]:


new_truck_two_values_list = []

for i in range(len(truck_two_values_list)):
    #print(truck_two_values_list[i])
    truck_two_values_list[i] = str(truck_two_values_list[i]).split(", ")
    new_truck_two_values_list.append(truck_two_values_list[i])
    #print(new_truck_two_values_list[i])


# In[43]:


truck_two_dict = {}

for i in range(len(truck_two_values_list)):
    truck_two_dict[truck_two_key_list[i]] = new_truck_two_values_list[i]
    
for key, value in truck_two_dict.items():
    print(key, value)
    
truck_two_dict_copy = copy.deepcopy(truck_two_dict)


# In[44]:


#truck_two.print()


# #### Truck Three

# In[45]:


#Truck Three

truck_three_key = []
truck_three_values = []

for i in range(40):
    #print(truck_three.search_key(i))
    #print(truck_three.search_value(i))
    truck_three_key.append(truck_three.search_key(i))
    truck_three_values.append(truck_three.search_value(i))


# In[46]:


truck_three_key_list = []

for i in range(len(truck_three_key)):
    if truck_three_key[i] != None:
        if isinstance(truck_three_key[i], list):
            #print(truck_three_key[i])
            for j in range(len(truck_three_key[i])):
                if truck_three_key[i][j] not in truck_three_key_list:
                    #print(truck_three_key[i][j])
                    truck_three_key_list.append(truck_three_key[i][j])
        else:
            #print(truck_three_key[i])
            if truck_three_key[i] not in truck_three_key_list:
                truck_three_key_list.append(truck_three_key[i])
        
#print(truck_three_key_list)


# In[47]:


truck_three_values_list = []

for i in range(len(truck_three_values)):
    if truck_three_values[i] != None:
        if isinstance(truck_three_values[i], list):
            #print(truck_three_values[i])
            for j in range(len(truck_three_values[i])):
                if truck_three_values[i][j] not in truck_three_values_list:
                    #print(truck_three_values[i][j])
                    truck_three_values_list.append(truck_three_values[i][j])
        else:
            #print(truck_three_key[i])
            if truck_three_values[i] not in truck_three_values_list:
                truck_three_values_list.append(truck_three_values[i])
        
#print(truck_three_values_list)


# In[48]:


new_truck_three_values_list = []

for i in range(len(truck_three_values_list)):
    #print(truck_three_values_list[i])
    truck_three_values_list[i] = str(truck_three_values_list[i]).split(", ")
    new_truck_three_values_list.append(truck_three_values_list[i])
    #print(new_truck_three_values_list[i])


# In[49]:


truck_three_dict = {}

for i in range(len(truck_three_values_list)):
    truck_three_dict[truck_three_key_list[i]] = new_truck_three_values_list[i]
    
for key, value in truck_three_dict.items():
    value[4] = "10:00:00"
    print(key, value)
    
truck_three_dict_copy = copy.deepcopy(truck_three_dict)


# In[50]:


#truck_three.print()


# #### All Trucks

# In[51]:


truck_dict = truck_one_dict | truck_two_dict | truck_three_dict


# In[52]:


for key, value in truck_dict.items():
    print(key, value)


# ### 3. Create a Nearest Neighbor Algorithm

# After creating the hash table, the optimized path of all locations need to be figured out. The Nearest Neighbor Algorithm (similar Greedy Algorithm) can find the unvisited nearest neighbor and go through the list of addresses until they are all visited. However, because we have two trucks that have packages to different addresses, the optimized path of each truck (based on the package's addresses) will need to be optimized and the total path will need to be less than 140 miles.

# ![](WGU_Downtown_Map.png)

# In[53]:


#number of addresses
num_address = len(new_distance_file)
#print(num_address) #it's actually 26 because 'DISTANCE BETWEEN HUBS IN MILES' is considered a column but doesn't do anything

visited = [False] * num_address
destination_opt = []
total_distance = 0


# In[54]:


#start at the first address = WGU
current_address = 0
destination_opt.append(current_address)
visited[current_address] = True

#find the nearest unvisited address and repeat until all addresses have been visited
while len(destination_opt) < num_address:
    nearest_address = None
    nearest_distance = math.inf
    
    #find the nearest unvisited address
    for a in range(num_address):
        if not visited[a]:
            distance = float(new_distance_file[current_address][a])
            if distance < nearest_distance:
                nearest_address = a
                nearest_distance = distance
                
    #move to nearest address
    current_address = nearest_address
    destination_opt.append(current_address)
    visited[current_address] = True
    total_distance = total_distance + nearest_distance
    
#complete the series by returning back to start address
#destination_opt.append(0)
total_distance = total_distance + float(new_distance_file[current_address][0])


# In[55]:


#print("Optimized Path: " + str(destination_opt)) #will need to add 0 (WGU) at the end since we want to go back go Hub
#print("Total Distance: " + str(total_distance) + " miles")


# In[56]:


address_name = []
for column_name in distance_file_csv.columns.values:
    address_name.append(column_name)
    
#for i in range(len(address_name)):
    #print("Node " + str(i) + " - " + address_name[i])


# In[57]:


## order the addresses based on the optimized list
opt_address = [address_name[i] for i in destination_opt]
#print(opt_address)


# In[58]:


#print("Optimized Path + Locations: \n")

#for (opt, a) in zip(destination_opt, opt_address):
    #print("Node " + str(opt) + " - " + a)


# This would be the optimized path if there was just one truck, but that would take to much time and we wouldn't be able to get all the packages delivered by EOD.

# Now we can work on optimizing the path for all three trucks: Truck One, Truck Two, and Truck Three, since we can see that the Nearest Neighbor Algorithm works properly. In order to do this, each truck variable will be a copy of the `distance_file_csv`, and from there remove any columns (addresses) that are not in the specific variable's dictionary.

# #### Truck One Data

# In[59]:


truck_one_csv = distance_file_csv.copy()
#truck_one_csv.head()


# In[60]:


truck_one_csv.drop(truck_one_csv.columns[[1, 3, 7, 8, 9]], axis = 1, inplace=True)
truck_one_csv = truck_one_csv.drop(truck_one_csv.index[[1, 3, 7, 8, 9]])


# In[61]:


truck_one_csv.drop(truck_one_csv.columns[[5, 6, 8, 9]], axis = 1, inplace=True)
truck_one_csv = truck_one_csv.drop(truck_one_csv.index[[5, 6, 8, 9]])


# In[62]:


truck_one_csv.drop(truck_one_csv.columns[[7, 13, 14, 15, 16, 17]], axis = 1, inplace=True)
truck_one_csv = truck_one_csv.drop(truck_one_csv.index[[7, 13, 14, 15, 16, 17]])


# In[63]:


truck_one_csv.head(40)


# In[64]:


truck_one_distances = truck_one_csv.to_numpy()
#print(truck_one_distances)


# In[65]:


truck_one_address = []

for value in truck_one_dict.values():
    if value[0] not in truck_one_address:
        truck_one_address.append(value[0])

#print(truck_one_address)


# #### Truck Two Data

# In[66]:


truck_two_csv = distance_file_csv.copy()
#truck_two_csv.head()


# In[67]:


truck_two_csv.drop(truck_two_csv.columns[[1, 2, 4, 5, 6]], axis = 1, inplace=True)
truck_two_csv = truck_two_csv.drop(truck_two_csv.index[[1, 2, 4, 5, 6]])


# In[68]:


truck_two_csv.drop(truck_two_csv.columns[[5, 6, 8, 9]], axis = 1, inplace=True)
truck_two_csv = truck_two_csv.drop(truck_two_csv.index[[5, 6, 8, 9]])


# In[69]:


truck_two_csv.drop(truck_two_csv.columns[[6, 8, 11, 12, 14]], axis = 1, inplace=True)
truck_two_csv = truck_two_csv.drop(truck_two_csv.index[[6, 8, 11, 12, 14]])


# In[70]:


truck_two_csv.head()


# In[71]:


truck_two_distances = truck_two_csv.to_numpy()
#print(truck_two_distances)


# In[72]:


truck_two_address = []

for value in truck_two_dict.values():
    #print(value[0])
    if value[0] not in truck_two_address:
        truck_two_address.append(value[0])

#print(truck_two_address)


# #### Truck Three Data

# In[73]:


truck_three_csv = distance_file_csv.copy()
#truck_three_csv.head()


# In[74]:


truck_three_csv.drop(truck_three_csv.columns[[3, 4, 5, 8]], axis = 1, inplace=True)
truck_three_csv = truck_three_csv.drop(truck_three_csv.index[[3, 4, 5, 8]])


# In[75]:


truck_three_csv.drop(truck_three_csv.columns[[12, 14, 16, 17, 18, 21, 22]], axis = 1, inplace=True)
truck_three_csv = truck_three_csv.drop(truck_three_csv.index[[12, 14, 16, 17, 18, 21, 22]])


# In[76]:


pd.set_option('display.max_columns', None)
truck_three_csv.head(7)


# In[77]:


truck_three_distances = truck_three_csv.to_numpy()
#print(truck_three_distances)
#print(truck_three_distances[14])


# In[78]:


truck_three_address = []

for value in truck_three_dict.values():
    #print(value[0])
    if value[0] not in truck_three_address:
        truck_three_address.append(value[0])

#print(truck_three_address)


# #### Nearest Neighbor Algorithm

# In[79]:


#notes on this algorithm are seen above in the practice code if there was only one truck
def truck_best_path(truck_dict, truck_distances, truck_csv, truck_pathway, truck_location_miles):
    truck_num_address = len(truck_csv)
    truck_visited = [False] * truck_num_address
    truck_path = []
    truck_distance = 0
    
    truck_current_location = 0
    truck_path.append(truck_current_location)
    truck_visited[truck_current_location] = True
    
    if truck_dict == truck_three_dict:
        truck_current_location = 9
        truck_path.append(truck_current_location)
        truck_visited[truck_current_location] = True
    
    
    #O(n2)
    while len(truck_path) < truck_num_address:
        truck_nearest_address = None
        truck_nearest_distance = math.inf
        
        for x in range(truck_num_address):
            if truck_visited[x] == False:
                truck_distance = float(truck_distances[truck_current_location][x])
                if truck_distance < truck_nearest_distance:
                    truck_nearest_address = x
                    truck_nearest_distance = truck_distance
            
        
        truck_location_miles.append(truck_nearest_distance)
        truck_current_location = truck_nearest_address
        truck_path.append(truck_current_location)
        truck_visited[truck_current_location] = True
    
    truck_distance = round(sum(truck_location_miles), 2)

    
    if truck_dict == truck_three_dict:
        truck_distance = 0
        truck_location_miles.clear()
        for i in range(len(truck_path)):
            if truck_path[i + 1] == truck_path[-1]:
                truck_location_miles.append(float(truck_three_distances[truck_path[i]][truck_path[i+1]]))
                break
            else:
                truck_location_miles.append(float(truck_three_distances[truck_path[i]][truck_path[i+1]]))
        #print(truck_location_miles)
            
        truck_distance = round(sum(truck_location_miles), 2)
        
            
    truck_location_miles.append(float(truck_distances[truck_path[-1]][truck_path[0]])) 

    

    print("Optimized Truck Path: " + str(truck_path))
    print("Total Distance: " + str(truck_distance) + " miles\n")
    
    
    #O(n)
    address_name = []
    for column_name in truck_csv.columns.values:
        address_name.append(column_name)    

       
    truck_best_path = [address_name[i] for i in truck_path]
    print("Best Path for Truck:")

    #O(n)
    for (path, x) in zip(truck_path, truck_best_path):
        truck_pathway.append(x)
        print("Location " + str(path) + " - " + x)     


# #### Truck One

# In[80]:


#truck one
#need to add western governors back in to figure out the time for truck three to leave
truck_one_pathway = []
truck_one_location_miles = []
truck_best_path(truck_one_dict, truck_one_distances, 
                truck_one_csv, truck_one_pathway, truck_one_location_miles)

#order of location # is based on truck_one_csv columns


# #### Truck Two

# In[81]:


#truck two
truck_two_pathway = []
truck_two_location_miles = []
truck_best_path(truck_two_dict, truck_two_distances, 
                truck_two_csv, truck_two_pathway, truck_two_location_miles)


# #### Truck Three

# In[82]:


#truck three
#location 9 (3060 Lester St) needs to be the first location as package 11 must be delivered by 10:30
truck_three_pathway = []
truck_three_location_miles = []
truck_best_path(truck_three_dict, truck_three_distances, 
                truck_three_csv, truck_three_pathway, truck_three_location_miles)


# #### All Truck Total Mileage

# In[83]:


all_truck_mileage = truck_one_location_miles + truck_two_location_miles + truck_three_location_miles
all_truck_total_mileage = round(sum(all_truck_mileage), 2)


# In[84]:


print("Total Distance Between All Trucks: " + str(all_truck_total_mileage) + " mi")


# ### 4. Get Packages Sent Out!

# Remember:
# - The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
# - There are no collisions.
# - Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
# - Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
# - The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).
# - The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
# - Keep the combined total distance traveled under 140 miles.

# $$
#     time = \frac{distance}{speed (mph)} x 60 min
# $$

# In[103]:


def send_packages(truck_pathway, truck_location_miles, truck_number_dict, time, truck_packages):
    
    #O(n2)
    #changes the third index of value to 'EN ROUTE'
    #also creates a new dictionary with the delivery time being the key and the value being a dictionary of all trucks
    for key, value in truck_number_dict.items():
        value[3] = 'EN ROUTE'
        truck_packages[value[5]] = truck_dict
    
    current_time = time
    #this changes package 9's address to "410 S State St" at 10:20
    if truck_number_dict == truck_three_dict:
        for key, value in truck_three_dict.items():
            if key == 9:
                if str(current_time) == "10:20:00":
                    value[0] = "410 S State St"
                
                    
    if truck_number_dict == truck_two_dict:
        for key, value in truck_two_dict.items():
            if key == 12:
                value[0] = "3575 W"
                
    
    #O(n2)
    for i in range(len(truck_pathway)):
        #starts the delivery, shows the current time
        if truck_pathway[i] == truck_pathway[0]:
            print("-------- Out For Delivery --------")
            print("       | Current Time: " + str(current_time) + " |       \n")
    
        #when truck_pathway[i] isn't the beginning address
        if truck_pathway[i] != truck_pathway[0]:
            for key, value in truck_number_dict.items():
                if key == 9:
                    if current_time >= datetime.time(10, 20):
                        value[0] = "410 S State St"
                #since package 9 was changed, no packages will be delivered to "300 State St"
                if truck_pathway == truck_three_pathway:
                    if "300 State St" in truck_pathway[i]:
                        print("\tNo packages to deliver here!")
                        break
                #prints the package and the time it was delivered
                #also sets the third value to 'DELIVERED'
                if value[0] in truck_pathway[i]:
                    print("\tPackage " + str(key) + " has been delivered at " + str(current_time))
                    value[4] = str(time)
                    value[3] = "DELIVERED"
                    value[5] = str(current_time)
                
            print()
            print("--------------------------------------------------------------------------------------------")
            print()
            
            
        #updating the time using the time equation (time = (distance/speed) * 60)
        time_in_min = int((truck_location_miles[i] / 18) * 60)
        #print(time_in_min)
    
        #if the minutes is less than 60
        if (current_time.minute + time_in_min) < 60:
            current_time = datetime.time(current_time.hour, current_time.minute + time_in_min)
        #when the minutes is more than 60, it will add an hour and find the difference to determine the minutes
        else:
            current_time = datetime.time(current_time.hour + 1, abs((current_time.minute) - (60 - time_in_min)))    
            
    
        #when truck_pathway[i] is the last variable
        if truck_pathway[i] == truck_pathway[-1]:
            print()
            print(str(truck_pathway[i]) + " ---> " + str(truck_pathway[0]) + ": " + str(truck_location_miles[i]) + " mi")
            print()
            print("-------- Arrived @ " + truck_pathway[0] + " --------")
            print("         | Current Time: " + str(current_time) + " |         \n")
            break
        else:
            #shows the current truck_pathway going to the upcoming truck_pathway and shows the miles between the two
            print(str(truck_pathway[i]) + " ---> " + str(truck_pathway[i + 1]) + ": " + str(truck_location_miles[i]) + " mi")
        print("\n\n") 
    
        print("-------- Arrived @ " + truck_pathway[i + 1] + " --------")
        print("         | Current Time: " + str(current_time) + " |         \n")


# #### Truck One

# In[104]:


truck_one_packages = {}
send_packages(truck_one_pathway, truck_one_location_miles, truck_one_dict, datetime.time(8,0), truck_one_packages)


# In[105]:


truck_one_packages_sorted = dict(sorted(truck_one_packages.items()))


# #### Truck Two

# In[106]:


truck_two_packages = {}
send_packages(truck_two_pathway, truck_two_location_miles, truck_two_dict, datetime.time(8,0), truck_two_packages)


# In[107]:


truck_two_packages_sorted = dict(sorted(truck_two_packages.items()))


# #### Truck Three

# In[108]:


truck_three_packages = {}
send_packages(truck_three_pathway, truck_three_location_miles, truck_three_dict, datetime.time(10), truck_three_packages) 


# In[109]:


truck_three_packages_sorted = dict(sorted(truck_three_packages.items()))


# #### All Trucks

# In[110]:


all_truck_packages = truck_one_packages_sorted | truck_two_packages_sorted | truck_three_packages_sorted


# In[111]:


all_truck_packages_sorted = dict(sorted(all_truck_packages.items()))


# In[112]:


#for key, value in all_truck_packages_sorted.items():
    #print(key, value)
    #print()


# ## F. Look-Up Function

# The look-up function will be pulling information from the Hash Table created previously in order to view the specifications of the packages. First the data from the Hash Table needs to be pulled from each truck and combine them together before inputting them into the function.

# Now that the data has been created, we can ask the user for input to look up the specific packages.

# In[95]:


def look_up_package(truck_dict, user_input):
    #O(n2)
    while user_input != "":
        if user_input.isnumeric():
            #while the input is in between 1 and 40 since the packages go from 1-40
            if int(user_input) <= 40 and int(user_input) >= 1:
                for key, value in sorted(truck_dict.items()):
                    if int(user_input) == key:
                        print(value)
                        print()
                        exit_input = str(input("Are you finished searching for packages? [y/n] ")).lower()
                        if exit_input == "n" or exit_input == "y":
                            if exit_input == "y":
                                return
                            else:
                                user_input = str(input("\nWhat package are you looking for? Package #"))
                        else:
                            print("Invalid, please enter choose [y/n] ")
                            exit_input = str(input("Are you finished searching for packages? [y/n] ")).lower()
                            if exit_input == "y":
                                return
                            elif exit_input == "n":
                                user_input = str(input("\nWhat package are you looking for? Package #"))
                                print(value)
                                exit_input = str(input("Are you finished searching for packages? [y/n] ")).lower()
                else:
                    print("Invalid, please enter a package number from 1 - 40.")
                    user_input = str(input("\nWhat package are you looking for? Package #")).lower()

            else:
                print("Invalid, please enter a package number from 1 - 40.")
                user_input = str(input("What package are you looking for? Package #")).lower()


# In[96]:


print("---------------------------- Look Up a Package ----------------------------\n")
user_input = str(input("What package are you looking for? Package #"))

look_up_package(truck_dict, user_input)


# ## G. Create an Interface to View Status and Info of Package

# This interface will provide the user to view the status and information of any package at any time. The function will be based on the time so we can see if it's been delayed, loaded, enroute, or delivered.

# In[113]:


truck_pathway = truck_one_pathway + truck_two_pathway + truck_three_pathway


# In[114]:


truck_packages_copy_key = []
truck_packages_copy_values = []


# In[115]:


#print("Please enter a start time: ")
#start_hour_input = str(input("Hour: "))
#start_minute_input = str(input("Minute(s): "))
#start_time = datetime.time(int(start_hour_input), int(start_minute_input))
#print(str(start_time))

#print("\nPlease enter an end time: ")
#end_hour_input = str(input("Hour: "))
#end_minute_input = str(input("Minute(s): "))
#end_time = datetime.time(int(end_hour_input), int(end_minute_input))
#print(str(end_time))

def view_package_by_time(start_time, end_time):

    print("\n---------------------------------------------------------------------------------------------------------------\n")

    #O(n)
    for key, value in all_truck_packages_sorted.items():
        truck_packages_copy_key.append(key)
        truck_packages_copy_values.append(value)
        
        #O(n)
        for i in range(len(truck_pathway)): 
            if truck_pathway[i] != truck_pathway[0]:
                #O(n)
                for j in range(len(truck_packages_copy_values)):
                    #O(n)
                    #looks at the key and value of the dictionaries truck_packages_copy_values[j]
                    for k, v in truck_packages_copy_values[j].items():
                        #if the delivery time is greater than the key in truck_packages_copy_key[j] it's en route
                        if v[5] > truck_packages_copy_key[j]:
                             v[3] = 'EN ROUTE'
                        #if the delivery time is less than or equal to truck_packages_copy_key[j] it's delivered
                        if v[5] <= truck_packages_copy_key[j]:
                            v[3] = 'DELIVERED'
                        #if the start time is 10:00 (only truck three)
                        if v[4] == "10:00:00":
                            #if the start time is greater than truck_packages_copy_key[j] the packages are at the hub
                            #until 10:00, then it will either be en route or delivered
                            if v[4] > truck_packages_copy_key[j]:
                                v[3] = "LOADED ON TRUCK - AT HUB"

    
        #print(key, value)
        #print()
        if str(key) >= str(start_time) and str(key) <= str(end_time):
            print(key)
            #goes through the key and value within the value within the all_truck_packages_sorted
            for k, v in value.items():
                for key_one, value_one in truck_one_dict.items():
                    if k == key_one:
                        if v[3] == 'DELIVERED':
                            print("Truck: 1, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              ", Delivered at " + str(v[5]))
                        else:
                            print("Truck: 1, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
                for key_two, value_two in truck_two_dict.items():
                    if k == key_two:
                        if v[3] == 'DELIVERED':
                            print("Truck: 2, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              ", Delivered at " + str(v[5]))
                        else:
                            print("Truck: 2, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
                for key_three, value_three in truck_three_dict.items():
                    if k == key_three:
                        if v[3] == 'DELIVERED':
                            print("Truck: 3, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              ", Delivered at " + str(v[5]))
                        else:
                            print("Truck: 3, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
            print()
    
    

#each individual truck combined together; works properly but unable to sort the keys in order of time    
#for key, value in truck_one_packages_sorted.items():
    #truck_packages_copy_key.append(key)
    #truck_packages_copy_values.append(value)
    
    #for i in range(len(truck_pathway)): 
        #if truck_pathway[i] != truck_pathway[0]:
            #for j in range(len(truck_packages_copy_values)):
                #for k, v in truck_packages_copy_values[j].items():
                    #if v[5] > truck_packages_copy_key[j]:
                        #v[3] = 'EN ROUTE'
                    #if v[0] in truck_pathway[i]:
                        #v[3] = "EN ROUTE"
                    #if truck_packages_copy_key[j] == v[5]:
                        #v[3] = 'DELIVERED'
                    #if v[5] <= truck_packages_copy_key[j]:
                        #v[3] = 'DELIVERED'
    
    #print(key, value)
    #print()
    #if str(key) >= str(start_time) and str(key) <= str(end_time):
        #print(key)
        #for k, v in value.items():
            #for key_one, value_one in truck_one_dict.items():
                #if k == key_one:
                    #if v[3] == 'DELIVERED':
                        #print("Truck: 1, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              #", Delivered at " + str(v[5]))
                    #else:
                        #print("Truck: 1, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
            #for key_two, value_two in truck_two_dict.items():
                #if k == key_two:
                    #if v[3] == 'DELIVERED':
                        #print("Truck: 2, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              #", Delivered at " + str(v[5]))
                    #else:
                        #print("Truck: 2, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
            #for key_three, value_three in truck_three_dict.items():
                #if k == key_three:
                    #if value_three[4] == '10:00:00':
                        #v[3] = 'LOADED ON TRUCK - AT HUB'
                    #if v[3] == 'DELIVERED':
                        #print("Truck: 3, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              #", Delivered at " + str(v[5]))
                    #else:
                        #print("Truck: 3, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
        #print()
        
    
#for key, value in truck_two_packages_sorted.items():
    #truck_packages_copy_key.append(key)
    #truck_packages_copy_values.append(value)
    
    #for i in range(len(truck_pathway)): 
        #if truck_pathway[i] != truck_pathway[0]:
            #for j in range(len(truck_packages_copy_values)):
                #for k, v in truck_packages_copy_values[j].items():
                    #if v[5] > truck_packages_copy_key[j]:
                        #v[3] = 'EN ROUTE'
                    #if v[0] in truck_pathway[i]:
                        #v[3] = "EN ROUTE"
                    #if truck_packages_copy_key[j] == v[5]:
                        #v[3] = 'DELIVERED'
                    #if v[5] <= truck_packages_copy_key[j]:
                        #v[3] = 'DELIVERED'
    
    #print(key, value)
    #print()   
    #if str(key) >= str(start_time) and str(key) <= str(end_time):
        #print(key)
        #for k, v in value.items():
            #for key_one, value_one in truck_one_dict.items():
                #if k == key_one:
                    #if v[3] == 'DELIVERED':
                        #print("Truck: 1, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              #", Delivered at " + str(v[5]))
                    #else:
                        #print("Truck: 1, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
            #for key_two, value_two in truck_two_dict.items():
                #if k == key_two:
                    #if v[3] == 'DELIVERED':
                        #print("Truck: 2, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              #", Delivered at " + str(v[5]))
                    #else:
                        #print("Truck: 2, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
            #for key_three, value_three in truck_three_dict.items():
                #if k == key_three:
                    #if value_three[4] == '10:00:00':
                        #v[3] = 'LOADED ON TRUCK - AT HUB'
                    #if v[3] == 'DELIVERED':
                        #print("Truck: 3, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              #", Delivered at " + str(v[5]))
                    #else:
                        #print("Truck: 3, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
        #print()
    
    
#for key, value in truck_three_packages_sorted.items():
    #truck_packages_copy_key.append(key)
    #truck_packages_copy_values.append(value)
    
    #for i in range(len(truck_pathway)): 
        #if truck_pathway[i] != truck_pathway[0]:
            #for j in range(len(truck_packages_copy_values)):
                #for k, v in truck_packages_copy_values[j].items():
                    #if v[5] > truck_packages_copy_key[j]:
                        #v[3] = 'EN ROUTE'
                    #if v[0] in truck_pathway[i]:
                        #v[3] = "EN ROUTE"
                    #if truck_packages_copy_key[j] == v[5]:
                        #v[3] = 'DELIVERED'
                    #if v[5] <= truck_packages_copy_key[j]:
                        #v[3] = 'DELIVERED'
    
    #print(key, value)
    #print()
    #if str(key) >= str(start_time) and str(key) <= str(end_time):
        #print(key)
        #for k, v in value.items():
            #for key_one, value_one in truck_one_dict.items():
                #if k == key_one:
                    #if v[3] == 'DELIVERED':
                        #print("Truck: 1, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              #", Delivered at " + str(v[5]))
                    #else:
                        #print("Truck: 1, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
            #for key_two, value_two in truck_two_dict.items():
                #if k == key_two:
                    #if v[3] == 'DELIVERED':
                        #print("Truck: 2, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              #", Delivered at " + str(v[5]))
                    #else:
                        #print("Truck: 2, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
            #for key_three, value_three in truck_three_dict.items():
                #if k == key_three:
                    #if v[3] == 'DELIVERED':
                        #print("Truck: 3, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]) + 
                              #", Delivered at " + str(v[5]))
                    #else:
                        #print("Truck: 3, Package ID : " + str(k) + ", Address: " + str(v[0]) + ", Status: " + str(v[3]))
        #print()


# ## H. Screenshots from Interface

# The screenshots from the interface will also include the total milage driven by all three trucks.

# ### 1. Status of Packages Between 8:35AM and 9:25AM

# In[116]:


print("Please enter a start time: ")
start_hour_input = str(input("Hour: "))
start_minute_input = str(input("Minute(s): "))
start_time = datetime.time(int(start_hour_input), int(start_minute_input))
print(str(start_time))

print("\nPlease enter an end time: ")
end_hour_input = str(input("Hour: "))
end_minute_input = str(input("Minute(s): "))
end_time = datetime.time(int(end_hour_input), int(end_minute_input))
print(str(end_time))

view_package_by_time(start_time, end_time)


# ### 2. Status of Packages Between 9:35AM and 10:25AM

# In[117]:


print("Please enter a start time: ")
start_hour_input = str(input("Hour: "))
start_minute_input = str(input("Minute(s): "))
start_time = datetime.time(int(start_hour_input), int(start_minute_input))
print(str(start_time))

print("\nPlease enter an end time: ")
end_hour_input = str(input("Hour: "))
end_minute_input = str(input("Minute(s): "))
end_time = datetime.time(int(end_hour_input), int(end_minute_input))
print(str(end_time))

view_package_by_time(start_time, end_time)


# ### 3. Status of Packages Between 12:03PM and 1:12PM

# In[102]:


print("Please enter a start time: ")
start_hour_input = str(input("Hour: "))
start_minute_input = str(input("Minute(s): "))
start_time = datetime.time(int(start_hour_input), int(start_minute_input))
print(str(start_time))

print("\nPlease enter an end time: ")
end_hour_input = str(input("Hour: "))
end_minute_input = str(input("Minute(s): "))
end_time = datetime.time(int(end_hour_input), int(end_minute_input))
print(str(end_time))

view_package_by_time(start_time, end_time)


# The output for this status of packages above is empty because all the packages are delivered before 12pm, including the last package from Truck 3 that is delivered at 11:56am.

# ## I. Justify Nearest Neighbor Algorithm

# ### 1. Strengths of Nearest Neighbor Algorithm

# 1. The Nearest Neighbor Algorithm is fairly easy to implement and is able to run quickly as long as the data is in a type of matrix (reference the truck `.csv` files to see examples). The programming actually isn't too complicated and it's easy to gather data from the algorithm.
# 2. The algorithm is able to adapt very easily. There are very minimal changes that need to be made if there are more or less trucks as long as there is data tied to each truck that is added.

# ### 2. Verification of Algorithm

# #### Provide the Total Combined Miles
# 
# It must be less than 140 mi.

# In[119]:


print("Total Distance Between All Trucks: " + str(all_truck_total_mileage) + " mi")


# #### Verification of Packages
# 
# 1. They were delivered on time.
# 2. They were delivered according to their delivery specifications.

# In[120]:


send_packages(truck_one_pathway, truck_one_location_miles, truck_one_dict, datetime.time(8,0), truck_one_packages)


# In[121]:


send_packages(truck_two_pathway, truck_two_location_miles, truck_two_dict, datetime.time(8,0), truck_two_packages)


# In[122]:


send_packages(truck_three_pathway, truck_three_location_miles, truck_three_dict, datetime.time(10), truck_three_packages)


# ### 3. Different Possible Algorithms

# Two possible algorithms that would essentially do the same thing as the Nearest Neighbor Algorithm would be:
# 1. The **Nearest Insertion Algorithm** is very similar to the Nearest Neighbor Algorithm as the insertion algorithm starts with two locations and checks if the next location has been visited or not. It will then add the location to the visited list, but will check to see if there is a shorter distance between the visited locations (and may alter the pathway if there is a shorter distance).
# 2. The **Random Insertion Algorithm** is just like the Nearest Insertion Algorithm as it starts with two locations, but it randomly chooses locations and checks if it's been visited or not. If it hasn't been visited it will join the visited list and will check to see if there is a shorter distance between the visited locations.

# ### 4. Algorithm Differences

# 1. **Nearest Insertion Algorithm**
#     - Since the Nearest Insertion Algorithm is so similar to the Nearest Neighbor Algorithm, it follows the same time complexity: O(n2).
#     - An advantage to this algorithm is that it starts with two locations. However, a disadvantage to this algorithm would be that it wouldn't fully optimize the locations and distances as it only finds the nearest ones with the least amount of distance between locations.
#  
#  <br>
#     
# 2. **Random Insertion Algorithm**
#     - Because the Random Insertion Algorithm is very similar to the Nearest Insertion Algorithm, it has the same time complexity: O(n2).
#     - A disadvantage to this algorithm is that because it chooses locations at random, it may not be able to find the most optimal locations and distances and may take longer than the rest of the algorithms.

# ## J. Describe What You Would Do Differently

# I would only change my program by implementing a Truck class before running the Hash Table so the packages could be manually loaded through the Truck class rather than taking the more difficult and time-consuming path of implementing each truck as a Hash Table, then organizing the data and moving it into a dictionary.

# ## K. Justify the Data Structure in Part D

# ### 1. Explaination and Verification

# #### Provide the Total Combined Miles
# 
# Must be less than 140 mi.

# In[123]:


print("Total Distance Between All Trucks: " + str(all_truck_total_mileage) + " mi")


# #### Verification of Packages
# 
# 1. They were delivered on time.
# 2. They were delivered according to their delivery specifications.

# In[124]:


send_packages(truck_one_pathway, truck_one_location_miles, truck_one_dict, datetime.time(8,0), truck_one_packages)


# In[125]:


send_packages(truck_two_pathway, truck_two_location_miles, truck_two_dict, datetime.time(8,0), truck_two_packages)


# In[126]:


send_packages(truck_three_pathway, truck_three_location_miles, truck_three_dict, datetime.time(10), truck_three_packages)


# #### Verification of Look-Up Function

# In[127]:


print("---------------------------- Look Up a Package ----------------------------\n")
user_input = str(input("What package are you looking for? Package #"))

look_up_package(truck_dict, user_input)


# #### Verification of Package Status and Information

# In[128]:


print("Please enter a start time: ")
start_hour_input = str(input("Hour: "))
start_minute_input = str(input("Minute(s): "))
start_time = datetime.time(int(start_hour_input), int(start_minute_input))
print(str(start_time))

print("\nPlease enter an end time: ")
end_hour_input = str(input("Hour: "))
end_minute_input = str(input("Minute(s): "))
end_time = datetime.time(int(end_hour_input), int(end_minute_input))
print(str(end_time))

view_package_by_time(start_time, end_time)


# #### Efficiency
# 
# Adding packages shouldn't directly affect the time needed to complete the look-up function as the function is meant to be able to check the `truck_dict` to see if it exists and extract the package data from there. So with each package getting added, it will first be added to the `truck_dict`. Unless there were thousands of packages, then the function might slow down when searching through the dictionary, but it should still work properly.

# #### Overhead
# 
# Adding multiple packages could potentially affect the data structure space if the size of the data structure isn't large enough. This program has the data structure size set to 48 which could cause many packages to be inserted into the buckets. Luckily the packages should spread evenly between the buckets, but if there's too many packages in a bucket it can heavily affect the space. To fix this, all that needs to be done is to set the data structure size to something much larger.

# #### Implication
# 
# Adding more trucks shouldn't be too much of an issue as the current trucks in the program gather packages that need to be delivered early, and the other two trucks are divided by even and odd packages. With adding more trucks, some trucks could focus on later delivery times, or could split the packages using the modulo `%` to split packages by the number of trucks. Adding the additional trucks wouldn't affect the look-up time as the look-up function only looks up packages, and it shouldn't affect the space usage in a negative way, in fact it should help reduce space usage by splitting the packages up instead of having three trucks holding a lot of packages.
# 
# Adding more locations shouldn't affect the look-up time either as it would only be affected by packages (that may contain the new locations). It shouldn't affect the space usage either as in this program the new locations and distances would be added to the truck `.csv` file, not into the look-up function.

# ### 2. Alternate Data Structures

# 1. An alternative data structure that I would have preferred to use over a Hash Table would be a **dictionary**. The dictionary is essentially identical to a Hash Table but is a lot easier to manipulate, organize, and extract the data. The dictionary also wouldn't put the package data into buckets that contain multiple packages; it would just be possible to use a for-loop to take the data from the package `.csv` and turn it in a dictionary.
# ```
# {1: [195 W Oakland Ave, 10:30 AM, 21, LOADED ON TRUCK - IN HUB, 08:00:00, 00:00:00],
#  2: [2530 S 500 E, EOD, 44, LOADED ON TRUCK - IN HUB, 08:00:00, 00:00:00]}
# ```
# 2. Another alternative data structure I would have used is a **list** as it could be very similar to a dictionary without needing to use `.items()` to go through the dictionary to view its keys and values. It would be little more complicated to view (if not printed out in a for-loop), but would be very easy to organize and extract data when needed.
# ```
# [[1, [195 W Oakland Ave, 10:30 AM, 21, LOADED ON TRUCK - IN HUB, 08:00:00, 00:00:00]],
# [2, [2530 S 500 E, EOD, 44, LOADED ON TRUCK - IN HUB, 08:00:00, 00:00:00]]]
# ```

# #### Data Structure Differences
# 
# 1. **Dictionary**
#     - Dictionaries are mutable, meaning the data within the dictionaries can be altered. This can be both be advantageous or disadvantageous as it allows you to change the keys or values, but it also means that if there are multiple keys that are the same variable, the value will be replaced each time.
#     - Dictionaries are able to contain multiple data types for both keys and values, with the exception of lists. Dictionary keys can be strings, integers, boolean, etc., but can't be a list. Dictionary values can be the same as dictionary keys: strings, integers, boolean, etc, but can also be a list that contains multiple data types as well.
# 
# <br>
# 
# 2. **List**
#     - Just like dictionaries, lists are mutable; but unlike dictionaries, lists are altered by using the list index as compared to the key, value pair. Personally, it is a easier to view data in a list within a for-loop than it is using a dictionary.
#     - Another big difference from dictionaires is that lists can contain duplicates, while dictionaries will overwrite the value if there are duplicate keys. This can be an advantage if a program that is being created may have duplicate values, such as a grocery list. 

# ## L. Sources

# No outside sources were used.
