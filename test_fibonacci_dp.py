def Fibonacci(n):
	dp = [0] * 101
	if n == 0:
		dp[n] = 0	
	elif n == 1:
		dp[n] = 1
	elif dp[0] == 0:
		dp[n] = Fibonacci(n-1) + Fibonacci(n-2) 
	return dp[n] 

def test_cases():
	assert Fibonacci(0) == 0
	assert Fibonacci(1) == 1
	assert Fibonacci(2) == 1
	assert Fibonacci(3) == 2
	assert Fibonacci(4) == 3	
	assert Fibonacci(5) == 5
	assert Fibonacci(6) == 8
	assert Fibonacci(7) == 13
	assert Fibonacci(8) == 21
	assert Fibonacci(9) == 34
	assert Fibonacci(10) == 55
	assert Fibonacci(15) == 610
	assert Fibonacci(20) == 6765
	assert Fibonacci(28) == 317811


