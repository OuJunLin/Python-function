str1 = input()

def checkStr(str_in):
    flat = "YES"
    for i in range(len(str_in)//2):
        if str_in[i] != str_in[-1-i]:
            flat = "NO"
            break
    
    return flat



print(checkStr(str1))