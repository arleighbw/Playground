
# coding: utf-8

# # List Comprehensions
# 
# In addition to sequence operations and list methods, Python includes a more advanced operation called a list comprehension.
# List comprehensions allow us to build out lists using a different notation. You can think of it as essentially a one line for loop built inside of brackets. For a simple example:

# ## Simple list comprehension
# 
# If you find yourself using a for loop to only .append() to a list, you might want to consider a list comprehension, for example

# In[2]:


mylist = []
for let in 'word':
    mylist.append(let)


# In[3]:


mylist


# ### Using a list comprehension

# In[4]:


# Grab every letter in string
myletters = [let for let in 'word']


# In[5]:


myletters


# Let's go through some more complex examples

# In[6]:


squares = [x**2 for x in range(0,11)]


# In[7]:


squares


# We can also use if statements in a list comprehension

# In[11]:


evens = [x for x in range(0,10) if x%2 == 0]


# In[12]:


evens


# You can also do an if/else statement in a list comprehension, but keep in mind, at a certain point you will sacarafice readability, which is a big part of Python. If you are having trouble figuring out how to put something in a list comprehension, just use a for loop instead, its almost always just as efficient.
# 
# Keep in mind the ordering gets changed when adding the if/else statement. In general, such complicated list comprehensions are probably best avoided to maintain readability!

# In[18]:


mylist = [x if x%2 == 0 else 'not even' for x in range(0,10) ]


# In[19]:


mylist


# Ok that is all for working with Python, its time for your second Field Readiness Exam recruit!
