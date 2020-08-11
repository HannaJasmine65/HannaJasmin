N = int(input("Enter the number of rows "))
num1 = 1
num2 = 1
sum = 1
for i in range (1, int(N)+1): 
 for count in range(1,i+1):
       print(sum, end = " ")
       sum = num1 + num2
       #updating values
       num1 = num2
       num2 = sum
       count += 1
 print("\n")
 num1 = 1
 num2 = 1
 sum = 1


#espected output for N=7
#1 
#1 2 
#1 2 3 
#1 2 3 5 
#1 2 3 5 8 
#1 2 3 5 8 13 
#1 2 3 5 8 13 21 

