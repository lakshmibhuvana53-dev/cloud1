# Basics of Python Programming Language
# Author: Bhuvana 

# functions and methods used in strings 

1. len() - returns the length of a program

message='hello,world'
print(len(message))
returns - 7


2. lower() - converts all characters in a string to lowercase

print('Hello,World'.lower())
returns - hello,world


3. upper() - converts all characters in a string to upper case

print('hello,world'.upper())
returns - HELLO,WORLD

4. count() - counts the number of occurences of a substring in a string

print('hello,world')
print(message.count('l'))
returns - 3

5. find() - returns the index of the first occurence of a substring in a string

print('hello,world'.find('w'))
returns - 6

6.replace() - replaces a substring with another substring in a string

print('hello,world'.replace('world','universe'))
returns - hello,universe


7. format() - formats a string by replacing placeholders with values

greeting='Hello' 
name='Sweety'
print('{},{}'.format(greeting,name))
returns - Hello,Sweety
       or
print(f'{greeting},{name} . Welcome !') 
returns - Hello,Sweety . Welcome !
       or
message=greeting +', '+name +'. Welcome !'
print(message)
returns - Hello,sweety . Welcome !

8. split() - splits a string into a list of substrings based on a delimmiter

sentence='Hello,world,how,are,you'
print(sentence.split(','))
returns - ['Hello', 'world', 'how', 'are', 'you']

