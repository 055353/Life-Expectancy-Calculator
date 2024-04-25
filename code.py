# This code calculates the days, weeks, and months left for you to live if you are supposed to live for 90 years.

# Define the target age
target_age = 90

# Ask for the user's age
user_age = input("Please enter your age: ")

# Calculate the days, weeks, and months left
days_left = 365 * (target_age - int(user_age)) # Calculate days left by multiplying remaining years by 365
weeks_left = 52 * (target_age - int(user_age)) # Calculate weeks left by multiplying remaining years by 52
months_left = 12 * (target_age - int(user_age)) # Calculate months left by multiplying remaining years by 12

# Print the result
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left to live.")
