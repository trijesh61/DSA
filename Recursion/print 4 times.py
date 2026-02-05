#print "Trijesh" 4 times using Recursion
def printTrijesh(c):
    if c<=0:
        return 
    print("Trijesh")
    c-=1
    printTrijesh(c)
printTrijesh(4)