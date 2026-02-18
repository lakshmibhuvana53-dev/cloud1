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

# Functions used in integers 

01. print(type(variable_name))
       Gives the data type of the value stored in variable
   num=14
   print(type(num))    
   class<int>

02. We can use comparision operators(relational operators) and airthemetic operators
       . Addition - + : print(3+2)
       . Subtraction - - : print(3-2)
       . Multiplication - * : print(3*2)
       . Division - /: print(3/2)
       . Modulus - % : print(3%2)
       . Float devision - // : print(3//2)
       . Exponent and power - ** : print(3**2) = o/p= 9

     Comparision Operators
       . Greater than - > : print(num1 > num2)
       . Lesser than - < : print(num1 < num2)
       . Equal to - == : print(num1==num2)
       . Greater than or equal to - >= : print(num1>=num2)
       . Lesser than or equal to - <= : print(num1<=num2)
       . Not equal to - != : print(num1!=num2)

    These operators gives boolean expressions like true or false

    Few built in functions 
       . print(abs(-3))
           gives the absolute values for above example the output is 3
       . print(round(3.75))
           gives the round figure of the digits for above example the output is 4
       . print(round(3.75,1))
           gives the round figure value and another one arguement too for the above example the output is 3.8

      To work with string values

       . num_1='200'
         num_2='300'
         num_1=int(num_1)
         num_2=int(num_2)
         print(num_1+num_2)

         The out put  of the above code is 500
         (if the datatype int (the 3rd and 4th line)is not mentioned the output will be like 200300 but not the value what is expected )         



       
