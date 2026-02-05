#print "Trijesh" 4 times using Recursion
def printTrijesh(c):
    if c<=0:
        return 
    print("Trijesh")
    c-=1
    printTrijesh(c)
printTrijesh(4)


Count=0
def print__():
    global Count
    if Count==4:
        return
    Count+=1
    print("Trijeshhh.....")
    print__()
print__()