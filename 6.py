engkor_dict = dict()
eng = input("영어 단어:")
kor = input("한글 단어:")

while(True):
    engkor_dict[eng] = kor
    eng = input("영어 단어:")
    kor = input("한글 단어:")
    if(eng == kor == ""):
        break

print(engkor_dict)
