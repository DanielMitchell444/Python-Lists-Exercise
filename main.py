##Over the last few weeks, we have learned a lot. From conditional statements
##to functions, to variables. 
'''
We have learned a lot. But now, we will be learning about lists.
The defintion of list is that they are used to store multiple items
in a variable. To create a list, you can use the following syntax
'''

list = ["Python", "C++", "JavaScript"]

'''
Lists, like strings, start at 0. Meaning the first index starts at 0 and the
second index starts at 1.
The cool thing is that lists are changable, which means we can change, add, remove
items in a list after it has been created.
The other cool thing is that lists can have items with the same value
Now you will practice making a list
'''

'''
PRACTICE:
Below this comment, i want you to create a list with whatever you want
inside it. Please post the code below this comment.
'''
'''
Now that we have a definitin for lists, we can start talking about
the cool methods that are used with lists. The first method we will
be looking at is the len() method
The len() method essentially checks to see how many items are in a list
The syntax is like so
'''

print(len(list))

'''
PRACTICE:
Using the list you made above, print out the length of the list
using the len method. Please post the code below this comment
'''


'''
One important note is that lists can be any data type, they
can also hold multiple data types at once.
'''

'''
In order to access an index of a list, we can do this like so
'''

print(list[0])

##Typically when we select an index, this is the syntax we will be using


'''
In most instances, you can also change array values. This can be
done using the following syntax.
lets say we want to change the second index of our array we created
earlier, we can do this like so.
'''

list[1] = "hello"

'''
This would essentially change the list item from C++ to hello
'''

'''
Another useful tool that we can use with lists is the insert method.
The insert method essentially just inserts a new list item
into a given index without replacing the existing values
For example, we could place the list item watermelon in the 
list like so
'''

list.insert(2, "Watermelon")

'''
PRACTICE: Below this comment, i want you to use the insert method
on your newly created list that inserts a random value at the 3rd
index of the list. Please write the code below this comment
'''



'''
So, we learned about how to add items into specific elements,
but what if we want to just add a list item to the end of the list?
Well luckily, theres a solution for that, and that is the
append method
The append method essentially adds items to the end of a list
The syntax is like so
'''

list.append("Banana")

'''
And this essentially adds the list item banana to the end of the list
'''

'''
PRACTICE:
Below this comment, i want you to add a list item to your list
using the append method. Please write the code below this comment
'''

'''
There are also ways to remove items from a list. We can do this
using the remove method
the remove method essentially just removes a specified item
from the list. For example, lets say we want to remove
the list item C++. We can do this like so
'''

list.remove("C++")

'''
And this would essentially just remove C++ list item from the list
'''

'''
Another way to remove a specified index is using the pop method.
The pop method removes a specific index from a list.
The syntax is like so
'''

list.pop(0)

'''
This would essentially remove Python, the first list item
from the list
An important thing to note here is that if you don't specify 
an index, .pop() will remove the last item in the list.
'''

'''
PRACTICE:
Below this comment, i want you to use the pop method to
remove the 2nd index from the list. Please post the code
below this comment.
'''

'''
The 2nd to  last method that i want to show you is the clear() method.
The clear method essentially just clears all the items from the
list. Now, the list will still be available, but all the contents
will be cleared. We can use this method like so
'''
list.clear()


'''
The last method we will be talking about is the index method.
the index method returns the position at the first occurance
of the specified index.
For example, lets create a new list called list2 and use that
method

if we go
'''

list2 = ['apples', 'banana', 'cherry']

x = list2.index('cherry')
print(x)

'''
This would essentially print out the 2nd index, since
that is the index that cherry is at.
'''

'''
Within this section, there is another important tool that we need 
to learn that is related to arrays. And that tool is for loops.
There are 2 types of loops in Python, for loops, and while loops.
We will get to while loops later, but for now, lets focus on for
loops
A for loop is used for iterating over a sequence such as lists,
strings, tuples, dictionaries, and sets. We will get to 
tuples, dictionaries, and sets later, but for now we will
be primarily focusing on strings and lists.
for loops typically loop through once through each item
of a list.
For example, lets say we have a list of fruits like so
'''

fruits = ["Apples", "Banana", "Cherry"]

'''
We can loop through the list like so
'''

for x in fruits:
    print(x)

'''
You might be asking yourself, what is x? Well, x is essentially
just each list item without the list, while fruits would be the
individual lists printed out 3 times
for example, if you print out x, you will see
Apple
banana
cherry

but if you print out fruits, you will see the list we created printed
out 3 times
'''

'''
PRACTICE:
Below this comment, i want you to create your own list and then
loop through it using a for loop. After that, i want you to
print out the list individually. Please post the code below this
comment
'''

'''
BREAK STATEMENT:
The break statement essentially stops the loop before it has
looped through all the items. For example, if we made
something like this
'''
for x in fruits:
  print(x)
  if x == "banana":
    break
  
'''
Like we learned during the conditional lessons, we are essentially
looping through the loops array, printing each individual list
item, and then checking to see if x is equal to banana, when
x does equal banana, it would essentially stop the loop
'''

'''
PRACTICE:
Below this comment, i want you to loop through the array
you created above, below the for loop, i want you to
print out each individual index, and then check to see
if a list item is equal. Then, i want you to use the break
statement
'''


'''
CONTINUE STATEMENT:
The continue stops the current iteration of the loop and
continues with the next item.
For example, if we do something like so
'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

'''
This would essentially not print banana, since
when the individual item is equal to banana, it would
continue to the next iteration.
'''


'''
RANGE FUNCTION
We can also set a for loop to only loop for a specific number of times,
that is the range function. The range function returns a sequence
of numbers, starting at 0, and increments by 1 and ends at
a specific number
for example, lets say we want to loop through 5 numbers,
we can do this like so
'''

for x in range(5):
  print(x)

'''
This would loop through x 5 times, but it would only show numebrs
up to 4, because lists start at 0.
You can also specify a range like so
'''

for y in range(2,6):
  print(x)

'''
This would not include 6, it would only show numbers 2 through 5.


PRACTICE:
Below this comment, i want you to loop through numbers using
a for loop, loop through numbers 2 through 10 and then print
out each number. Post this below this comment
'''

'''
ELSE KEYWORD:
The else keyword specifies a block of code to be executed
when the loop has ended. We can do this like so
'''
for x in range(6):
  print(x)
else:
  print("Finally finished!")


'''
NESTED FOR LOOPS
A nested for loop is essentially a loop inside a loop.
The inner loop will be executed one time for each iteration
of the outer loop. For example, if we have something
like this.
'''

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

'''
It would essentially just print out red with every
individual list item in fruits, and go on. Its easier
to just show you the output.
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry

I will explain this better in person lol.
'''






