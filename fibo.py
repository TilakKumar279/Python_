print("We Shall print the Fibonacci Numbers in different forms");
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print (b)
        a, b = b, a+b

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
	
if __name__ == "__main__":
import sys
fib(int(argv[1]))


fib = [0, 1]
def fibo(n):
  for i in range(n):
    fib.append(fib[i] + fib[i+1])
  return fib
print(fibo(int(input("Enter:"))))