#1. Task: print "Hello World"
print("Hello World")

#2. Print "Hello Noelle!" with the name in a variable
name = "Adrian"
print("Hello", name, "!") # with a comma
print("Hello " + name + "!") # with a +

#3. Print "Hello 42!" with the number in a variable
num = 25
print("Hello", num) # with a comma
#print("Hello" + num) # with a +   -- this one should give us an error!

#4. Print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

# NINJA BONUS: figure out how to resolve the error from #3 without changing the + sign to a comma
print("Hello", str(num))

# Store 2 foods in variables and print the string "I love to eat {{food_one}} and {{food_two}}" with format method
food_one = "lasagna"
food_two = "sweet potato"
print("I love to eat {} and {}.".format(food_one, food_two))

# Store 2 foods in variables and print the string "I love to eat {{food_one}} and {{food_two}}" with f strings
print(f"I love to eat {food_one} and {food_two}")

