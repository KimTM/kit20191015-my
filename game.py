import random

d = True
def Start():
    sss=input("게임을 시작하겠습니까?(1번 o 나머지x):")
    if sss=="1":
        print("게임시작.")
    else:
         print("게임종료.")
         exit(0)

print("가위바위보 게임입니다.")
try:
    Start()
except:
    print("숫자를 제대로 입력하세요^^")
    Start()

set_charact=input("이름을 입력하시오 : ")
charact={
    "name":name }
print("{0}님 반갑습니다".format(charact["name"]))

dic = {"이긴횟수" : 0 } 

print("1번 가위 2번 바위 3번 보 중 선택하여 숫자를 입력하시오")


while dic["이긴횟수"] != 5 :

        user=input("숫자입력(1~3) : ")
  
        if user=="1":
                if random.choice(["가위","바위","보"])=="가위":
                    print("무승부")
                elif random.choice(["가위","바위","보"])=="바위":
                    print("패")
                else: 
                    print("승")
                    dic["이긴횟수"] +=1
                    print("득점:",dic["이긴횟수"])
                
        if user=="2":
                if random.choice(["가위","바위","보"])=="가위":
                    print("승")
                    dic["이긴횟수"] +=1
                    print("득점:",dic["이긴횟수"])
                elif random.choice(["가위","바위","보"])=="바위":
                    print("무승부")
                else:
                    print("패")
 

        if user=="3":
                if random.choice(["가위","바위","보"])=="가위":
                    print("패")
                elif random.choice(["가위","바위","보"])=="바위":
                    print("승")
                    dic["이긴횟수"] +=1
                    print("득점:",dic["이긴횟수"])
                else:
                    print("무승부")
    

f=open("game.txt", "r", encoding="UTF-8")         
r=f.read()
print(r)
f.close()