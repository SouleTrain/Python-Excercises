def mysplit(x):
    if x.isspace() or x == '':
        return []
    lst = []
    wrd = ""
    inwrd = x[0].isspace() == False
    for i in x:
        if inwrd:
            if i.isspace() == False:
                wrd += i
            else:
                lst.append(wrd)
                inwrd = False
        else:
            if i.isspace() == False:
                inwrd = True
                wrd = i
            else:
                continue
    if inwrd:
        lst.append(wrd)
    return lst
    
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
#this took me forever to figure out because I was using x instead of i for like everything under the function
