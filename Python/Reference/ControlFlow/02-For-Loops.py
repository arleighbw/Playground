
# coding: utf-8

# # for loop
# 
# Welcome back recruit, its time to learn a new loop! A **for loop** acts as an iterator in Python, it goes through items that are in a sequence or any other iterable item. Objects that we've learned about that we can iterate over include strings,lists,tuples, and even built in iterables for dictionaries, such as the keys or values.
# 
# Here's the general format for a for loop in Python:
# 
#     for item in object:
#         statements to do stuff
#         
# The variable name used for the item is completely up to the coder, so use your best judgment for choosing a name that makes sense and you will be able to understand when revisiting your code. This item name can then be referenced inside you loop, for example if you wanted to use if statements to perform checks.
# 
# Let's go ahead and work through several example of for loops using a variety of data object types. we'll start simple and build more complexity later on.

# ## for loop with a list

# In[2]:


mylist = [1,2,3,4]

for num in mylist:
    print(num)


# In[3]:


for totally_made_up in mylist:
    print(totally_made_up)


# In[8]:


for num in mylist:
    print(num,end=' ')


# In[10]:


for num in mylist:
    print("some unrelated variable, but print for every num in mylist")


# ## for loop with strings

# In[11]:


for letter in "This is a string recruit":
    print(letter)


# In[12]:


mystring = 'This is a string recruit'

for word in mystring.split():
    print(word)


# ## for loop with tuple

# In[13]:


tup = (1,2,3,4)

for num in tup:
    print(num)


# ## tuple unpacking

# In[14]:


list_of_tups = [(1,2),(3,4),(5,6),(7,8),(9,10)]


# In[18]:


for x in list_of_tups:
    print(x)


# In[20]:


for x in list_of_tups:
    print(x[0])


# In[21]:


for x in list_of_tups:
    print(x[1])


# In[16]:


for (num1,num2) in list_of_tups:
    print(num1)
    print(num2)
    print('\n')
    


# In[22]:


# Doesn't need the parenthesis

for num1,num2 in list_of_tups:
    print(num1)
    print(num2)
    print('\n')
    


# ## for loop with dictionaries

# In[23]:


my_dictionary = {'a':1,'b':2,'c':3}


# Remember that dictionaries don't retain any order! So only loop through them with this in mind!

# In[24]:


for item in my_dictionary:
    print(item)


# In[25]:


for k in my_dictionary.keys():
    print(k)


# In[26]:


for k in my_dictionary.keys():
    print(k)
    print(my_dictionary[k])
    print('\n')


# ----

# ## continue
# The continue keyword can be a bit tricky to see its usefulness, but it allows you to continue with the top level loop, basicaly the opposite of break. It will take time before you realize a good situation to use it in, but here is a simple example:

# In[1]:


for letter in 'code':
    if letter == 'd':
        continue
        
    print('Current Letter is: {}'.format(letter))


# That is all for now recruit, excellent work!
