import random

class Component:
    def __init__(this, w, v):
        this.w = w
        this.v = v

    def __repr__(this):
        return str(this.w) + " " + str(this.v)

class Knapsack:
    def __init__(this, Comps, T):
        this.Comps = Comps
        this.n = len(Comps)
        this.T = T

    def solveKnapsack(this):
        M = [[None] * (this.T + 1)] * (this.n + 1)
        for i in range(1, this.T):
            M[0][i] = 0
        for j in range(1, this.n):
            M[j][0] = 0
        
        for j in range(1, this.n):
            for S in range(1, this.T):
                if this.Comps[j].w > S:
                    M[j][S] = M[j-1][S]
                else:
                    M[j][S] = max(M[j-1][S], this.Comps[j].v + M[j-1][S - this.Comps[j].w])
        this.M = M

    def getSolution(this, n, T):
        if (n == 0 or T == 0):
            return []
        if (this.Comps[n].w > T):
            return this.getSolution(n-1, T)
        if (this.M[n-1][T] > this.Comps[n].v + this.M[n-1][T - this.Comps[n].w]):
            return this.getSolution(n-1, T)
        else:
            return this.getSolution(n-1, T - this.Comps[n].w) + [n]
                                  

def createComponents(n):
    temp = []
    for i in range(n):
        temp.append(Component(random.randint(0, 1000), random.randint(0, 1000)))
    return temp

x = createComponents(10)
y = Knapsack(x, 2600)
y.solveKnapsack()
print(y.getSolution(y.n-1, y.T-1))
