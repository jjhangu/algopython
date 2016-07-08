def helptoclone(A):
    c=0
    t=0

    for i in A:
        if i %2==0:
            c += 1
            t += c

    return len(A)*c-t