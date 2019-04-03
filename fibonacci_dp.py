import array

dp = [0] * 101

def Fibonacci(n):
	if n == 0:
		dp[n] = 0	
	elif n == 1:
		dp[n] = 1
	elif dp[0] == 0:
		dp[n] = Fibonacci(n-1) + Fibonacci(n-2) 
	return dp[n] 

print("The fibonacci sequence is determined by the function \"f(n) = f(n-1) + f(n-2)\", where \"f(0) = 0\" and \"f(1) = 1\"\nThis program return the value of f(n) in the function f(n) = f(n-1) + f(n-2)")


x = int(input("Tap the value of n"))

print ("The value is: ", Fibonacci(x))
