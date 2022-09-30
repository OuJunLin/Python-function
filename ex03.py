n = input()

def letterToNumber(c_in):
    num = 0
    if ord(c_in) < 73:
        num = ord(c_in)-55
    elif ord(c_in) == 73:
        num = 34
    elif ord(c_in) < 79:
        num = ord(c_in)-56
    elif ord(c_in) == 79:
        num = 35
    elif ord(c_in) < 87:
        num = ord(c_in)-57
    elif ord(c_in) == 87:
        num = 32 
    elif ord(c_in) < 90:
        num = ord(c_in)-58
    elif ord(c_in) == 90:
        num = 33
    return int(str(num)[0]), int(str(num)[1])
 
 
 
def checkStr(str_in):
    flat = "WRONG!!!"
    p = 0
    if len(str_in) == 10:
        x1, x2 = letterToNumber(str_in[0])
        p = x1 + (x2*9)
        
        for i in range(1, 8):
            p += (int(str_in[i])*(9-i))
        
        p = p + int(str_in[8]) + int(str_in[9])
        if p%10 == 0:
            flat = "CORRECT!!!"
    else:
        flat = "WRONG!!!"
    
    return flat



print(checkStr(n))