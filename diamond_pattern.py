#first half printing
N = int(input("Enter the maximum width of the pattern "))

if ((int(N)%2) != 0):
  rows = (int(N)+1)/2
else: 
  rows = int(N)

l = 0
for i in range(1, int(rows) + 1):
 for j in range (1, (int(rows) - i) + 1):
   print(end = "  ")
 while l != (2 * i - 1):
   print("*", end =" ")
   l = l + 1
 l = 0
 print("\n")
 
#printing second half
l = 2
n = 1
for i in range(1, int(rows)):
 for j in range (1, l):
   print(end = "  ")
 l = l + 1
 while n <= (2 * (int(rows) - i) - 1):
   print("*", end = " ")
   n = n + 1
 n = 1
 print("\n")


#expected pattern for N=7
#          * 
#        * * * 
#      * * * * * 
#    * * * * * * * 
#      * * * * * 
#        * * * 
#          * 

