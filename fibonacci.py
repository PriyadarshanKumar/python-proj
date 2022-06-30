
# def fibo(n):
#    a = 0
#    b = 1
#    print("Fibonacci Number is: ", a)
#    print("Fibonacci Number is: ", b)
#    for i in range(0, n - 1):
#       sum = a + b
#       a = b
#       b = sum
#
#       print("Fibonacci Number is: ", sum)

def fibo(n):
   if(n<=1):
      return n
   else:
      d= fibo(n-1) + fibo(n-2)
      # print("Fibonacci Number is :",d)
      return d
n=int(input())
print("Fibonacci Number is :",0)
print("Fibonacci Number is :",1)
fibo(n)