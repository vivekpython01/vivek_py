#!/usr/bin/env python
# coding: utf-8

# In[7]:


x=10
y=20


# In[8]:


print(x+y)


# In[10]:


#Rules for declaring variable 
   
 1. There should not be gap between variable name.  Example : First name ='Raj' --Invalid
                                                                First_name ='Raj' --Valid
                                                                Firstname  ='Raj' --Valid
 2. It should not be start with number.             Example : 11First name   ='Raj' --Invalid
                                                                First_name11 ='Raj' --Valid
                                                                Firstname11  ='Raj' --Valid
 3. It should not be start with special character.  Example : $First name ='Raj' --Invalid
                                                               First_name$ ='Raj' --Valid
                                                               Firstname$1 ='Raj' --Valid


# In[ ]:


# Data type in python
1.String    -->str
2.List      -->list
3.Tuple     -->tuple
4.Set       -->set
5.Dictionay -->dict
# Python is Case sensitive language.


# In[ ]:


What is string ?
String is sequence of characters.
A string is an immutable data type(which cannot be changed once it is assign)

#Declaration of string 
  There are 3 ways to declare  string variable.
    1. ''        --> single quotes
    2. " "       --> Double quotes
    3."""  """   --> Triple quotes
    
    


# name1='Mohit'

# In[14]:


print(name1)


# In[27]:


name2="Ajay Kumar Singh"


# In[28]:


print(name2)


# In[30]:


name3="""Amit"""


# In[31]:


print(name3)


# In[ ]:


# type() is used to find the datatype of variable


# In[32]:


type(name3)


# In[ ]:


# String Methond
   
   title() --> is used to convert input string to Camel Case  --> ravi kumar  to Ravi Kumar
   upper() --> is used to convert input string to Upper Case  --> ravi kumar  to RAVI KUMAR
   lower() --> is used to convert input string to Upper Case  --> RAVI KUMAR  to ravi kumar   


# In[39]:


name="ravi kumar"


# In[40]:


print(name.title())


# In[41]:


name="RAVI KUMAR"


# In[42]:


print(name.title())


# In[49]:


name="ravi kumar"


# In[50]:


print(name.upper())


# In[51]:


name="RAVI KUMAR"


# In[52]:


print(name.lower())


# In[ ]:


Note : f-strings in Python  also known as Literal string interpolation
The use of f-string allows the programmer to dynamically insert a variable into a string in a clean and concise manner.
To perform these dynamic behaviours within an f-string we wrap them inside curly brackets within the string, 
and prepend a lower case f to the beginning of the string (before the opening quote.
                                                          
name = 'World'
greeting = f'Hello! {name}'
print(greeting)


# In[54]:


name = 'World'
greeting = f'Hello! {name}'
print(greeting)


# In[57]:


# Example
val1 = 2
val2 = 3
expr = F'The sum of {val1} + {val2} is {val1 + val2}'
print(expr)


# In[ ]:





# In[ ]:




