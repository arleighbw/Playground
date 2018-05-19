
# coding: utf-8

# # While Loops
# 
# Now that we understand control flow with if, elif,and else statements let's learn about loops. The first loop we will learn about is the **while loop**.
# 
# A while loop will repeatedly execute a single statement or group of statements as long as the condition being checked is true. The reason it is called a 'loop' is because the code statements are looped through over and over again until the condition is no longer met.
# 
# Code indentation becomes very important as we begin to work with loops and control flow. Let's work through some examples recruit!

# In[1]:


# Start by setting variable x to 0
x = 0

while x < 3:
    print('X is currently')
    print(x)
    print("Adding 1 to x")
    x = x + 1 #alternatively you could write x += 1


# ____
# #### Cautionary Note!
# Be careful with while loops! There is a potential to write a condition that always remains True, meaning you have an infinite running while loop. If this happens to you, try using Ctrl+C to kill the loop. Often in a notebook setting that won't work, so you can try to restart the kernel. If that still doesn't work, use Ctrl+C at the command line running the notebook. Still not working recruit? Oh boy, you're in trouble now! Try restarting your computer :)
# ____
# Let's move on with some more examples. First let's show you how to accept an input from a user:

# In[3]:


# Run this cell only once
# If you run it again without providing an
# input your cell will get stuck with In[*] 
# To fix this, restart the kernel.

# Okay, now for the code

saved_input = input("Please input a number: ")


# In[4]:


saved_input


# Notice its a string! You can always cast it with **int()** or **float()** to get a int or float to work with.
# 
# Let's see how we could use this:

# In[8]:


print("Welcome Agent")
# start with some default passcode (needs to be defined before while loop starts)
passcode = 0

while passcode != 123:
    passcode = int(input("Please provide your passcode: "))

# This won't run until the while loop is 
# done because of the indentation
print("Correct Passcode!")


# In[9]:


print("Welcome Agent")
# start with some default passcode (needs to be defined before while loop starts)
passcode = 0

while passcode != 123:
    passcode = int(input("Please provide your passcode: "))

    #Nested control flow logic
    if passcode != 123:
        print("Sorry wrong passcode provided")
        print("Try Again")
        print('\n')
    
# This won't run until the while loop is 
# done because of the indentation
print("Correct Passcode!")


# # break keyword

# 
# The break keyword allows you to "break" out of the loop that contains the break keyword. For example

# In[10]:


x = 0

while x < 10:
    print(x)
    print('add one to x')
    x += 1
    
    if x == 3:
        # This will cause to break out of the top loop 
        # Note that if statements don't count as loops
        break


# Excellent work recruit! Let's move on to discuss for loops!
