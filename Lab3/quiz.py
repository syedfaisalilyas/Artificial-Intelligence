counter=0
def quiz(n):
    counter=0
    if n==0 or n==1:
        return n
    else:
        counter+=1
        
        return ((quiz(n-1)-quiz(n-2))*quiz(n-1))


def dp(n):
    dyp=[0*n]
    print(len(dyp))
    if n in dyp:
        return dyp[n]
    else:
        return dp(n-1)-dp(n-2)*dp(n-1)
# print(counter)
print(dp(3))
