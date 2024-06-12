#4. Fibonaci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13

n=int(input("Enter the range of Fibonaaci Series"))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c

