# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
ex1string = 'this is an string'
ex1number = 5
ex1list = ['esto',1,True,"cajón"]
ex1boolean = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
ex2string = ex1string[:3] 

# Exercise 3: Use an index to grab the first element from your list.
ex3 = ex1list[0]

# Exercise 4: Create a new number variable that adds 10 to your original number.
ex4 = ex1number + 10

# Exercise 5: Use an index to get the last element in your list.
ex5 = ex1list[-1]

# Exercise 6: Use split to transform the following string into a list. 
names = 'harry,alex,susie,jared,gail,conner'
ex6 = names.split(',')

# Exercise 7: Get the first word from your string using indexes. Use the upper function to
# transform the letters into uppercase. Create a new string that takes the uppercase word and the
# rest of the original string.
ex7word = ex1string.split(' ')[0].upper()
_, __, ex7string = ex1string.partition(' ')
ex7sentence = ex7word + (' ') + ex7string

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
ex8 = f'This is a sentence with my number {ex1number} inside'
print(ex8)

# Exercise 9: Print “hello world”. 
print ("hello world")