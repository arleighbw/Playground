
# coding: utf-8

# # Python Lists
# 
# We've learned that strings are sequences of characters. Similarly, lists are sequences of objects, they can hold a variety of data types in order, and they follow the same sequence and indexing bracket rules that strings do. They can also take in mixed data types. 
# 
# Let's explore some useful examples:

# In[15]:


my_list = [1,2,3]


# In[16]:


my_list


# In[17]:


my_list2 = ['a','b','c']


# In[18]:


my_list2


# In[13]:


a = 100
b = 200
c = 300
my_list3 = [a,b,c]


# In[22]:


my_list


# ## Indexing and Slicing
# 
# This works the same as in a string!

# In[26]:


mylist = ['a','b','c','d']


# In[27]:


mylist[0]


# In[28]:


mylist[0:3]


# ### The len function
# 
# Python has built in functions that you can call. We'll slowly introduce more of them as we need them. One useful built in function is the **len** function which returns back the length of an object. Notice how its syntax highlighted, indicating that its a built in function. If you see this auto-highlighting occur when choosing your own variable name, then you should choose a different variable name, so you don't accidentally overwrite the function.

# In[29]:


len('string')


# In[30]:


len(my_list)


# ## Useful List Methods
# 
# Methods are actions you can call off a function. Their typical format is:
# 
#     mylist = [1,2,3]
#     mylist.some_method()
#     
# You must call the parenthesis to execute the method! Let's go through a few useful ones pertaining to lists.

# In[31]:


mylist = [1,2,3]


# In[32]:


mylist.append(4)


# In[33]:


mylist


# In[34]:


mylist.pop()


# In[35]:


mylist


# In[36]:


mylist.append


# In[37]:


mylist.append(4)


# In[38]:


mylist


# In[39]:


item = mylist.pop()


# In[40]:


item


# In[41]:


mylist


# In[42]:


first_item = mylist.pop(0)


# In[43]:


first_item


# In[49]:


mylist


# In[50]:


mylist = [1,2,3]


# In[51]:


# This method doesn't return anything.
# Instead it performs the action "in-place" , or on the list itself without returning anything.
mylist.reverse()


# In[52]:


mylist


# In[56]:


# Also in place
mylist.sort()


# In[57]:


mylist


# In[58]:


# THIS WON'T WORK!
result = mylist.reverse()


# In[60]:


# Doesn't return anything
result


# In[61]:


print(result)


# In[66]:


mylist = [1,2,3]
mylist.insert(0,'NEW')


# In[67]:


mylist


# ## Nested Lists
# 
# Lists can hold other lists! This is called a nested list. Let's see some examples.

# In[68]:


new_list = [1,2,3,['a','b','c']]


# In[69]:


type(new_list)


# In[70]:


new_list[3]


# In[71]:


new_list[3][0]


# That is all for now, we'll be using lists a lot throughout your training!
