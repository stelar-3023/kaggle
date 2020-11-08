

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