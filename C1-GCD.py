def gcd(m,n):
    f1,f2,cf = [],[],[1,]
    
    for i in range(1,m+1):
        if m % i == 0:
            f1.append(i)
    for j in range(1,n+1):
        if n % j == 0:
            f2.append(j)
    for k in f1:
        if k in f2:
            cf.append(k)
    print(f1,f2,cf)
    return cf[-1]
    
print(gcd(4,8))