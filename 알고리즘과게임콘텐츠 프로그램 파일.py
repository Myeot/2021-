#tkinter모듈 가져오기
from tkinter import *
from tkinter import messagebox

#포인트 설정
point = 0

#플레이어 설정
class Player():
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="lightpink", outline="hotpink")
        self.x, self.y = x, y
        self.nx, self.ny = x, y
    
    def move(self, direction):
        #w, a, s, d로 플레이어 조작
        if direction == 'w':
            self.nx, self.ny = self.x, self.y - 1
        elif direction == 'a':
            self.nx, self.ny = self.x - 1, self.y
        elif direction == 's':
            self.nx, self.ny = self.x, self.y + 1
        elif direction == 'd':
            self.nx, self.ny = self.x + 1, self.y

        if not self.is_collide():
            self.canvas.move(self.id, (self.nx - self.x) * 30, (self.ny - self.y) * 30)
            self.x, self.y = self.nx, self.ny

        # 첫 번째 퀴즈: 야구 게임
        if map[self.y][self.x] == 4:
            key = Tk()
            key.title("첫 번째 퀴즈")
            key.option_add("*Font", "맑은고딕 18")
            
            width, height = 500, 100
            x, y = (key.winfo_screenwidth() - width) / 2, (key.winfo_screenheight() - height) / 2
            key.geometry("%dx%d+%d+%d" % (width, height, x, y))

            lab = Label(key)
            lab.config(text = "숫자 야구 게임")
            lab.pack()

            btn = Button(key)
            btn.config(text = "도전")
            btn.config(width = 10)

            def close():
                key.destroy()

            def ball():
                import random
                secretLen = 3

                secretList = random.sample(range(10), secretLen)
                secret = ''
                for i in range(secretLen):
                    secret += str(secretList[i])


                for chance in range(10, 0, -1):
                    while True:
                        guess = input(("%d 번의 기회가 남았습니다." % chance) + "세 자리 숫자를 추측해보세요.: ")
                        if len(guess) == secretLen and guess.isdigit():
                            break
                    strike = 0
                    ball = 0
                    for i in range(secretLen):
                        if secret[i] == guess[i]:
                            strike += 1
                        elif secret[i] in guess:
                            ball += 1

                    if strike == secretLen:
                        print('성공!!')
                        global point
                        point = point + 1
                        canvas.delete("item1")
                        map[self.y][self.x] = 0
                        close()
                        break
                    if strike > 0:
                        if ball > 0:
                            print("%d strike(s) and %d ball(s)\n" % (strike, ball))
                        else:
                            print("%d strike(s)\n" % strike)
                    else:
                        if ball > 0:
                            print("%d ball(s)\n" % ball)
                        else:
                            print("Out\n")

                else:
                    print("실패했습니다. 다시 시도하세요.")
    
                    
            btn.config(command = ball)
            btn.pack()
            
            key.mainloop()

        #두 번째 퀴즈: 사칙연산
        elif map[self.y][self.x] == 5:
            
            key = Tk()
            key.title("두 번째 퀴즈")
            key.option_add("*Font", "맑은고딕 18")
            
            width, height = 500, 150
            x, y = (key.winfo_screenwidth() - width) / 2, (key.winfo_screenheight() - height) / 2
            key.geometry("%dx%d+%d+%d" % (width, height, x, y))

            lab = Label(key)
            lab.config(text = "사칙연산")
            lab.pack()
            
            btn = Button(key)
            btn.config(text = "보기")
            btn.config(width = 10)

            def num():
                cal = Tk()
                cal.title("사칙연산")
                cal.option_add("*Font", "맑은고딕 18")
                cal.resizable(False, False)

                width, height = 200, 40
                x, y = (cal.winfo_screenwidth() - width) / 2, (cal.winfo_screenheight() - height) / 2
                cal.geometry("%dx%d+%d+%d" % (width, height, x, y))

                text = Text(cal)
                text.insert(CURRENT, "3 + 8 x 9 / 2 = ?")
                text.pack()
                
            ent = Entry(key)
            ent.pack()

            def close():
                key.destroy()

            def answer():
                if ent.get() == '39':
                    global point
                    point = point + 1
                    canvas.delete("item2")
                    map[self.y][self.x] = 0
                    close()

            btn2 = Button(key)
            btn2.config(text = "입력")
            btn2.config(width = 10)

            btn.config(command = num)
            btn.pack()

            btn2.config(command = answer)
            btn2.pack()

            key.mainloop()


        #세 번째 퀴즈: 파이썬 퀴즈
        elif map[self.y][self.x] == 6:
            
            key = Tk()
            key.title("세 번째 퀴즈")
            key.option_add("*Font", "맑은고딕 18")
            
            width, height = 550, 200
            x, y = (key.winfo_screenwidth() - width) / 2, (key.winfo_screenheight() - height) / 2
            key.geometry("%dx%d+%d+%d" % (width, height, x, y))

            lab = Label(key)
            lab.config(text = "파이썬 퀴즈")
            lab.pack()

            lab = Label(key)
            lab.config(text = "함수 안에서 선언된 변수는 전역 변수이다.")
            lab.option_add("*Font", "맑은고딕 15")
            lab.pack()
            
            def close():
                key.destroy()

            def click():
                    global point
                    point = point + 1
                    btn2 = Button(key)
                    btn2.config(text = "거짓")
                    btn2.config(width = 10)
                    canvas.delete("item3")
                    map[self.y][self.x] = 0
                    close()

            def click2():
                btn = Button(key)
                btn.config(text = "참")
                btn.config(width = 10)
                
            btn = Button(key)
            btn.config(text = "참")
            btn.config(width = 10)

            btn2 = Button(key)
            btn2.config(text = "거짓")
            btn2.config(width = 10)

            btn.config(command = click2)
            btn.pack(side = LEFT, padx = 70)

            btn2.config(command = click)
            btn2.pack(side = RIGHT,  padx = 70)

            key.mainloop()

            #str = StringVar()

            rv = IntVar()

            rb1 = Radiobutton(key, text = "참", value = 1, variable = rv)
            rb1.select()
            rb2 = Radiobutton(key, text = "거짓", value = 2, variable = rv)

            btn = Button(key)
            btn.config(text = "선택")
            btn.config(width = 10)
            btn.config(command = click)

            rb1.pack()
            rb2.pack()
            btn.pack()

            key.mainloop()


        #포인트가 3이 되면 도착지점 도달
        elif point == 3:
            if map[self.y][self.x] == 3:
                messagebox.showinfo(title="성공", message="•*.°미로 탈출 성공 °.*•")
        
    #이동한 곳이 벽인지 아닌지 판별
    def is_collide(self):
        if map[self.ny][self.nx] == 1:
            return True
        else:
            return False

#키리스너 이벤트
def keyEvent(event):
    player.move(repr(event.char).strip("'"))

#tk선언
root = Tk()
root.title("미로 찾기")
root.resizable(False, False)

#창 너비, 높이, 위치 설정
width, height = 690, 690
x, y = (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

#canvas추가, 키이벤트 부착, 창 모양 및 색깔, 마우스 포인터 모양 등 설정
canvas = Canvas(root, width=width, height=height, bg="white", bd=10, relief="ridge", highlightthickness=5, highlightcolor="thistle", cursor="heart")
canvas.bind("<Key>", keyEvent)
canvas.focus_set()
canvas.pack()

#미로 맵 제작(1: 벽, 2:플레이어, 3:도착지점, 4,5,6: 퀴즈)
map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 4, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 5, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 6, 1, 0, 1, 1,1, 0, 1, 0, 1, 0, 1, 0,  1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#canvas에 맵 그리기
for y in range(len(map[0])):
    for x in range(len(map[y])):
        if map[y][x] == 1:
            canvas.create_rectangle(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="thistle", outline = "darkmagenta")
        elif map[y][x] == 2:
            player = Player(canvas, x, y)
        elif map[y][x] == 3:
            canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="lightblue", outline = "steelblue")
        elif map[y][x] == 4:
            canvas.create_arc(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="moccasin", outline = "gold", tag = "item1")
        elif map[y][x] == 5:
            canvas.create_arc(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="moccasin", outline = "gold", tag = "item2")
        elif map[y][x] == 6:
            canvas.create_arc(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="moccasin", outline = "gold", tag = "item3")

root.mainloop()
