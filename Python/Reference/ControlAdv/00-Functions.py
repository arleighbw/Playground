
# coding: utf-8

# # Functions
# 
# Welcome to your third stage of recruitment! This is where you will really begin to realize the power of Python and be able to create reproducible code that actually accomplishes tasks and solves problems.
# 
# The basis for reproducible code is the **function**.

# Formally, a function is a useful device that groups together a set of statements so they can be run more than once. They can also let us specify parameters that can serve as inputs to the functions.
# 
# On a more fundamental level, functions allow us to not have to repeatedly write the same code again and again. If you remember back to the lessons on strings and lists, remember that we used a function len() to get the length of a string. Since checking the length of a sequence is a common task you would want to write a function that can do this repeatedly at command.
# 
# Functions will be one of most basic levels of reusing code in Python, and it will also allow us to start thinking of program design (we will dive much deeper into the ideas of design when we learn about Object Oriented Programming).

# ## The def Statement
# 
# To create a function we use the **def** keyword. This is the general form of a function:

# In[1]:


def lowercase_function_name(argument1,argument2,argument3='default value'):
    '''
    This is the DocString of the function. It is where you can write a helpful 
    description for anyone who will use your function.
    '''
    # After the docstring you write code that does stuff.


# We begin with def then a space followed by the name of the function. Try to keep names relevant, for example len() is a good name for a length() function. Also be careful with names, you wouldn't want to call a function the same name as a built-in function in Python (such as len).
# 
# Next come a pair of parenthesis with a number of arguments separated by a comma. These arguments are the inputs for your function. You'll be able to use these inputs in your function and reference them. After this you put a colon.
# 
# Now here is the important step, you must indent to begin the code inside your function correctly. Python makes use of whitespace to organize code. Lots of other programing languages do not do this, so keep that in mind.
# 
# Next you'll see the doc-string, this is where you write a basic description of the function. Using iPython and iPython Notebooks, you'll be able to read these doc-strings by pressing Shift+Tab after a function name. Doc strings are not necessary for simple functions, but its good practice to put them in so you or other people can easily understand the code you write.

# ____
# 
# **Let's now walk through lots of examples of different functions.**
# ___

# ### Example 1

# In[5]:


def report_agent():
    print("Reporting Agent")


# If you call the function without parenthesis it won't run, instead it will just report back what the object is:

# In[6]:


report_agent


# Use parenthesis to run the function:

# In[7]:


report_agent()


# ### Example 2
# ** Passing in arguments/parameters **

# In[8]:


def report(name):
    print("Reporting {}".format(name))


# In[9]:


# Notice the error
report()


# In[10]:


report('Bond')


# ### Example 3
# ** Default arguments can be used to set a default value. **

# In[11]:


def report(name='Jason'):
    print('Reporting {}'.format(name))


# In[12]:


report()


# In[13]:


report('Kay')


# ## The return keyword
# So far all of our functions have only been printing results, but what if we wanted to save the actual results of a function to another variable? How could we do this? Let's first see what happens with just print()

# In[25]:


def add(n1,n2):
    print(n1+n2)


# In[26]:


add(2,3)


# In[27]:


result = add(2,3)


# In[28]:


result


# In[29]:


type(result)


# Notice how we aren't able to save the result of the print() function. That is because it is not **returning** anything. Let's now use the return keyword.

# In[30]:


def add(n1,n2):
    return n1+n2


# In[32]:


add(2,3)


# Notice how jupyter is reporting an output with Out[]. We can actually assign this result

# In[33]:


result = add(2,3)


# In[34]:


result


# In[35]:


result


# In[36]:


result


# ### Solving Problems with Functions
# 
# Functions are a core building block for scripts and code. Let's show how you could solve a problem with a function.

# ** Write a function that returns a boolean (True/False) indicating if the word 'secret' is in a string. **

# In[38]:


def secret_check(mystring):
    return 'secret' in mystring


# In[39]:


secret_check('This is a secret.')


# In[40]:


secret_check('SECRET')


# We can fix this with .lower()

# In[41]:


def secret_check(mystring):
    return 'secret' in mystring.lower()


# In[43]:


secret_check('SECRET!')


# _____

# ** Create a code maker function. This function will take in a string name and replace any vowels with the letter x.**

# In[53]:


def code_maker(mystring):
    output = list(mystring)
    for i,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = 'x'
    
    output = ''.join(output)     
    return output


# Let's see what **''.join(output)** does:

# In[54]:


''.join(['a','b','c'])


# In[55]:


'--'.join(['a','b','c'])


# In[56]:


'-x-'.join(['a','b','c'])


# In[57]:


code_maker('Edward')


# In[58]:


code_maker('John')


# Excellent work recruit! Since functions are crucial to becoming a competent Python programmer, up next we will have some tasks for you to complete with functions. Good luck!
