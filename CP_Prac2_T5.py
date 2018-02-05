
# coding: utf-8

# In[30]:


## Computing Practical 2 - Task 5

year = int(input("Input year: ")) 

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = 1
else:
    leap = 0
    
name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input("Input month: "))

print("{0} {1} has {2} days.".format(name[month-1], year, days[month-1] + leap))

