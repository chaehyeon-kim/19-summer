""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
def lines_from_file(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line)
    lines = [x.strip() for x in lines]
    return lines

def new_sample(path,i):
    lines=lines_from_file(path)
    return lines[i]

def analyze(sample_paragraph, typed_string, start_time, end_time):
    wpm=((len(typed_string)/5)/(end_time-start_time))*60
    k,total,count,ap=0,0,0,0.0
    words=split(sample_paragraph)
    wordt=split(typed_string)
    if len(words)<len(wordt):
        leng=len(words)
    else:
        leng=len(wordt)
    for word in range(leng):
        wordt=split(typed_string)
        if words[k]==wordt[k]:
            total+=1
        k+=1
        count+=1
        if len(words)<len(wordt):
            leng=len(words)
        else:
            leng=len(wordt)
        if count>0:
            ap=total/leng*100
        else:
            ap=0
    lst=[wpm,ap]
    return lst

def is_vowel(character):
    if character in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False


def pig_latin(wordt):
    if len(wordt) == 1:
        if not is_vowel(wordt[0]):
            return wordt + 'ay'
        else:
            return wordt + 'way'
    else:
        if is_vowel(wordt[0]):
            return wordt + 'way'
        elif not ( 'a' in wordt or 'e' in wordt or 'i' in wordt or 'o' in wordt or 'u' in wordt or 'A' in wordt or 'E' in wordt or 'I' in wordt or 'O' in wordt or 'U' in wordt ):
            return wordt + 'ay'
        else:
            i = 0
            while i < len(wordt):
                if is_vowel(wordt[i]):
                    return wordt[i:] + wordt[0:i] + 'ay'
                else:
                    i = i + 1

def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    lowest = 10000
    closest = ''
    for word in words_list: 
        word_score = score_function(user_input, word)
        if lowest > word_score:
            lowest, closest = word_score, word
    return closest

def swap_score(word1, word2):
    def helper(i, word1, word2):
        if not word1[0] or not word2[0]:
            return i
        elif word1[0] == word2[0]:
            return helper(i, word1[1:], word2[1:])
        else:
            return helper(i+1, word1[1:], word2[1:])
    return helper(0, word1, word2)

def swap_score(word1, word2):
    def helper(i, word_l1, word_l2):
        if word_l1 == '' or word_l2 == '':
            return i
        elif word_l1[0] != word_l2[0]:
            i += 1
        return helper(i, word_l1[1:], word_l2[1:])
    return helper(0, word1, word2)
# END Q1-5

# Question 6
def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""
    # BEGIN Q6
    def helper(i, word_l1, word_l2):
        if word_l1 == [] and word_l2 != []:
            return i + len(word_l2)
        elif word_l1 != [] and word_l2 == []:
            return i + len(word_l1)
        if word_l1 == [] or word_l2 == []:
            return i
        elif word_l1[0] not in word_l2 and word_l2[0] in word_l1:
            return helper(i+1, word_l1[1:], word_l2)
        elif word_l1[0] in word_l2 and word_l2[0] not in word_l1:
            return helper(i+1, word_l1, word_l2[1:])
        elif word_l1[0] not in word_l2 and word_l2[0] not in word_l1:
            word_l1[0] = word_l2[0]
            return helper(i+1, word_l1, word_l2)
        elif 1 < len(word_l1) and word_l1[0] != word_l2[0] and word_l1[1] == word_l2[0]:
            return helper(i+1, word_l1[1:], word_l2)
        elif word_l1[0] in word_l2 and word_l2[0] in word_l1:
            return helper(i, word_l1[1:], word_l2[1:])
    return helper(0, list(word1), list(word2))
    # END Q6
KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
	
def score_function_accurate(word1, word2):
    def helper(i, word_l1, word_l2):
        if word_l1 == [] and word_l2 != []:
            return i + len(word_l2)
        elif word_l1 != [] and word_l2 == []:
            return i + len(word_l1)
        if word_l1 == [] or word_l2 == []:
            return i
        elif word_l1[0] not in word_l2 and word_l2[0] in word_l1:
            return helper(i+1, word_l1[1:], word_l2)
        elif word_l1[0] in word_l2 and word_l2[0] not in word_l1:
            return helper(i+1, word_l1, word_l2[1:])
        elif word_l1[0] not in word_l2 and word_l2[0] not in word_l1:
            word_l1[0] = word_l2[0]
            return helper(i+1, word_l1, word_l2)
        elif 1 < len(word_l1) and word_l1[0] != word_l2[0] and word_l1[1] == word_l2[0]:
            return helper(i+1, word_l1[1:], word_l2)
        elif word_l1[0] in word_l2 and word_l2[0] in word_l1:
            return helper(i, word_l1[1:], word_l2[1:])
    score= helper(0, list(word1), list(word2))
    
    if len(word1) == len(word2):
        k=0
        score2=0
        for i in range(len(word1)):
            if word1[k]!=word2[k]:
                score2=score2+KEY_DISTANCES[word1[k],word2[k]]
                k+=1
            else:
                k+=1
        return score2
    return score
# END Q7-8
