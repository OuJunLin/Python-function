isbn = input().split()
for i in range(len(isbn)):
    if isbn[i] == "X":
        isbn[i] = 10
    else:
        isbn[i] = int(isbn[i])



def listToSum(list_in):
    sum1 = 0 
    
    list_out = []
    for i in range(len(list_in)):
        for j in range(i+1):
            sum1 += list_in[j]
        list_out.append(sum1)
        sum1 = 0
    
    return list_out



def checkISBN(list_in):
    flat = "NO"
    if len(list_in) == 10:
        list_in = listToSum(list_in)
        list_in = listToSum(list_in)
        if list_in[9]%11 == 0:
            flat = "YES"
    
    return flat



print(checkISBN(isbn))