# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 07:58:00 2019

Problem Set 2

#1 Lex index as a linear order of input
#2 Weight of a Word

@author: sl288
"""


from nose.tools import ok_

# =============================================================================
# Problem 1
# This program finds the lexicographically index as a linear order in which the 
# list is passed as a linear order on [0, 1, ... , n - 1]
# =============================================================================

import math

def lin_lex_index(word):
    length = len(word)
    lex_index = 0
    k = 0
    
    for word_index in range(length):        
        k = base_k(word, word_index)        
        lex_index += k * math.factorial(length - word_index - 1)
        
    return lex_index

"""
    Sub-function of lin_lex_index()
    Calculates the k digit that is changed in each places.
"""
def base_k (word, word_index):
    k = 0
    for next_letter in word[word_index :]:
        if next_letter < word[word_index]:
            k += 1
            
    return k

#Code Test
ok_(17 == lin_lex_index([3, 6, 2, 1]))
ok_(13 == lin_lex_index([9, 2, 10, 5]))
ok_(1 == lin_lex_index([4, 3]))
ok_(2 == lin_lex_index([2, 1, 3]))
ok_(35 == lin_lex_index([1, 2, 4, 3, 0]))
ok_(0 == lin_lex_index(list(range(0, 1000))))
lin_lex_index(list(range(500, 0, - 1))) #checked by factorial of 500 in calculator 



# =============================================================================
# Problem 2
# This program finds all the cominbation of words by starting with weight_word 
# function which the word_find will make new words during enumeration, which
# the weight() will check the weight of the word before prepending the word in
# the list.
# Note: Empty word has a weight of zero.
# =============================================================================

""" 
Pass n twice, for word_find for n as a counter and the limit of the n
    to check satisfy the conidition of weight of a word when a word of length 
    n is created
"""

def weight_words(l, n, w):
    assert (n >= 0)
    return word_find(l, n, w, n)
    
"""
    Sub-function of weight_word()
    Prepends the element to the list if the weight() function is True for 
    satisfying its weight parameter
"""

def prepend (words, element, w, n):
    word_prepend = []
    
    for word in words:
        if(weight([element] + word, w, n)):
            word_prepend.append([element] + word)
            
    return word_prepend

"""
    Sub-function of weight_word()
    Checks the weight of the word passed as a parameter. Returns the boolean
    value to the calling function, prepend() (above), to determine whether to 
    include the word in the list or not. 
"""
    
def weight(word, w, n):
    weight_calc= sum(word)
    
	# since the word is still increasing, the weight can be less than the expected weight w
    if(len(word) < n):
        if(weight_calc <= w):
            return True
        
    # for the final check, when the word is composed with n letters,
    # the word has to have weight of w before it is decided to be prepended
    # to a list
    
    elif(len(word) == n):
        if(weight_calc == w):
            return True
        
    else:
        return False

"""
    Sub-function of weight_word()
    Prepending the words to the list.
"""

def word_find(l, n, w, k):
    if n == 0:
        return [[]]
    
    list_weighted = []
    words = word_find(l, n - 1, w, k)

    for element in l:
        new_words = prepend(words, element, w, k)
        list_weighted.extend(new_words)
        
    return list_weighted



#Code Test
ok_([] == weight_words([4, 25], 3, 5))
ok_([[90, 13], [13, 90]] == weight_words([90, 13], 2, 103))
ok_([] == weight_words([2, 9, 13], 3, 0))    
ok_([[16]] == weight_words([16], 1, 16))    

#Note that the following two cases are in inverse order of each other.
ok_([[10, 10, 6], [10, 6, 10], [6, 10, 10]] == 
    weight_words([1, 5, 10, 2, 6, 4, 7], 3, 26))
ok_([[6, 10, 10], [10, 6, 10], [10, 10, 6]] == 
    weight_words([7, 4, 6, 2, 10, 5, 1], 3, 26))
ok_([[10, 10, 5, 5, 5, 5], [10, 5, 10, 5, 5, 5], [10, 5, 5, 10, 5, 5], 
      [10, 5, 5, 5, 10, 5], [10, 5, 5, 5, 5, 10], [5, 10, 10, 5, 5, 5],
      [5, 10, 5, 10, 5, 5], [5, 10, 5, 5, 10, 5], [5, 10, 5, 5, 5, 10],
      [5, 5, 10, 10, 5, 5], [5, 5, 10, 5, 10, 5], [5, 5, 10, 5, 5, 10],
      [5, 5, 5, 10, 10, 5], [5, 5, 5, 10, 5, 10], [5, 5, 5, 5, 10, 10]] == 
    weight_words([20, 14, 10, 5], 6, 40))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
