#!/bin/python3

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    from collections import deque
    from copy import deepcopy


    d = open(dictionary_file)
    dictionary = d.read().split("\n")
    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)
    if start_word == end_word:
        return stack

    while len(queue) != 0:
        q  = queue.pop()
        dictionary_copy = deepcopy(dictionary)
        for i in dictionary_copy:
            if _adjacent(q[-1], i) is True:
                copy = deepcopy(q)
                copy.append(i)
                if i == end_word:
                    return copy
                queue.appendleft(copy)
                dictionary.remove(i)
    return None

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if len(ladder) == 1:
        return True
    elif len(ladder) == 2:
        for i in range(len(ladder)):
            if _adjacent(ladder[i], ladder[i+1]) == True:
                return True
    elif len(ladder) > 0 and len(ladder) != 1 and len(ladder) != 2:
        for i in range(len(ladder)-1):
            if _adjacent(ladder[i], ladder[i+1]) == True:
                continue
            else:
                return False
        return True
    else:
        return False

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
#   import math
 #  same = 0
#   for i in range(len(word1)):
#       if word1[i] == word2[i]:
#           same += 1
#       if abs(same-len(word1)) == 1:
#           return True
#       else:
#           return False
    from string import ascii_lowercase
    matches = []
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] in ascii_lowercase and word2[i] in ascii_lowercase:
                if word1[i] == word2[i]:
                    matches.append('1')

    if len(matches) >= len(word1) - 1:
        return True
    else:
        return False

