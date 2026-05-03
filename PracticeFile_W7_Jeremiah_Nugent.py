#For this practice file from week 7, we learned how to color code our lines
# In[1]:
#Accessing the first item from the list colors
colors = ['red', 'green', 'blue']
First_item= colors[0]
print(First_item)
 

# In[2]:
#Accessing the third item from the mixedList
mixedList = ['hello', 123, 45.6, True]
mixedList[2]

# In[3]:
colors = ['red', 'green', 'blue']
First_item= colors[-1]
print(First_item)

# In[4]:
even_number = [2,4,6,8,10,12,14,16]
print(len(even_number))

# In[5]:
my_list = [10, 20, 30, 40]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# In[6]:
alist = [1, 4, 9, 16, 25]
print(alist[0:4])

# In[7]:
alist = [1, 4, 9, 16, 25]
print(alist[:5])

# In[8]:
alist = [1, 4, 9, 16, 25]
print(alist[3:])

# In[9]:
alist = [1, 4, 9, 16, 25]
print(alist[0:4:2])

# In[10]:
# Translate Air Quality Index (AQI) from number to color and concern
# https://www.airnow.gov/aqi/aqi-basics/
 
# lists of levels and corresponding colors and concerns
levels = [301, 201, 151, 101, 51, 0]
colors = ['Maroon', 'Purple', 'Red', 'Orange', 'Yellow', 'Green']
concerns = ['Hazardous', 'Very Unhealthy', 'Unhealthy','Unhealthy for Sensitive Groups', 'Moderate', 'Good']
 
# input
level = int(input('Enter an AQI level (integer): '))
 
# processing
for i in range(len(levels)):
    if level >= levels[i]:
        color = colors[i]
        concern = concerns[i]
        break
 
# output
print('AQI color:', color)
print('AQI concern level:', concern)
 

# In[11]:
vegetables = ['cabbage', 'spinach', 'potato']
fruits = ['apple', 'banana', 'cherry']
for x in vegetables:
    for y in fruits:
        print(x, y)

# In[12]:
matrix = [['John', 'Jones'], ['Jane', 'Doe'], ['Jim', 'Johnson']]
# display the list of lists
for row in matrix:
    for cell in row:
        print(cell, end='|')
    print()
