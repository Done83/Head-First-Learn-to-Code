# Get dog's and and age from the user
dog_name = input("What is your dog's name? ")
dog_age = int(input("What is your dog's age? "))
# Multiply dog's age from input with 7 to get humans age
human_age = dog_age * 7
# Display a message to end user with their dog age calculated to human age
print(f"Your dog {dog_name} is {human_age} years old in human years")