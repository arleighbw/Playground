#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:19:56 2018

@author: arleighbw
"""
import string

#def encrypt(text,shift):
#    '''
#    INPUT: text as a string and an integer for the shift value.
#    OUTPUT: The shifted text after being run through the Caeser cipher.
#    '''
#    
#    # Create a normal plain alphabet
#    
#    # Create a shifted version of this alphabet 
#    # (Try slicing using the shift and then reconcatenating the two parts)
#    
#    # Use a for loop to go through each character in the original message.
#    # Then figure out its index match in the shifted alphabet and replace.
#    # It might be helpful to create an output variable to hold the new message.
#    
#    # Keep in mind you may want to skip punctuation with an if statement.
#    
#    # Return the shifted message. Use ''.join() method 
#    # if you still have it as a list.
    
def ceaserEncrypt(text,shift):
    encrypt = ""
    alphabet = list(string.ascii_lowercase)
    
    for letter in text.lower():
        encrypt = encrypt + alphabet[((alphabet.index(letter) + shift) % len(alphabet))]
    
    return encrypt

    

#    '''
#    INPUT: A shifted message and the integer shift value
#    OUTPUT: The plain text original message.
#    '''
#    
#    # Create a normal plain alphabet
#    
#    # Create a shifted version of this alphabet with the shift value.
#    
#    # Use a for loop to go through each character in the encrypted message.
#    # Then figure out its index match in the plain alphabet and replace.
#    # It might be helpful to create an output variable to hold the new message.
#    
#    # Keep in mind you may want to skip punctuation with an if statement.
#    
#    # Return the original message. Use ''.join() method 
#    # if you still have it as a list.
    
def ceaserDecrypt(text,shift):
    decrypt = ""
    alphabet = list(string.ascii_letters)
    
    for letter in text.lower():
        decrypt = decrypt + alphabet[((alphabet.index(letter) + len(alphabet) - shift) % len(alphabet))]

    return decrypt




def ceaser_brute_force(message):
    """
    INPUT: A shifted message
    OUTPUT: Prints out every possible shifted message. 
            One of the printed outputs should be readable.
    """
    
    # Use your previous decrypt() method and call it for every possible shift
    # using a For Loop.
    
    # Print out the result of each shift.
    
    
    
    
    
encTest = ceaserEncrypt("alex",2)
print(encTest)
print(ceaserDecrypt(encTest,2))
encTest = ceaserEncrypt("blayne",12)
print(encTest)
print(ceaserDecrypt(encTest,12))