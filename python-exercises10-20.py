
#11-Define a function generate_n_chars() that takes an integer n and a character c and returns a string, 
# n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the 
# string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate 
# to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)
def generate_n_chars(num,char):
    res=""
    for i in range(num):
        res+=char
    
    return res

print(generate_n_chars(10,"A"))



# 12-Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram(x:list):
    for i in  x:
        print(generate_n_chars(i,"*"))

histogram([4,8,9,10,11,12,13,14,15,16,17,18])


# 13-The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two
# and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot 
# tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns 
# the largest one.
def max_in_list(y:list):
    num=0
    for i in y:
        if i>num:
            num=i
    return num

print(max_in_list([2,23,45,7,87,23,34,56]))

# 14-Write a program that maps a list of words into a list of integers representing the lengths of the 
# correponding words.
def word_of_list(y:list):
    res=[len(word) for word in y]
    return res

print(word_of_list(["Sero","Bla", "mama", "hahaha","python", "so", "fun"]))

# 15-Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
def find_longest_word(y:list):
    list_len=word_of_list(y)
    return max(list_len)

print(find_longest_word(["Sero","Bla", "mama", "hahaha","python", "so", "fun"]))

# 16-Write a function filter_long_words() that takes a list of words and an integer n and returns the list of 
# words that are longer than n.
def filter_long_words(y:list,n):
    res = [word for word in y if len(word)>n]
    return res

print(filter_long_words(["Sero","Bla", "mama", "hahaha","python", "so", "fun"],3))

# 17-Write a version of a palindrome recognizer that also accepts phrase palindromes such as 
# "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
# "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", 
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
def polndrome_recognizer(y:str):
    symbols=[" ","'",",","?","!","."]
    for i in symbols:
        y=y.replace(i,"")
    
    if y.lower() == reverse(y.lower()):
        return True
    else:
        return False

def reverse(x:str):
    str1=""
    for i in x:
        str1=i+str1
    
    return str1

print(polndrome_recognizer("Was it a rat I saw?"))
print(polndrome_recognizer("Sedar dudu"))
print(polndrome_recognizer("Dammit, I'm mad!"))
print(polndrome_recognizer("Rise to vote sir"))

# 18-A pangram is a sentence that contains all the letters of the English alphabet at least once, 
# for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function 
# to check a sentence to see if it is a pangram or not.
def is_pangram(_str):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in alphabet:
        if not i in _str.lower():
            return False
        
    return True
print("---is_panram function---:")
print(is_pangram("The quick brown fox jumps over the lazy dog."))
print(is_pangram("The quick brown fox jumps over the lazy."))
print(is_pangram("Sphinx of black quartz, judge my vow"))
print(is_pangram("The quick onyx goblin jumps over the lazy dwarf"))


# 19-"99 Bottles of Beer" is a traditional song in the United States and Canada. 
# It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, 
# and can take a long time to sing. The song's simple lyrics are as follows:
# ---99 bottles of beer on the wall, 99 bottles of beer.
# ---Take one down, pass it around, 98 bottles of beer on the wall.
# The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers 
# reach zero.
# Your task here is write a Python program capable of generating all the verses of the song.
def sing_song(num=99):

    for i in range(1,num+1)[::-1]:
        print(str(i) +' bottles of beer on the wall,'+ str(i)+' bottles of beer.Take one down, pass it around,')

print(sing_song())

# 20-Represent a small bilingual lexicon as a Python dictionary in the following fashion 
# {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} 
# and use it to translate your Christmas cards from English into Swedish. That is, write a 
# function translate() that takes a list of English words and returns a list of Swedish words.

def translate_swedish(_str):
    _dict={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"} 
    word_list=_str.split(" ")
    res=[]
    for i in word_list:
        res.append(_dict[i])
    return " ".join(res)    


print(translate_swedish("happy new year"))
print(translate_swedish("happy new year and merry christmas"))



