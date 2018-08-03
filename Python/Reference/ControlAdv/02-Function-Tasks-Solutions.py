
# coding: utf-8

# # Function Tasks Solutions
# 
# Welcome Recruit! Let's see if you can solve these word problems by creating functions. The function "skeleton" has been set up for you to fill in below the problem description, as well as example outputs of what the function should return given certain inputs. Best of luck, some of these will be challenging! 
# 
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
# 
# ** Create a function that takes in two integers and returns True if their sum is 10, False if their sum is something else. **

# In[1]:


def check_ten(n1,n2):
    return (n1 + n2) == 10


# In[2]:


check_ten(10,0)


# In[3]:


check_ten(5,5)


# In[4]:


check_ten(2,7)


# ## Task 2
# 
# ** Create a function that takes in two integers and returns True if their sum is 10, otherwise, return the actual sum value. **

# In[5]:


def check_ten_sum(n1,n2):
    if (n1+n2) == 10:
        return True
    else:
        return n1+n2


# In[8]:


check_ten_sum(10,0)


# In[9]:


check_ten_sum(2,7)


# ## Task 3
# 
# Create a function that takes in a string and returns back the first character of that string in upper case.

# In[10]:


def first_upper(mystring):
    return mystring[0].upper()


# In[11]:


first_upper('hello')


# In[12]:


first_upper('agent')


# ## Task 4
# 
# **Create a function that takes in a string and returns the last two characters. If there are less than two chracters, return the string:  "Error". [Use this link if you need help/hint.](https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)**

# In[19]:


def last_two(mystring):
    if len(mystring) < 2:
        return "Error"
    else:
        return mystring[-2:]


# In[20]:


last_two('hello')


# In[21]:


last_two('hi')


# In[22]:


last_two('a')


# ## Task 5
# 
# ** Given a list of integers, return True if the sequence [1,2,3] is somewhere in the list. Hint: Use slicing and a for loop. **

# In[1]:


def seq_check(nums):
    
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        # Check in sets of 3 if we have 1,2,3 in a row
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False


# In[2]:


seq_check([1,2,3])


# In[4]:


seq_check([7,7,7,1,2,3,7,7,7])


# In[5]:


seq_check([3,2,1,3,2,1,1,1,2,2,3,3,3])


# ## Task 6
# 
# ** Given a 2 strings, create a function that returns the difference in length between them. This difference in length should always be a positive number (or just 0). Hint: Absolute Value.**

# In[27]:


def compare_len(s1,s2):
    return abs(len(s1)-len(s2))


# In[28]:


compare_len('aa','aa')


# In[29]:


compare_len('a','bb')


# In[30]:


compare_len('bb','a')


# ## Task 7
# 
# ** Given a list of integers, if the length of the list is an even number, return the sum of the list. If the length of the list is odd, return the max value in that list. **

# In[33]:


def sum_or_max(mylist):
    length = len(mylist)
    
    if length % 2 == 0:
        return sum(mylist)
    else:
        return max(mylist)


# In[34]:


sum_or_max([1,2,3])


# In[35]:


sum_or_max([0,1,2,3])


# ## Task 8
# 
# ** Agents in the field sometimes need to speak in code. Create a function that takes in a string name (e.g. "James", "Cindy", etc...) and replaces all vowels with the letter x. For our purposes, consider these letters as vowels: [a,e,i,o,u]). Then switch the position of the first and last letters.  **
# 
# **This task is challenging, break it down into multiple pieces. **

# In[41]:


def replace_and_switch(name):
    
    # Strings aren't mutable, so we need to use a list!
    # This creates a list of length name
    output = list(range(len(name))) 
    
    for i,letter in enumerate(name):
        if letter.lower() in ['a','e','i','o','u']:
            output[i] = 'x'
        else:
            output[i] = letter
    
    # Now switch first and last letter.
    last = output[-1]
    first = output[0]
    output[0] = last
    output[-1] = first
    
    # Join back together into a string
    return ''.join(output)


# In[42]:


replace_and_switch('James')


# In[43]:


replace_and_switch('Cindy')


# In[44]:


replace_and_switch("Alfred")


# Excellent work recruit! Later on you will be able to combine multiple functions to create large working pieces of code that accomplish complex tasks!
