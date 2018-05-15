str = input("문자열:")

def ic(str):
    for i in range(len(str)):
        a= ""
        a= a + str[i]
    return str

def icro(str):
    for j in range(len(str)-1,-1,-1):
        b= ""
        b= b + str[j]
    b= "".join(reversed(str))
    return b

print("개별 문자 출력:",ic(str))
print("역순 개별 문자 출력:",icro(str))
