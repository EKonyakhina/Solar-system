__author__ = 'student'
def read_graph():
    N,M = [int(j) for j in input().split()]
    A = [[] for j in range(N)]
    for i in range(M):
        x, y = [int(k) for k in input().split()]
        A[x].append(y)
    return A, N

def get_answer():
    A,N=read_graph()
    black=set()
    for x in range(N):
        if x in black:
            continue
        cycle=find_cycle(A, x, black)
        if cycle:
            return ' '.join(map(str,cycle))
    return 'YES'


def find_cycle(g,x,black):
    gray=set()
    parent=[-1]*len(g)
    hasLoop=False

    stack=[x]
    while stack:
        v=stack[-1]
        if v in black:
            stack.pop()
            continue
        if v in gray:
            gray.remove(v)
            black.add(v)
            stack.pop()
            continue

        gray.add(v)
        for neighbour in g[v]:
            if neighbour in black:
                continue
            elif neighbour in gray:
                stack=[]
                hasLoop=True
                break
            else:
                parent[neighbour] = v
                stack.append(neighbour)

    if hasLoop:
        result = [v]
        while result[-1] != neighbour:
            result.append(parent[result[-1]])
        return result[::-1]

    else:
        return[]

print(get_answer())





