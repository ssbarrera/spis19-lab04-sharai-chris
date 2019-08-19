def recProduct(a,b):
    answer=0
    if b!=0:
        return a+recProduct(a,b-1)
    else:
        return 0 
print(recProduct(2,5))


