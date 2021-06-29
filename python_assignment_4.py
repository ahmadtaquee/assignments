#!/usr/bin/env python
# coding: utf-8

# ### Problem 1.1
# Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# 
# - area = (s* (s-a)* (s-b)* (s-c)) ** 0.5 
# 
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# In[38]:


class triangle:
    
    # constructor - sides of a triangle
    def __init__(self, side_a, side_b, side_c):
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
    # subclass: calculate_area
    # parentclass: triangle
class calculate_area(triangle):
    
    def __init__(self, side_a, side_b, side_c):
        
        # inheriting the property of 'triangle' class i.e. sides of the triangle
        super(calculate_area, self).__init__(side_a, side_b, side_c)
               
    # own method - calculating the area of a triangle
    def area(self):
        
        # perimerter of a triangle
        s = (self.side_a + self.side_b + self.side_c)

        # area of a triangle
        area = (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))**0.5

        # returning the area of a triangle
        return area
    


# In[43]:


cal_area = calculate_area(3,4,5)  # creating a 'cal_area' object

# calling the 'area' method to calculate the area of a triangle

cal_area.area()


# In[ ]:





# In[ ]:





# ### Problem 1.2
# Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.
# 

# In[12]:


filter_list = []   # empty list to store the words which will be greater than a certain length


# takes the input of the words from the users and stored in a list
mylist = input('Enter list of words seperated by space: ').split() 

# min. length of the words we don't want to store
word_length = int(input('Enter length of the word: ')) 


def filter_long_words(input_list, input_number):
    
    '''
    filter_long_words function takes two arguments: first as a list and second as a integer, length of a word
    and returns the list of words which are longer then integer
    
    '''
    
    # iterating over the input_list
    for i in range(len(input_list)):
        
        # comparing the length of words from the input_list to the input_number
        if (len(input_list[i]) > input_number):
            
            # appending those words in filter_list which are longer than input_number
            filter_list.append(input_list[i])
    
    # returning the final filter_list after appending all the words
    return filter_list


# In[13]:


# calling the filter_long_words funtion

filter_long_words(mylist, word_length)


# In[ ]:


## 2nd method - not working properly

# m = []
# k = []


# def filter_long_words():
    
#     n = int(input('enter length: '))
    
#     input_string = input("Enter words:  ")

#     my_list = input_string.split(" ")

#     for i in range(len(my_list)):
#         if len(my_list[i]) > n:
#             k.append(my_list)
#             break
            
            
# filter_long_words()


# In[ ]:





# ### Problem 2.1 
# Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# 
# Hint: If a list [ ab, cde, erty ] is passed on to the python function output should come as [2,3,4]
# 
# Here 2,3 and 4 are the lengths of the words in the list.

# In[10]:


# First Method -

# takes the input of the words from the users and stored in a list
input_words = input('Enter list of words seperated by space: ').split()

# to store the length of the input_words
length_input_words = []


def calculate_length_words(input_list):
    
    '''
    calculate_length_words function takes one argument as a list 
    and returns the length of the words which are in input_list.
    
    '''
        
    # iterate over the input_list 
    for i in range(len(input_list)):
        
        # appending the length of the words in the length_input_words list
        length_input_words.append(len(input_list[i]))
        
    # returning the final list with length of each word
    return length_input_words


# In[11]:


# calling the calculate_length_words

calculate_length_words(input_words)


# In[ ]:





# In[6]:


## 2nd Method - 

# takes the input of the words from the users and stored in a list
input_words = input('Enter list of words seperated by space: ').split()


def calculate_length_words(input_list):
    
    '''
    calculate_length_words function takes one argument as a list 
    and returns the length of the words which are in input_list.
    
    '''
    
    # lambda function calculate the length of each word from the input_list
    # and returning it in a list
    
    return list(map(lambda x: len(x), input_list))


# In[7]:


calculate_length_words(input_words)


# In[ ]:





# ### Problem 2.2 
# Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.

# In[3]:


def check_vowel(char):
    
    '''
    check_vowel function will take only one argument as a character 
    and returns True if it is a vowel, or else False
    
    '''
    
    vowels = 'aeiou'  # storing the vowels in a 'vowels' variable
    
    # iterating over the 'vowels'
    for i in vowels:
        
        
        # comparing the small character to the 'vowels'
        if (char.lower()) == i:
            
            return True  # returinng True if 'char' is vowel and coming out from the loop using break
            break
        
    else:
        
        # returining False if 'char' is not a vowel
        return False
    


# In[5]:


# calling the check_vowel function

check_vowel('u')


# In[ ]:





# In[ ]:





# ### Assignment 3 - END

# ### Write your feedback please.

# In[ ]:




