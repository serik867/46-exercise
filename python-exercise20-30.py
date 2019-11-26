#21- write a function char_freq() that takes a string and builds a frequency listing of the characters contained
# in it. Represent the frequency listing as a Python dictionary. Try it with something like 
# char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(_str):
    _dict=dict()

    for i in _str:
        if i in _dict.keys():
            _dict[i]+=1
        else:
            _dict[i]=1
    
    return _dict

print(char_freq("abbabcbdbabdbdbabababcbcbab"))
print(char_freq("cacacacacacacacacacacacacacacac"))
print(char_freq("abbabcbdbabdbdbabababcbcbabhfhfhfhfhfhfhffhfhksksks"))


# 22-In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain 
# text is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 
# 3, A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who used 
# it to communicate with his generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar 
# cipher where the shift is 13. In Python, the key for ROT-13 may be represented by means of the following 
# dictionary:
# key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
#        'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
#        'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
#        'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
#        'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
#        'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
#        'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
# Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, 
# you will be able to read the following secret message:
#    Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
# Note that since English has 26 characters, your ROT-13 program will be able to both encode and 
# decode texts written in English.
# 
def ceaser_cipher(_str):
    keys = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    _list = _str.split(" ")
    new_word=""
    new_words=[]

    for word in _list:
        for i in range(len(word)):
            if word[i] in keys.keys():
                new_word+=keys[word[i]]
            else:
                new_word+=word[i]
        new_words.append(new_word)
        new_word=" "
    return " ".join(new_words)

print(ceaser_cipher("AlAl alaa"))
print(ceaser_cipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"))

# 23-Define a simple "spelling correction" function correct() that takes a string and sees to it that 1) 
# two or more occurrences of the space character is compressed into one, and 2) inserts an extra space after
# a period if the period is directly followed by a letter. E.g. correct("This   is  very funny  and    cool.
# Indeed!") should return "This is very funny and cool. Indeed!" Tip: Use regular expressions!
# 
# 
# 
# 
# 
# The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:
# If the verb ends in y, remove it and add ies
# If the verb ends in o, ch, s, sh, x or z, add es
# By default just add s
# Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns its third person singular form. Test your function with words like try, brush, run and fix. Note however that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all cases. Tip: Check out the string method endswith().
# In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:
# If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# If the verb ends in ie, change ie to y and add ing
# For words consisting of consonant-vowel-consonant, double the final letter before adding ing
# By default just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases.
# Higher order functions and list comprehensions
# Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?
# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.
# Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.
# Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. Use the higher order function map() to write a function translate() that takes a list of English words and returns a list of Swedish words.