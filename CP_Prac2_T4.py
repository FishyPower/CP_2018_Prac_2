
# coding: utf-8

# In[17]:


#Computing Practical 2 - Task 4

year = int(input("Input year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap")
else:
    print("Non-Leap")

