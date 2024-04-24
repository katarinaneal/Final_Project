def fibonacci(n):
    n1 = 0
    n2 = 1
    n3 = 1
    if n == 1:
        return 0
    for i in range(2,n):
        n3 = n2 + n1
        n1 =n2
        n2 =n3

    return n3

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        return True

def print_prime_factors(n):
   if is_prime(n) == True:
       print(f" {n} = {n}")
   i = 2
   num = n
   output = ""
   while i <= n // 2:
       if is_prime(i) == True and num % i == 0:
           if num / i == 1:
               output += str(i)
           else:
               output += str(i) + " * "
           num //= i

       else:
           i += 1
   print(output)