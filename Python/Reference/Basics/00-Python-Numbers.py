
# coding: utf-8

# # Python Numbers
# 
# Welcome recruit! It is time for you to begin your bootcamp by learning the basics. While these ideas may seem simple, they're fundamental enough that we should quickly go over them before tackling more complex topics. Let's begin by discussing the very basics of working with numbers in Python. This should be straight forward.

# ## Main Types of Numbers
# 
# Integers are whole numbers. Float (floating point) numbers are numbers with a decimal point.

# In[1]:


100


# In[2]:


type(100)


# In[3]:


1.2


# In[4]:


type(1.2)


# In[5]:


type(100.0)


# In[6]:


type(100.)


# ### Basic Arithmetic

# In[7]:


#Addition
1+1


# In[8]:


# Subtraction
2-1


# In[9]:


# Multiplication
2*2


# In[41]:


# Division
3/2


# In[42]:


# Division always returns floats!
1/1


# In[11]:


# Powers
2 ** 3


# In[12]:


2 ** (1/2)


# In[13]:


# Order of Operations
1 + 2 * 1000 + 1


# In[14]:


(1 + 2) * (1000+1)


# # Assigning Variables

# In[15]:


a = 2


# In[16]:


type(a)


# In[17]:


a + 3


# In[18]:


b = 3


# In[19]:


a + b


# In[28]:


# Reassignment
a = 1000


# In[29]:


a + b


# ### Reassignment with same variable

# In[30]:


a


# In[31]:


# Keep in mind, if you run this more than once, you will keep running a = a+a!
a = a + a


# In[32]:


a


# In[33]:


a = a + a


# In[34]:


a


# ## Simple Example

# In[36]:


message = 111
hash_code = 346728236


# In[37]:


secret_message = message * hash_code


# In[38]:


secret_message


# In[39]:


decrypted_message = secret_message / hash_code


# In[40]:


decrypted_message


# Excellent work recruit! Time to move on to the other basic data types.
