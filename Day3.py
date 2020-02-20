#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Adding Whitespace to the string
print('python')
print('\tpython')
print("hello\t...")

#  Note :  "\t" is a tab, 
#         "\n" is a newline 


# In[15]:


print("languages:\n\tpython\n\tjava\n\tswift\n\truby")


# In[39]:


print('Hello, \'friend\'!Please enter your name below:Name:(your name here)Age:(your age here)')
print("\n")
print('Hello, \'friend\'!\nPlease enter your name below:\nName:\t(your name here)\nAge:\t(your age here)')
print("\n")
print('Here\'s how you print directories path: \"C:Users\\python\\examples\"')  

 #Note :
print("\\ => print Backslash (\)")
print("\' => Single quote (')")
print('\" => Double quote (")')
#Note :\\	Backslash (\)
#        \'	Single quote (')
#        \"	Double quote (")


# In[60]:


# How to remove whitespace
fav_lang1 ="Python    "   # rightside space
fav_lang2 ="      Java"   # rightside space 
fav_lang3 ="  MongoDB    "   # space both side

print(fav_lang1) 
print(fav_lang2)
print("-------output after removing space---------")
print(fav_lang1.rstrip()) 
print(fav_lang2.lstrip())
print(fav_lang3.strip())


# In[49]:


# Number 

2+3 # Addition of integer


# In[48]:


3-5  #Subtraction of integer


# In[50]:


2*5  #Multiplication of integer


# In[51]:


20/5 #Division of integer


# In[52]:


2**3 # 2 to the Power 3


# In[53]:


# float
3.0+4.1


# In[56]:


x = 2.1
y = 3.1


# In[58]:


z=x+y
print(z)


# In[59]:


type(z)

