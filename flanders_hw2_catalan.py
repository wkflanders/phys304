# William Flanders
# Homework 2

def catalan(n):
    # Base case of if n = 0, return 1
    if n == 0:
        return 0
    else:
        # Recursive case of when n > 0
        # Performing fomula and multiplying by the n-1th Catalan number is
        return (4*n-2)*catalan(n-1)/(n+1)
    
print(catalan(100))