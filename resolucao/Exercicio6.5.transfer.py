def transfer(S,T):
    for i in range(len(S)):
        T.append(S.pop())
    return T

S = [1,2,3,4,5,6,7,8,9,10]
T = []

print(transfer(S,T))