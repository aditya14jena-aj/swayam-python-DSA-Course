"""
so this code is just an walkthrough by AJ for the NPTEL Weekly assignment
"""
#FUNCTION 1
def contracting(l):
    
    if len(l) < 3:
        return True
    
    for i in range(len(l)-2):
        diff1 = abs(l[i] - l[i+1])
        diff2 = abs(l[i+1] - l[i+2])
        
        if diff1 <= diff2:
            return False
    return True
    
#Function 2
def counthv(l):
    hc = 0
    vc = 0
    
    for i in range(1,len(l)-1):
        
        if l[i]>l[i-1] and l[i] > l[i+1]:
            #HILL condition
            hc += 1
            
        elif l[i] < l[i-1] and l[i] < l[i+1]:
            #VALLEY CONDITION
            vc += 1
    
    return[hc,vc]
    
#Function 3
def leftrotate(m):
    
    n = len(m)
    
    f = []
    
    for col in range(n-1 , -1 , -1):
        n_r = [m[row][col] for row in range(n)]
        
        f.append(n_r)
        
    return f