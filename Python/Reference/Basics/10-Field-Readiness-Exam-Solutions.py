
# coding: utf-8

# # Field Readiness Exam
# ## Solutions
# ** Let's see how you performed Recruit! **
# _______

# ### Task 1
# 
# **Open the exam.txt file with Python and with only read permission and store the contents in a list called exam_lines**

# In[7]:


with open('exam.txt') as f:
    exam_lines = f.readlines()


# In[8]:


print(exam_lines)


# ### Task 2
# 
# How many lines does this file have?

# In[9]:


len(exam_lines)


# ### Task 3
# 
# Print out the 5th line of the text file.

# In[10]:


# Bit of a trick recruit! Recall that indexing starts as zero!
print(exam_lines[4])


# ### Task 4
# 
# Grab the last line of the text file and save it to a variable called last.

# In[11]:


last = exam_lines[-1]


# In[44]:


last


# ### Task 5
# 
# Use indexing to grab the letter 'o' from the last line of the file.

# In[45]:


last[5]


# ### Task 6
# 
# How could you use Python to count how many words there are in the last line?

# In[46]:


# This won't work because it returns the number of characters
len(last)


# In[47]:


last.split()


# In[48]:


# This is correct
len(last.split())


# ### Task 7
# 
# What data types are returned by the following lines of code:
# 
#     1.)  2/3
#     2.)  2 + 2.0
#     3.)  1 + 1
#     4.)  "2" + "2"
#     5.)  1 > 2
#     
# Try to do these in your head before checking by running the code in python.

# **Answers**
# 
# 1. Float
# 2. Float
# 3. Int
# 4. String
# 5. Boolean

# ### Task 8
# 
# Let's check how well you understand indexing and key calls. Here we present to you a set of dictionaries and lists that are nested inside a single dictionary **d**. While this is an unrealistic representation of how you would use these data types in the field, this is just for practice:

# In[49]:


d = {"levelone":[1,2,{'leveltwo':[5,6,[1,['get me please']]]}]}


# Your task is to retrieve the string "get me please" from the dictionary with stacked index and key calls.
# 
# Hint: Approach this step by step, slowly adding on more and more index calls. Recall that you can use .keys() to figure out what keys are in a  dictionary.

# In[50]:


# Let's show the solutions step by step


# In[51]:


d['levelone']


# In[52]:


d['levelone'][2]


# In[53]:


d['levelone'][2]['leveltwo']


# In[54]:


d['levelone'][2]['leveltwo'][2]


# In[55]:


d['levelone'][2]['leveltwo'][2]


# In[56]:


d['levelone'][2]['leveltwo'][2][1]


# In[57]:


# Previous one is still a list, we asked for a string!
d['levelone'][2]['leveltwo'][2][1][0]


# ### Bonus Task
# 
# How many unique integers are in this list? (You will need to use a casting method we haven't shown you yet)

# In[41]:


mylist = [1,2,3,4,5,6,4,3,2,1,2,3,4,5,6,6,7,8,5,6,7,8,9,8,9,8,9,7,10,123,1,2,2,3,1,3,2,4,1,4,4,1,2,2,22,3,4,1,4,1]


# In[42]:


set(mylist)


# In[43]:


len(list(set(mylist)))


# Excellent work recruit, now that you are done with the basics of data types and storage with Python, let's move on to learning about control flow with Python.
