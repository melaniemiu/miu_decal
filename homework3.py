

#1 Oski Problem

def computepower(x,y):
     if y == 0:
        return 1
     else:
        return x * computepower(x, y - 1)     
     
x = 2
y = 3
print(computepower(x,y))



#2 Wardrobe

def temperatures(a,b,c,d,e,f,g):

    min_temp = min(a,b,c,d,e,f,g)
    max_temp = max(a,b,c,d,e,f,g)

    return(min_temp, max_temp)

a = 15
b = 14
c = 17
d = 20
e = 23 
f = 28
g = 20

print(temperatures(a,b,c,d,e,f,g))



#3 Weekend

def isweekend(day):
    if day == 6:         # == checks if the variable (day) is equal to the integer (6), different from day = 6 (defining the day is 6)
       return "true"
    if day == 7:
        return "true"
    else: 
        return "false"
 
day = 6
print(isweekend(day))



#4 Fuel Calculator 

def fuel_efficiency(distance, fuel): 

    (fuel_efficiency) = distance / fuel
    return(fuel_efficiency)

distance = 70
fuel = 21.5

print(fuel_efficiency(distance, fuel))



#5 Secret Code

def reverse_number(n, reversed_num = 0):
    if n == 0:
        return reversed_num
    else:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        return reverse_number(n // 10, reversed_num)

print(reverse_number(12345))



#6.1 For Loops

def find_min_with_for_loop(nums): 
    # A "for loop" is a way to repeat something (like checking each number in a list) until you've done it for every item. 
    # It's like saying, "For each item in this list, do something."

    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
        return min_value
    
def find_max_with_for_loop(nums):

    max_value = nums[0]
    for num in nums:
        if num < max_value:
            max_value = num
    return max_value

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))
print(find_max_with_for_loop(nums))



#7 Vowels

def vowel_and_consonant_count(text):
    vowel = "AEIOUaeiou"

    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowel:
                vowel_count += 1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))



#8 Calculate Digital Root

def digital_root(num):
    num = sum(int(digit) for digit in str(num))

    return num

num = 2468
print(digital_root(num))