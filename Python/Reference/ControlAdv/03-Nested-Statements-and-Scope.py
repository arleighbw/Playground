
# coding: utf-8

# # Nested Statements and Scope
# 
# Welcome back recruit. After those Function Tasks you should now be a lot more comfortable writing functions. Later on we will see how functions can interact with each other as part of larger scripts, in order to continue this discussion, we need to learn about nested statements and scope. Its important to understand how Python deals with the variable and function names you assign. When you create a variable name in Python the name is stored in a name-space. Variable names also have a scope, the scope determines the visibility of that variable name to other parts of your code.
# 
# ### Simple Example
# Lets start with a quick thought experiment, imagine the following code:

# In[1]:


x = 'outside'

def report():
    x = 'inside'
    return x


# What do you expect the output of calling report() to be?

# In[2]:


report()


# Okay, that makes sense, as we see x was reassigned inside of the report() function. What do you think happens if we call print(x) outside of this function?

# In[4]:


print(x)


# The reason we don't see the effect of this reassignment outside of the function, is because of **scope**.

# ## Scope
# 
# This idea of scope in your code is very important to understand in order to properly assign and call variable names.
# 
# In simple terms, the idea of scope can be described by 3 general rules:
# 
# 1. Name assignments will create or change local names by default.
# 2. Name references search (at most) four scopes, these are:
#     * local
#     * enclosing functions
#     * global
#     * built-in
# 3. Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.

# The statement in #2 above can be defined by the LEGB rule.
# 
# **LEGB Rule.**
# 
# **L: Local ** — Names assigned in any way within a function (def or lambda)), and not declared global in that function.
# 
# **E: Enclosing function locals** — Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
# 
# **G: Global (module)** — Names assigned at the top-level of a module file, or declared global in a def within the file.
# 
# **B: Built-in (Python)** — Names preassigned in the built-in names module : open,range,SyntaxError,...

# ### Example of Local

# In[5]:


def report():
    
    # This is a local assignment
    x = 'local'
    print(x)


# ### Example of Enclosing Function Locals
# 
# Remember that this occurs when a function is inside of another function (we'll see more examples of this later, these are called nested functions, you won't use them that often as you start out programming).

# In[7]:


x = 'This is a global level'

def enclosing():
    x = 'Enclosing Level'
    
    def inside():
        # This function is inside enclosing
        # Notice the indentation
        print(x)
        
    # Now let's call inside()
    # Note the indentation
    inside()


# So what will happen when we call enclosing()? What will we see?

# In[8]:


enclosing()


# This means the inside() function first looks for the **x** variable locally. Since its not defined there, it looks at the enclosing level, it finds it defined there, so it can then print it out. Let's see what happens if it wasn't defined in the enclosing function (meaning it was global).
# 
# ### Global

# In[9]:


x = 'This is a global level'

def enclosing():
    # X is not defined inside this enclosing function either!
    
    def inside():
        # This function is inside enclosing
        # Notice the indentation
        print(x)
        
    # Now let's call inside()
    # Note the indentation
    inside()


# In[10]:


enclosing()


# ### Built-in
# 
# These are built-in functions and keywords, be careful not to overwrite these! If you variable name is already specially highlighted when you are typing it, its probably a built-in function!

# In[11]:


len


# In[12]:


sum


# In[13]:


list


# ### Local Variables vs Global Variables
# 
# Now that we've seen the levels, let's make sure we understand with another example:

# In[14]:


x = 'global outside'

def myfunc(x):
    
    print('X is {}'.format(x))
    
    x = 'redefined inside myfunc()'
    
    print('X is {}'.format(x))
    
    


# In[15]:


myfunc(x)


# In[16]:


print(x)


# ## global keyword
# Now there may be an occasion where you specifically want to overwrite the global variable inside of a function. How can you do that? You can use the **global** keyword before the variable to indicate you want to "grab" the global variable. Keep in mind this is generally not recommended, and you should try your best to avoid this until you become more experienced, because it becomes very easy to accidentally create errors this way by overwriting variables in one part of your script that effect the script in a completely different part. 
# 
# Let's see an example of the **global** keyword.

# In[20]:


x = 'global outside'

def myfunc():
    # Must declare global keyword before every using it
    # inside of the function.
    global x 
    
    print('X is {}'.format(x))
    
    x = 'redefined inside myfunc() with global keyword'
    
    print('X is {}'.format(x))
    
    


# In[22]:


myfunc()


# In[23]:


print(x)


# Excellent work recruit! Now this should help you build an understanding when you later on create scripts with multiple functions and variables!
