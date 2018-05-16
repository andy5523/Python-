it = input("제품명:")
items = {"라면":650,"우유":1100,"콜라":1200,"캔커피":500,"과자":700}
s = 0
while True:
    if(it == ""):
        break
    elif it in items:
        s += items[it]
        print("[",it,":",items[it],"] >",s)
        it = input("제품명:")
    elif it not in items:
        print(it,"오류")
        it = input("제품명:")
    
    

print("총 금액:",s)
