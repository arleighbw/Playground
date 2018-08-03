
# coding: utf-8

# # Sets
# 
# It's time to quickly cover another fundamental data structure recruit! The Set!
# 
# Sets are an unordered collection of unique elements. We can construct them by using the set() function. Let's go ahead and make a set to see how it works:

# ## Constructing Sets

# In[1]:


x = set()


# In[2]:


x.add(1)


# In[3]:


x


# In[5]:


x.add(2)


# In[6]:


x


# Note the curly brackets. This does not indicate a dictionary! Although you can draw analogies as a set being a dictionary with only keys.
# 
# We know that a set has only unique entries. So what happens when we try to add something that is already in a set?

# In[7]:


x.add(1)


# In[8]:


x


# Notice how it won't place another 1 there. That's because a set is only concerned with unique elements! We can cast a list with multiple repeat elements to a set to get the unique elements. For example:

# In[9]:


mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]


# In[10]:


set(mylist)


# You can also quickly create a set with just {}

# In[11]:


myset = {1,2,3}


# In[12]:


type(myset)

