
# coding: utf-8

# # Dictionaries
# 
# So far we've only seen how to store data types in sequences like storing characters in a string or items in a list. But what if we want to store information another way? Most programming languages have what is called a *hash table*, which is a key-item pairing. Under the hood, this allows for faster look up times of objects (at the "cost" of not being able to sort the data), practically it allows for us to store data with a mapping. 
# 
# The choice of deciding between sequences like a list and mappings like a dictionary often depends on the specific situation. As you become a stronger programmer, choosing the right storage format will become more intuitive.
# 
# Let's cover the basics of dictionaries!

# ## Creating a Dictionary

# In[9]:


# Make a dictionary with {} and : to signify a key and a value
d = {'key1':'value1','key2':'value2'}


# In[10]:


# Call values by their key
d['key1']


# In[11]:


d['key2']


# ### Adding New Key-Item Pairs

# In[12]:


d['new_key'] = 'new item'


# In[13]:


d


# ** Note: Dictionaries are unordered! *This may not be clear at first with smaller dictionaries, but as dictionaries get larger they won't retain order, which means they can not be sorted!* If you need order and the ability to sort, stick with a sequence, like a list! One last time -- A DICTIONARY IS AN UNORDERED MAPPING. THIS IS NOT IMMEDIATELY OBVIOUS WITH SMALL DICTIONARIES!**

# In[48]:


d = {'a':1,'z':2}


# In[49]:


d


# In[50]:


d['new'] = 0


# In[51]:


d


# In[52]:


d['za'] = 'hello'


# In[53]:


d


# Dictionaries are very flexible in the data types they can hold, they can hold numbers, strings, lists, and even other dictionaries!

# In[54]:


d = {'k1':10,'k2':'stringy','k3':[1,2,3,],'k4':{'inside_key':100}}


# In[55]:


d


# In[56]:


d['k1']


# In[57]:


d['k2']


# In[58]:


d['k3']


# In[60]:


d['k3'][0]


# In[61]:


d['k4']


# In[63]:


d['k4']['inside_key']


# Error if you ask for a key that isn't there!

# In[65]:


d['oops']


# Keep dictionaries in mind when you need to create a mapping and don't care about order! 
# 
# For example:
# 
# https://en.wikipedia.org/wiki/Secret_Service_code_name

# In[70]:


code_names = {"Obama":'Renegade',
             "Bush":'Trailblazer',
             "Reagan":"Rawhide",
             "Ford":"Passkey"}


# In[71]:


code_names["Ford"]


# Or populations:
# 
# https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)

# In[72]:


pop_in_mil = {"USA":323,
      "Germany": 83,
      "India": 1324}


# In[73]:


pop_in_mil["USA"]


# ## Methods

# In[75]:


code_names.keys()


# In[76]:


code_names.values()


# In[77]:


code_names.items()


# Great work recruit, we're almost done with your basics bootcamp. Just need to learn about sets and tuples, working with files, and you will be on your way to your first field readiness exam!
