
def permutationFromCycles(n, cycles):
    mapping=[0]*n
    for i in range(n):
        mapping[i]=i
    for cycle in cycles:
        for i in range(len(cycle)):
            assert mapping[cycle[i]]==cycle[i]
            mapping[cycle[i]]=cycle[(i+1)%len(cycle)]
    return mapping

def trivialPermutation(n):
    mapping=[0]*n
    for i in range(n):
        mapping[i]=i
    return mapping

def cycles(p):
    C=[]
    n = len(p)
    incyc=[False]*n
    for i in range(n):
        if not incyc[i]:
            if p[i]!=i:
                newcycle=[i]
                C.append(newcycle)
                incyc[i]=True
                next=p[i]
                while next!=i:
                    newcycle.append(next)
                    incyc[next]=True
                    next=p[next]
    return C
        
def printPermutation(p):
    C=cycles(p)
    s=''
    for cycle in C:
        cyclestr='('
        for el in cycle:
            cyclestr+=str(el)+','
        s+=cyclestr[:len(cyclestr)-1]+')'
    if s=='':
        s='()'
    print(s)

# def __repr__(self):
#     return 'permutation('+str(self.n)+','+str(self.mapping)+')'

def isTrivial(p):
    for i in range(len(p)):
        if p[i] != i:
            return False
    return True

def testPermutation(n):
    """
    Creates a nasty permutation of length n, with a very large "period".
    """
    M=[i+1 for i in range(n)]
    clen=2
    cind=0
    while clen+cind<n:
        M[cind+clen-1]=cind
        cind+=clen
        clen+=1
    M[n-1]=cind
    return M