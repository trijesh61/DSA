#tail recursion
c=0
def func():
    global c
    if c==4:
        return
    c+=1
    print("count",c)
    #func()
func()