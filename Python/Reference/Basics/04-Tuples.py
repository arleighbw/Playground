
# coding: utf-8

# # Tuples 
# 
# Hello Recruit! Welcome back. Let's quickly go over Tuples, a fundamental data type that you will see quite a bit as you learn more on your way to becoming a full agent.
# 
# Tuples are ordered sequences just like a list, but have one major difference, they are **immutable**. Meaning you can not *mutate* them, mutate being another word for change. So in practice what does this actually mean? It means that you can not reassign in item once its in the tuple, unlike a list, where you can do a reassignment.
# 
# Let's see this in action:
# 
# ## Creating a Tuple
# 
# You use parenthesis and commas for tuples:

# In[1]:


t = (1,2,3)


# In[5]:


type(t)


# In[6]:


# Mixed data types are fine
t = ('a',1)


# In[7]:


# Indexing works just like a list
t[0]


# ## Immutability

# In[10]:


mylist = [1,2,3]


# In[11]:


type(mylist)


# In[12]:


# No problem for a list!
mylist[0] = 'new'


# In[13]:


mylist


# In[14]:


t = (1,2,3)


# In[15]:


t[0] = 'new'


# You also can't add items to a tuple:

# In[18]:


t.append('NOPE!')


# ## Tuple Methods
# 
# Tuples only have two methods available .index() and count()

# In[23]:


t = ('a','b','c','a')


# In[26]:


# Returns index of first instance!
t.index('b')


# In[27]:


t.count('a')


# ## Why use tuples?
# 
# Lists and tuples are very similar, so you may find yourself exchanging use cases for either one. However, you should use a tuple for collections or sequences that shouldn't be changed, such as the dates of the year, or user information such as an address,street, city , etc.
# 
# One interesting use of tuples involves for loops, we'll cover this later on when we discuss tuple unpacking. Excellent work so far recruit!
