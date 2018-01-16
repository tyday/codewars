digdic = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I", 0:""}
divids = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1, 0]

def solutionrec(n, nlist):
    if n in nlist:
        return digdic[n]
    else:
        if n // nlist[0] > 0:
            return digdic[nlist[0]]*(n//nlist[0])+ solutionrec(n%nlist[0],nlist)
        else:
            return solutionrec(n,nlist[1:])

def solution(n):
    divids = sorted(digdic.keys(),reverse=True)
    a = solutionrec(n,divids)
    #digdic[n] = a
    # print(digdic)
    return a

print(solution(1))
print(solution(2))
print(solution(11))
print(solution(20))
print(solution(30))
print(solution(33))
print(solution(1966))