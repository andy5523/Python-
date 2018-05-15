it = input("제품명:")

items = {"라면":650,"우유":1100,"콜라":1200,"캔커피":500,"과자":700}
s=0
while(True):
    if(it == ""):
        break
    s += items[it]
    print("[%s:%d] > %d"%(it,items[it],s))
    it = input("제품명:")

print("총금액 :",s)

    

