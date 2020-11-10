

spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

color = 'blue'
print(color)

pi = 3.14159
diameter = 3
radius = diameter / 2.0
print(radius)
area = pi * (radius**2)
print(area)

a = [1, 2, 3]
b = [3, 2, 1]
temp = a
a = b
b = temp
print(a)
print(b)

a = (5-3) // 2 
print(a)

a = 8 - (3 * 2) - (1 + 1)
print(a)

alice_candies = 121
bob_candies = 77
carol_candies = 109

to_smash = (alice_candies + bob_candies + carol_candies) % 3
print(to_smash)

def round_to_two_places(num):
    return round(num, 2)
    pass 

print(round_to_two_places(4.5568))

def to_smash(total_candies, n_friends=3):
    return total_candies % n_friends
print(to_smash(123, 5))

def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0
print(sign(0))  

def to_smash(total_candies, n_friends=3):
    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3
print(to_smash(5))

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = True

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

def is_negative(number):
    if number < 0:
        return True
    else:
        return False
print(is_negative(1))

def concise_is_negative(number):
    return number < 0
    pass # Your code goes here (try to keep it to one line!)
print(concise_is_negative(1))