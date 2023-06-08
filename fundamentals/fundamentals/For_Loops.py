#print all integers from 0 to 150
for i in range(150):
    print(i)

#multiples of 5 from 5 to 1000
for i in range(5, 1000, 5):
    print(i)

#print integers from 1 to 100; if divisible by 5 print coding, if divisible by 10 print coding dojo
for i in range(1, 100):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#add odd integers from 0 to 500,000
odd_sum = 0
for i in range(500000):
    if i % 2 != 0:
        print(i)
        odd_sum = odd_sum + i
print(odd_sum)

#print positive numbers starting at 2018 counting down by fours
for i in range(2018, 0, -4):
    print(i)

#set three variables: low, high, mult
lowNum = 9
highNum = 124
mult = 8

for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)