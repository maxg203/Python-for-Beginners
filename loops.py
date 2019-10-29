"""
### For loop
int_list = [1, 2, 3, 4, 5, 6]
sum = 0
for iter in int_list:
    sum += iter
print("Sum =", sum)
print("Avg =", sum/len(int_list))

##Output :
#Sum = 21
#Avg = 3.5
"""

"""
### Nested For loop
for x in range(1,5): 
  for y in range(1,5): 
    print(x*y)
    
##Output :
#1
#2
#3
#4
#2
#4
#6
#8
#3
#6
#9
#12
#4
#8
#12
#16
"""

### While Loop
fruits = ["banana", "apple", "orange", "kiwi"]
position = 0
while position < len(fruits):
    print(fruits[position])
    position = position + 1
print("reached end of list")

##Output :
#banana
#apple
#orange
#kiwi
#reached end of list
