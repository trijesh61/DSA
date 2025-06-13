def remove_duplicates(a):
    seen = set()
    l = []
    for i in a:
        if i not in seen:
            seen.add(i)
            l.append(i)
    return l

a=list(map(int,input().split()))
print(remove_duplicates(a))