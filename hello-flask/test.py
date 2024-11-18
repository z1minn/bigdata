import nvapi

def hello(msg):
    #print(f"hello {msg}")
    #return "출력" #결과값(있어도 되고 없어도 되고)
    return f"hello {msg}"

#keyword = input("맛집 검색: ") # 입력창에 입력 받기
#nvapi.blog(keyword)
keyword = "경성대 밥장인"
data = nvapi.blog(keyword)
for b in data:
    print(b["title"])



# 입력 받은 값은 keyword에 저장
# 입력받은 값을 hello 함수에 입력값으로 넣기
#result = hello(keyword) # 위 함수에서 전달된 값을 result에 전달
#print(result) # 전달된 값을 화면에 출력

def hello2():
    menu = ["짜장면", "김밥", "라면", "돈까스"] #리스트
    dmenu = {"메뉴":"짜장면", "가격": 5000} #딕셔너리
    return menu

#menu = hello2()
#print(menu)
#for m in menu:
#    print(m)