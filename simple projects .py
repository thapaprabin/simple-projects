'''print("STORY GENERATOR  ")

name = input("Enter your name :")
fav_pet = input("What is your favorite pet : ")

mother = input("Enter the name of your mother: ")
age = int(input("Whats your mother age : "))


print(f"Mr. {name} is the most hardworking person.He is an entrepreneur of nepal.  \n His mother name is {mother}.She is {age} years old now." )
print(f"He has a pet({fav_pet}) in his home.It's name is Wolf")'''

"""# Print title of the game
print("Mad Libs Generator!")
# Instructions for the user
print("Please provide the following words:")

# Prompt user for different types of words and store their responses
adjective1 = input("Adjective: ")  # Get an adjective from user
noun1 = input("Noun: ")  # Get a noun from user
verb1 = input("Verb: ")  # Get a verb from user
adjective2 = input("Adjective: ")  # Get another adjective
noun2 = input("Noun: ")  # Get another noun

# Create the story using an f-string to insert the user's words
story = f"""
Once upon a time, there was a {adjective1} {noun1} who loved to {verb1}.
One day, the {noun1} found a {adjective2} {noun2} and their life changed forever!
"""

# Display the completed story to the user
print("\nYour Mad Libs Story:")
print(story)  # Print the generated story """


import random

print("D I C E   R O L L E R  GAME ")

def roll_dice()
    return random.randint(1,6)

while True:

    user = input(" Press enter to roll the dice ")
    roll=roll_dice()

    print(f"congratulations !You rolled number { roll }")

