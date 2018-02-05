
# coding: utf-8

# In[15]:


#Computing Practical 2 - Task 2

a = int(input("Input side a: "))
b = int(input("Input side b: "))
c = int(input("Input side c: "))

perimeter = a + b + c

def logic():
    if perimeter - a <= a:
        return False
    elif perimeter - b <= b:
        return False
    elif perimeter - c <= c:
        return False
    else:
        return True

if logic() == True:
    print("perimeter = " "{0}" .format(perimeter)) 
else:
    print("Invalid triangle!")

