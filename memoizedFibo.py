import time
def fib(n, dp):
    if n == 1 or n == 2:
        return 1
    else:
        if dp[n] != 0:
            return dp[n]
        return fib(n-1, dp) + fib(n-2, dp)
    
dp = [0] * 100
#print current time with ms
print(time.strftime("%H:%M:%S%z", time.localtime()))
print(fib(10, dp))
print(time.strftime("%H:%M:%S%z", time.localtime()))