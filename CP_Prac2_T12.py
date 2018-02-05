
# coding: utf-8

# In[18]:


# Computing Practical 2 - Task 12

integer = int(input("Input integer: "))
factor = 2
factors = []
while integer >= factor:
    
    if integer % factor != 0:
        factor = factor + 1
    elif integer % factor == 0:
        integer = integer / factor
        factors.append(factor)
        
if integer == 1:
    print(factors)

