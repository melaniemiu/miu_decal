

#2.1 - Making a List Variable

nut_raker = list(range(21))
print(nut_raker)




#2.2 Working with List Elements

def squareList(butter):
    return[n ** 2 for n in butter] # ran into an issue here with syntax using () instead of [].

butter = list(range(21)) # forgot the syntax for range((number value)). whoops lol
jelly = squareList(butter)

print(jelly)




#2.3 Slicing

def slice(jelly):
    return jelly[0:15] # didn't know the command for this part, googled it.

print(slice(jelly))




#2.4 Striding

def every_fifth(jelly):
    sando = squareList(jelly)
    return jelly[4:21:5] # didn't know which values to use for the slicing so I plugged and chugged, ran it and redid it until I got the values.

print(every_fifth(jelly))

#2.5 Slicing and Striding

def I_am_over_this_assignment_atpLOL(jelly):
    freaking_frick = jelly
    return freaking_frick[21:0:-3] # ngl [0:21:-3] was not working for me so i was like let's inverse this shit and it worked. debugging at its finest 0_<

jelly = squareList(butter)
print(I_am_over_this_assignment_atpLOL(jelly))





#3.1 Matrices

def lol(): #everything here was either incorrect or i had to google it. forgot about empty lists until now..

    matrix = [] #used matrix() like calling a function. used matrix = [] instead
    num = 1 

    for i in range(5): #forgot about for i in range. then i remember (after googling)
        row = []
        for j in range(5): 
            row.append(num) #forgot about append command. then i remembered it.
            num += 1 #got =+ the first time instead of +=

        matrix.append(row)
    return matrix #this thing was considered outside the function for the longest time bc i didn't indent the shit above correctly.

matrix5_5 = lol()

for row in matrix5_5:
    print(row) 
#fml this took me 2 days.





#3.2 Replacing 2D lists with multiples of 3

def gmtfo():
    matrix = [] 
    num = 1 

    for i in range(5):
        row = []
        for j in range(5): 
            row.append(num) 
            num += 1 
        matrix.append(row) #forgor to add this line entirely. 
    return matrix

matrix = gmtfo()

def getmetfout(matrix):
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0: #forgor what == meant
                matrix[i][j] = "?"
    return matrix

matrix2 = getmetfout(matrix)      

for row in matrix2:
    print(row)





#3.3 Summing None "?" Elements

def i_need_sleep():
    matrix = [] #i did not initialize a new matrix whatsoever.
    num = 1 

    for i in range(5):
        row = []
        for j in range(5): 
            row.append(num) 
            num += 1
        matrix.append(row)

    return matrix

def it_is_1_am(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix

#this whole part below i had to google.

def not_question_marks(matrix):
    total = 0
    for row in matrix:
        for value in row: #forgot for i in range function. googled to fix.
            if value != "?":  #forgot what != did. googled it to fix that.
                total += value #did =+ again instead of +=
    return total

matrix = i_need_sleep() #forgot the () to state it is a function.
matrix_2 = it_is_1_am(matrix)

result = not_question_marks(matrix_2)

print(result)  