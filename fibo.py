def fibonacci(n):
    fib = [0,1]
    
    for i in range(2,n+1):
        next_fib = fib[i-1] + fib[i-2]
        fib.append(next_fib)
    
    return fib

num = int(input("Digite um número: "))

fib = fibonacci(num)

if num in fib:
    print(f"O número {num} pertece a sequencia de Fibonacci. ")
    
else:
    print(f"O número {num} não pertece a sequencia de Fibonacci.")