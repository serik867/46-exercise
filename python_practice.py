#1-- Define a function max() that takes two numbers as arguments and returns the largest of them. 
# Use the if-then-else construct available in Python. (It is true that Python has the max() function built in,
#  but writing it yourself is nevertheless a good exercise.)

def max_num(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

print("max_num function 1-(45,56),2-(67,56)=",max_num(45,56), max_num(67,56))

#2-- Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def max_of_three(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3

print("max_of_three function 1-(45,56,65), 2-(47,56,48),3-(67,56,65) =",max_of_three(45,56,65),max_of_three(47,56,48),max_of_three(67,56,65))

#3-- Define a function that computes the length of a given list or string. 
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless 
# a good exercise.)
def leng(_list):
    count=0
    if type(_list)== str:
        _list=list(_list)

    for i in _list:
        if i != " ":
            count+=1
    return count

print("Length of list or string",leng([1,2,3,4,5,6,7,8,9,10]), leng("python is great") )

# 4--Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, 
# False otherwise.
def isVowel(_char):
    vowel=['a','e','i','o','u']
    if _char.lower() in vowel:
        return True
    else:
        return False

print("isVowel function 1-A, 2-L, 3-a -- ", isVowel('A'), isVowel('L'), isVowel('a'))

# 5--Write a function translate() that will translate a text into "rövarspråket" 
# (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. 
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".

def translate(_str):
    result=[]
    _list = _str.split()
    for word in _list:
        _list1=[]
        for i in word:
            if not isVowel(i):
                _list1.extend([i,'o',i])
            elif isVowel(i):
                _list1.extend([i])
        result.append("".join(_list1))
        _list1=[]
        
    
    return " ".join(result)


print("tranlate(this is fun) - "+ translate("this is fun"))



# 6--Define a function sum() and a function multiply() that sums and multiplies (respectively) 
# all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, 
# and multiply([1, 2, 3, 4]) should return 24.
from functools import reduce
def sum(_list):
    return reduce(lambda a,b: a+b,_list)

def multiply(_list):
    return reduce(lambda a,b:a*b,_list)


print("sum() the list--", sum([1,2,3,4]))
print("multiple() the list --",multiply([1,2,3,4]))

# 7--Define a function reverse() that computes the reversal of a string. 
# For example, reverse("I am testing") should return the string "gnitset ma I".
def reverse(_str):
    result=''
    for i in _str:
        result=i+result
    return result 

print("reverse() the string -I am testing -- ",reverse("I am testing"))

# 8--Define a function is_palindrome() that recognizes palindromes 
# (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.
def is_palindrome(_str):
    if _str == reverse(_str):
        return True
    else:
        return False
    
print("is_palindrome function -radar,serdar,geeg-- ",is_palindrome('radar'),is_palindrome('serdar'), is_palindrome('geeg'))

# 9--Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, 
# and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does,
# but for the sake of the exercise you should pretend Python did not have this operator.)
def is_member(x,y):
    for i in y:
        if i==x:
            return True
        
    return False

print("is_member -(2,[1,2,3,45]),('a','start'),(2,[1,3,4,6,76]) --", is_member(2,[1,2,3,45]), is_member('a','start'), is_member(2,[1,3,4,6,76]))

# 10--Define a function overlapping() that takes two lists and returns True if they have at least one 
# member in common, False otherwise. You may use your is_member() function, or the in operator, 
# but for the sake of the exercise, you should (also) write it using two nested for-loops.

def overlapping(_list1,_list2):
    for x in _list1:
        for y in _list2:
            if x==y:
                return True
    return False

print("overlapping function -([1,2,3,4,5],[6,7,8,9,10]),([1,2,3,4,5,6,7],[10,11,12,13,14,15,7])-- ",overlapping([1,2,3,4,5],[6,7,8,9,10]), overlapping([1,2,3,4,5,6,7],[10,11,12,13,14,15,7]))