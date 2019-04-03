def Fibonacci(n):		
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

print("The fibonacci sequence is determined by the function \"f(n) = f(n-1) + f(n-2)\", where \"f(0) = 0\" and \"f(1) = 1\"\nThis program return the value of f(n) in the function f(n) = f(n-1) + f(n-2)")

x = int(input("Tap the value of n"))

print("The value is: ", Fibonacci(x))
