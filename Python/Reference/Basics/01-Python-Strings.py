
# coding: utf-8

# # Python Strings
# 
# Welcome back recruit! It is time for you to learn about one of most basic fundamental data types in Python, the string. What is a string? Formally, **a string is an ordered sequence of characters**. Two key words here, **ordered** and **characters.** Ordered means that we will be able to use *indexing* and *slicing* to grab elements from the string. Characters hints at the fact that strings are more flexible than just using the alphabet, we'll see they can also hold other types of characters.

# ## Creating strings.

# In[1]:


# Comment. Won't show up when you run a script.


# In[2]:


# Single or double quotes are okay.
'hello'


# In[3]:


"hello"


# In[4]:


# Keep in mind potential errors
'I'm not a spy!


# In[5]:


# Use another set of quotes to capture that inside single quote
" I'm not a spy! "


# ## Basic Printing of Strings
# 
# In the jupyter notebook, a single string in a cell is automatically returned back. However, this is different than printing a string. Printing a string allows us to have multiple outputs. Let's see some useful examples:

# In[6]:


'one'
'two'


# In[7]:


print('one')
print('two')


# In[8]:


print("Special Codes")
print('this is a new line \n notice how this prints')
print('this is a tab \t notice how this prints')
print("Notice how they both follow the general escape character of backslash ")


# ## Indexing and Slicing
# 
# Recall that strings are *ordered sequences* of characters in order. This means we can "grab" single characters (indexing) or grab sub-sections of the string (slicing).

# ### Indexing
# 
# Indexing starts a 0, so the string hello:
# 
#     character:    h    e    l   l   o
#     index:        0    1    2   3   4
#     
# You can use square brackets to grab single characters

# In[9]:


word = "hello"


# In[10]:


word[0]


# In[11]:


word[3]


# Python also supports reverse indexing:
# 
#     character:        h     e     l    l    o
#     index:            0     1     2    3    4
#     reverse index:    0    -4    -3   -2   -1  
#     
# Reverse indexing is used commonly to grab the last "chunk" of a sequence.

# In[12]:


word[-1]


# ### Slicing
# 
# We can grab entire subsections of a string with *slice* notation.
# 
# This is the notation:
# 
#     [start:stop:step]
# 
# Key things to note:
# 
# 1. The starting index direclty corresponds to where your slice will start
# 2. The stop index corresponds to where you slice will go up to. **It does not include this index character!**
# 3. The step size is how many characters you skip as you go grab the next one.
# 
# Let's see some examples

# In[13]:


alpha = 'abcdef'


# In[14]:


# NOTICE HOW d IS NOT INCLUDED!
alpha[0:3]


# In[15]:


alpha[0:4]


# In[16]:


alpha[2:4]


# In[17]:


alpha[2:]


# In[18]:


alpha[:2]


# In[19]:


alpha[0:6:2]


# ## Basic String Methods
# 
# Methods are actions you can call off an object usually in the form .method_name() notice the closed parenthesis at the end. Strings have many, many methods which you can check with the Tab functionality in jupyter notebooks, let's go over some of the more useful ones!

# In[25]:


basic = "Hello world I am still a recruit"


# In[26]:


basic.upper()


# In[27]:


basic.lower()


# In[28]:


# Preview, we'll learn about lists later on!
basic.split()


# In[29]:


basic.split('I')


# # Print Formatting
# 
# You can use the .format() method off a string, to perform what is formally known as **string interpolation**, essentially inserting variables when printing a string.

# In[ ]:


user_name = "Recruit"


# In[ ]:


print("Welcome {}".format(user_name))


# In[ ]:


action = 'run'


# In[ ]:


print("The {} needs to {}".format(user_name,action))


# In[ ]:


print("The {a} needs to {b}".format(a=user_name,b=action))


# In[ ]:


print("The {b} needs to {a}".format(a=user_name,b=action))


# ### Formatting Numbers

# In[ ]:


num = 123.6789
print("The code is: {}".format(num))


# In[ ]:


print("The code is: {:.1f}".format(num))


# In[ ]:


print("The code is: {:.2f}".format(num))


# In[ ]:


print("The code is: {:.3f}".format(num))


# In[ ]:


print("The code is: {:.4f}".format(num))


# Excellent work recruit!
