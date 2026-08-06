def gcd(m,n):

    cf = [1,]
    for i in range(1,max(m,n)+1):
        if m % i == 0 and n % i == 0:
            cf.append(i)

    return cf[-1]
    
print(gcd(4,8))