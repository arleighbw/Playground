
# coding: utf-8

# # Control Flow Basics
# ## if , elif , and else statements
# 
# Welcome back recruit! Often when coding out small scripts, we'll need to control the flow of our logic. Our program will want to perform an action in only certain cases, we can use the **if**, **elif**, and **else** statements to control for these cases. Let's work through some examples:

# ## Simple if Statement
# The format for an if statement
# 
#     if some_condition:
#         # Do Something
# 

# In[1]:


if 1<2:
    print('One is less than two')


# In[2]:


if 1>2:
    print("One is greater than two")


# Notice what happens, the indented block of code only runs when the if condition is True!

# ## if else Statement
# 
# Let's now add in an alternate action in case the **if** is not True using the **else** statement.
# 
# Notice the format and how the code blocks line up, this is crucial in Python! Code indentation let's Python know what blocks and statements correspond together.

# In[4]:


if 1==1:
    print("One is equal to One")
else:
    print("First if was not True")


# In[5]:


if 1==2:
    print("One is equal to Two")
else:
    print("First if was not True")


# ## if, elif, else 
# 
# Now let's imagine we have multiple conditions to check before the final **else** statement, this is where we can use the **elif** keyword to check for as many individual conditions as necessary:

# In[6]:


if 2 == 0:
    print('First condition True')
elif 2 == 1:
    print("Second condition True")
elif 2 == 2:
    print("Third condition True")
else:
    print("None of the above conditions were True")


# In[8]:


if 2 == 0:
    print('First condition True')
elif 2 == 1:
    print("Second condition True")
elif 2 == 100:
    print("Third condition True")
else:
    print("None of the above conditions were True")


# Let's see what happens if we had multiple True conditions:

# In[9]:


if 2 == 2:
    print('First condition True')
elif 2 == 2:
    print("Second condition True")
elif 2 == 2:
    print("Third condition True")
else:
    print("None of the above conditions were True")


# Notice how only the first True condition's code block will be executed, keep this in mind when writing your scripts!

# It is important to keep a good understanding of how indentation works in Python to maintain the structure and order of your code. We will touch on this topic again when we start building out functions!

# ## Final Example
# 
# Let's see one final example.

# In[13]:


agent_code = 231912
access = False


# In[14]:


if agent_code == 12345:
    print('Code Reset')
    print("Please call a supervisor")
elif agent_code == 231912:
    print('Welcome Agent')
    print('Setting Your Access to True')
    access = True
else:
    print("Sorry Wrong Code Supplied")
    
# Now we can actually start another set of control flow logic here

if access == True:
    print('Access Granted')
else:
    print('Access Denied')


# Take a look at the last set of if/else block,since the variable **access** itself is a boolean, we also could have written it like this:

# In[16]:


if access:
    print("Access Granted")
else:
    print("Access Denied")


# Writing code like we just did in the above cell is cleaner, and you can name your variables differently to also make it even more legible (e.g. rename **access** to **access_granted** so you have **if access_granted** )
