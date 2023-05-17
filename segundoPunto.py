from functools import reduce
list1 = ["aa","bb","cc"]
list2 = ["aa","bb","cc"]
list3 = ["bb","ac","bv"]
    
def isEq(lis1,lis2):
    mapp = list(map(lambda x,y:x==y,lis1,lis2))
    red = reduce(lambda x,y : x and y, mapp)
    return red
    

print(isEq(list1,list3))
print(isEq(list1,list2))