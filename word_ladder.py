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
    import collections as cl
    import copy

    f = open('words5.dict')
    dictionary = f.readlines()
    
    if start_word in dictionary:
        dictionary.remove(start_word)

#   if end_word not in dictionary:
#       return 0

    dictionary.append(end_word)
    queue = cl.deque([[start_word, 1]])
    leng = len(start_word)
    ladder = []
    while queue:
        word, length = queue.popleft()
        ladder.append(word)
        if word == end_word:
            return ladder
        dictionary_copy = dictionary.copy()
        for n in dictionary_copy:
            if sum(n[i] != word[i] for i in range(leng)) == 1:
                dictionary.remove(n)
                queue.append([n, length+1])
    return 0

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    for i in range(len(ladder) - 1):
        if _adjacent(ladder[i], ladder[i+1]) == True:
            return True

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    matches = []
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                matches.append('1')

    if len(matches) >= len(word1) - 1:
        return True
    else:
        return False
