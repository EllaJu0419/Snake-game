import time
from tkinter import *
import random
from tkinter.messagebox import showinfo
import pickle

#screen resolution 1440x900
#Cheat code: control + c (c is lowercase)
#Boss key: control + z (z is lowercase)



#place the coords of obstacle
aaaa = []
#place the coords of food1
food11 = []

def clicked(event):
    pass


def growSnake():
    global score

    score += 10

    txt = "score:" + str(score)
    mainpage_canvas.itemconfigure(scoreText, text=txt)

    lastElement = len(snake) - 1
    lastElementPos = mainpage_canvas.coords(snake[lastElement])
    
    snake.append(mainpage_canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="#FDF3F3"))

    if (direction == "left"):
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0] + snakeSize, lastElementPos[1],
                               lastElementPos[2] + snakeSize, lastElementPos[3])
    elif (direction == "right"):
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0] - snakeSize, lastElementPos[1],
                               lastElementPos[2] - snakeSize, lastElementPos[3])
    elif (direction == "up"):
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] + snakeSize,
                               lastElementPos[2], lastElementPos[3] + snakeSize)
    else:
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] - snakeSize,
                               lastElementPos[2], lastElementPos[3] - snakeSize)
    if score != 0:
        if score % 30 == 0:
            placezhangai()
            aaaa.append(zuobiao)
            za.append(zhangai)

    if score == 60:
        placeFood1()
        food11.append(mainpage_canvas.coords(food1))  

def growSnake1():
    global score

    score += 20

    txt = "score:" + str(score)
    mainpage_canvas.itemconfigure(scoreText, text=txt)

    lastElement = len(snake) - 1
    lastElementPos = mainpage_canvas.coords(snake[lastElement])

    snake.append(mainpage_canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="#FDF3F3"))
    snake.append(mainpage_canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="#FDF3F3"))

    if (direction == "left"):
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0] + snakeSize, lastElementPos[1],
                               lastElementPos[2] + snakeSize, lastElementPos[3])
    elif (direction == "right"):
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0] - snakeSize, lastElementPos[1],
                               lastElementPos[2] - snakeSize, lastElementPos[3])
    elif (direction == "up"):
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] + snakeSize,
                               lastElementPos[2], lastElementPos[3] + snakeSize)
    else:
        mainpage_canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] - snakeSize,
                               lastElementPos[2], lastElementPos[3] - snakeSize)
    if score != 0:
        if score % 30 == 0:
            placezhangai()
            aaaa.append(zuobiao)
            za.append(zhangai)
            
    
    placeFood1()
    food11.append(mainpage_canvas.coords(food1))

        
#palce two different score food

def placeFood():
    global food, foodX, foodY

    food = mainpage_canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="steel blue")
    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)

    mainpage_canvas.move(food, foodX, foodY)

def placeFood1():
    global food1, foodX1, foodY1
    
    food1 = mainpage_canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="pink")
    foodX1 = random.randint(0, width - snakeSize)
    foodY1 = random.randint(0, height - snakeSize)

    mainpage_canvas.move(food1, foodX1, foodY1)


def moveFood():
    global food, foodX, foodY

    mainpage_canvas.move(food, foodX * (-1), foodY * (-1))

    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)

    mainpage_canvas.move(food, foodX, foodY)

def moveFood1():
    global  food1, foodX1, foodY1
    mainpage_canvas.move(food1, foodX1 * (-1), foodY1 * (-1))

zhangai = 0
zhangaiX = 0
zhangaiY = 0
za = []

#place obstacle 
def movezhangai():
    global zhangai, zhangaiX, zhangaiY,za

    mainpage_canvas.move(zhangai, zhangaiX * (-1), zhangaiY * (-1))

    zhangaiX = random.randint(0, width - 2 * snakeSize)
    zhangaiY = random.randint(0, height - 2 * snakeSize)

    mainpage_canvas.move(zhangai, zhangaiX, zhangaiY)


def placezhangai():
    global zhangai, zhangaiX, zhangaiY, zuobiao
    a = random.randint(1, 2)

    zhangaiX = random.randint(0, width - 2 * snakeSize)
    zhangaiY = random.randint(0, height - 2 * snakeSize)
    
    if a == 1:
        zhangai = mainpage_canvas.create_rectangle(0, 0, 10, 185, fill="white")
        zuobiao = (zhangaiX, zhangaiY, int(zhangaiX) + 10, int(zhangaiY) +185 )
    if a == 2:
        zhangai = mainpage_canvas.create_rectangle(0, 0, 185, 10, fill="white")
        zuobiao = (zhangaiX, zhangaiY, int(zhangaiX) + 185, int(zhangaiY) +10 )

    mainpage_canvas.move(zhangai, zhangaiX, zhangaiY)

def overlapping(a, b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False


def moveSnake():
    global score
    mainpage_canvas.pack()
    positions = []

    positions.append(mainpage_canvas.coords(snake[0]))

    if (positions[0][0] < 0):
        mainpage_canvas.coords(snake[0], width, positions[0][1], width - snakeSize, positions[0][3])
    elif (positions[0][2] > width):
        mainpage_canvas.coords(snake[0], 0 - snakeSize, positions[0][1], 0, positions[0][3])
    elif (positions[0][1] < 0):
        mainpage_canvas.coords(snake[0], positions[0][0], height, positions[0][2], height - snakeSize)
    elif (positions[0][3] > height):
        mainpage_canvas.coords(snake[0], positions[0][0], 0 - snakeSize, positions[0][2], 0)

    positions.clear()

    positions.append(mainpage_canvas.coords(snake[0]))

    if (direction == "left"):
        mainpage_canvas.move(snake[0], -snakeSize, 0)
    elif direction == "right":
        mainpage_canvas.move(snake[0], snakeSize, 0)
    elif direction == "up":
        mainpage_canvas.move(snake[0], 0, -snakeSize)
    elif direction == "down":
        mainpage_canvas.move(snake[0], 0, snakeSize)

    sHeadPos = mainpage_canvas.coords(snake[0])
    #food+10 score
    foodPos = mainpage_canvas.coords(food)
    
    if (overlapping(sHeadPos, foodPos)):
        moveFood()
        growSnake()

    #food1+20 score
    if score > 50:
        for j in food11:   
            if (overlapping(sHeadPos, j)):
                moveFood1()
                food11.clear()
                growSnake1()
            
    for i in range(1, len(snake)):
        positions.append(mainpage_canvas.coords(snake[i]))

    for i in range(len(snake) - 1):
        mainpage_canvas.coords(snake[i + 1], positions[i][0], positions[i][1], positions[i][2], positions[i][3])


    for i in range(1, len(snake)):
        if overlapping(sHeadPos, mainpage_canvas.coords(snake[i])):
            gameOver = True
            mainpage_canvas.create_text(width / 2, height / 2, fill="white", font="Times 20 italic bold",
                                        text="Game Over!")
            leader_board()
            
            
    for k in aaaa:
        if overlapping(sHeadPos,k):
            gameOver = True
            mainpage_canvas.create_text(width / 2, height / 2, fill="white", font="Times 20 italic bold",
                                        text="Game Over!")
            leader_board()
   
    if "gameOver" not in locals():
        mainpage.after(90, moveSnake)
    return score

    

    
def cheat_code(event):
    last_coord = []
    lastElement = len(snake) - 1
    last_coord.append(mainpage_canvas.coords(snake[lastElement]))
    last_one = snake[lastElement]
    snake.pop()
    mainpage_canvas.move(last_one, last_coord[0][0] * (-1), last_coord[0][1] * (-1))

def boss_key(event):
    tk=Toplevel()
    tk.title("Boss Key")
    tk.geometry("1150x700")
    canvas1 = Canvas(tk, height=1000, width=2000)
    background1 = PhotoImage(file="bosskey.png")  
    image1 = canvas1.create_image(0, 0, anchor="nw", image=background1)
    canvas1.pack(side="top")
    tk.mainloop()


def pushkey(event):
    
    global direction
    
    if event.keysym == leftkey:
        direction = "left"
    if event.keysym == rightkey:
        direction = "right"
    if event.keysym == upkey:
        direction = "up"
    if event.keysym == downkey:
        direction = "down"

    

def def_key():

    global UP, DOWN, LEFT, RIGHT
    define_key=Toplevel()
    define_key.title("Define the Keys")
    define_key.geometry("550x500")


    UP =Label(define_key,text='Up Key：')
    UP.grid(row=0,sticky=W)
    UP =Entry(define_key)
    UP.grid(row=0,column=1,sticky=E)
     

    DOWN =Label(define_key,text='Down Key：')
    DOWN.grid(row=1,sticky=W)
    DOWN =Entry(define_key)
    DOWN.grid(row=1,column=1,sticky=E)


    LEFT =Label(define_key,text='Left Key：')
    LEFT.grid(row=2,sticky=W)
    LEFT =Entry(define_key)
    LEFT.grid(row=2,column=1,sticky=E)


    RIGHT =Label(define_key,text='Right Key：')
    RIGHT.grid(row=3,sticky=W)
    RIGHT =Entry(define_key)
    RIGHT.grid(row=3,column=1,sticky=E)

    
    b_confirm = Button(define_key,text='Save',command=savekey)
    b_confirm.grid(row=4,column=1,sticky=E)

    
    define_key.mainloop()

def savekey():

    global upkey, downkey, leftkey, rightkey
    upkey = UP.get()
    downkey = DOWN.get()
    leftkey = LEFT.get()
    rightkey = RIGHT.get()

def rest():
    aaaa.clear()
    for wanmei in za:
        mainpage_canvas.delete(wanmei)


def pausegame():
    
    global pause
    pause=True
    showinfo('Pause','Push OK to continue')
    pause = False

def def_name():

    global NAME
    
    define_name=Toplevel()
    define_name.title("Input your name")
    define_name.geometry("550x500")


    NAME =Label(define_name,text='Your name：')
    NAME.grid(row=1,sticky=W)
    NAME =Entry(define_name)
    NAME.grid(row=1,column=1,sticky=W)

    
    a_confirm = Button(define_name,text='Save',command=savename)
    a_confirm.grid(row=2,column=1,sticky=W)

    
    define_name.mainloop()

def savename():
    
    global name
    name = NAME.get()


def leader_board():
    
    leader = Toplevel()
    leader.title("Leader Board")
    leader.geometry("450x700")
    Label(leader,text="Leader Board of history players", font=('Times 20 italic bold',18)).grid(row = 0,column=0,columnspan =3,padx=100, pady=5)
    Label(leader,text="Rank", font=('Times 20 italic bold',18)).grid(row = 1,column=0,padx=10, pady=5)
    Label(leader,text="Playername", font=('Times 20 italic bold',18)).grid(row = 1,column=1,padx=10, pady=5)
    Label(leader,text="Score", font=('Times 20 italic bold',18)).grid(row = 1,column=2,padx=10, pady=5)

    #open file and write name and score in
    filename = 'leader_board.txt'
    with open(filename,'a') as file_write:
        file_write.write(str(name)+':'+str(score)+'\n')

    #open file and read all the name and score
    with open(filename,'r') as file_read:
        dic = []
        for line in file_read.readlines():
            line = line.strip('\n')
            b = line.split(':')
            dic.append(b)
    my_dic = dict(dic)
    #compare the score in dic
    
    result = sorted(my_dic.items(),key = lambda x: int(x[1]),reverse=True)
    
    #print the result to the windows
    for i in range(len(result)):
        Label(leader,text=int(i+1), font=('Times 20 italic bold',18)).grid(row = int(i+2),column=0,padx=10, pady=5)
        Label(leader,text=result[i][1], font=('Times 20 italic bold',18)).grid(row = int(i+2),column=1,padx=10, pady=5)
        Label(leader,text=result[i][0], font=('Times 20 italic bold',18)).grid(row = int(i+2),column=2,padx=10, pady=5)
        
    Button(leader,text='Back',font=('Times 20 italic bold',18),command=leader.destroy).grid(row=int(len(result)+2),column=2,padx=10,pady=5)  
         
    leader.mainloop()

    
def savegame():
    coord_food = mainpage_canvas.coords(food)
    coord_food1 = mainpage_canvas.coords(food1)

    #coord of snake
    sn = []
    for i in range(0,len(snake)):
        sn.append(mainpage_canvas.coords(snake[i]))

    #coord of obstacle

    with open('save_game.pickle','wb') as savegame_file:
        pickle.dump([name,upkey,downkey,leftkey,rightkey,len(snake),score,direction,
                     foodX,foodY,foodX1,foodY1,sn,za,aaaa],savegame_file)
        
def loadgame():
    global width
    width = 720
    global height
    height = 720
    global mainpage
    mainpage = Toplevel()
    ws = mainpage.winfo_screenwidth()
    hs = mainpage.winfo_screenheight()
    x = (ws / 2) - (width / 2)
    y = (hs / 2) - (height / 2)
    mainpage.geometry('%dx%d+%d+%d' % (width, height, x, y))
    mainpage.title("Snake Game")
    global mainpage_canvas
    mainpage_canvas = Canvas(mainpage, bg="black", width=width, height=height)
    buttonBG = mainpage_canvas.create_rectangle(0, 0, 10, 3, fill="grey40", outline="grey60")
    buttonTXT = mainpage_canvas.create_text(50, 15, fill="white")
    rest_button = Button(mainpage, text='Rest', font=("Arial", 12),command=rest)
    rest_button.place(x=0, y=0)
    buttonBGp = mainpage_canvas.create_rectangle(10, 0, 10, 3, fill="grey40", outline="grey60")
    buttonTXTp = mainpage_canvas.create_text(50, 15, fill="white")
    pause_button = Button(mainpage, text='Pause', font=("Arial", 12),command=pausegame)
    pause_button.place(x=35, y=0)
    buttonBGpp = mainpage_canvas.create_rectangle(20, 0, 10, 3, fill="grey40", outline="grey60")
    buttonTXTpp = mainpage_canvas.create_text(50, 15, fill="white")
    save_button = Button(mainpage, text='Save', font=("Arial", 12),command=savegame)
    save_button.place(x=70, y=0)
    
    mainpage_canvas.tag_bind(buttonBG, "<Button-1>", clicked)
    mainpage_canvas.tag_bind(buttonTXT, "<Button-1>", clicked)
    mainpage_canvas.tag_bind(buttonBGp, "<Button-2>", clicked)
    mainpage_canvas.tag_bind(buttonTXTp, "<Button-2>", clicked)
    mainpage_canvas.tag_bind(buttonBGpp, "<Button-3>", clicked)
    mainpage_canvas.tag_bind(buttonTXTpp, "<Button-3>", clicked)


    global snake
    snake = []
    global snakeSize
    snakeSize = 15
    snake.append(mainpage_canvas.create_rectangle(snakeSize, snakeSize, snakeSize * 2, snakeSize * 2, fill="white"))
    global score
    score = 0
    global txt
    txt = "Score:" + str(score)
    global scoreText
    scoreText = mainpage_canvas.create_text(width / 2, 10, fill="white", font="Times 20 italic bold", text=txt)

   
    
    mainpage_canvas.bind("<Key>", pushkey)
    mainpage_canvas.focus_set()

    mainpage.bind("<Control-c>", cheat_code)
    mainpage.bind("<Control-z>", boss_key)
    
    global direction
    direction = "right"

    global name,upkey,downkey,leftkey,rightkey,length,foodX,foodY,foodX1,foodY1,sn,za,aaaa
    with open('save_game.pickle','rb') as loadgame_file:
        name,upkey,downkey,leftkey,rightkey,length,score,direction,foodX,foodY,foodX1,foodY1,sn,za,aaaa=pickle.load(loadgame_file)

    global food,food1
    food = mainpage_canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="steel blue")
    mainpage_canvas.move(food, foodX, foodY)
    food1 = mainpage_canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="pink")
    mainpage_canvas.move(food1, foodX1, foodY1)
    #put snake
    snake={}
    for i in range(0,length-1):
        snake[i]=mainpage_canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="#FDF3F3")
        sn[i]=mainpage_canvas.coords(snake[i])
        mainpage_canvas.move(snake[i], sn[i][0],sn[i][1])   
    #put obstacle
    for i in range(0,len(za)):
        mainpage_canvas.move(za[i],aaaa[i][0],aaaa[i][1])
    moveSnake()


    
       
def play():
    
    global width
    width = 720
    global height
    height = 720
    global mainpage
    mainpage = Toplevel()
    ws = mainpage.winfo_screenwidth()
    hs = mainpage.winfo_screenheight()
    x = (ws / 2) - (width / 2)
    y = (hs / 2) - (height / 2)
    mainpage.geometry('%dx%d+%d+%d' % (width, height, x, y))
    mainpage.title("Snake Game")
    global mainpage_canvas
    mainpage_canvas = Canvas(mainpage, bg="black", width=width, height=height)
    buttonBG = mainpage_canvas.create_rectangle(0, 0, 10, 3, fill="grey40", outline="grey60")
    buttonTXT = mainpage_canvas.create_text(50, 15, fill="white")
    rest_button = Button(mainpage, text='Rest', font=("Arial", 12),command=rest)
    rest_button.place(x=0, y=0)
    buttonBGp = mainpage_canvas.create_rectangle(10, 0, 10, 3, fill="grey40", outline="grey60")
    buttonTXTp = mainpage_canvas.create_text(50, 15, fill="white")
    pause_button = Button(mainpage, text='Pause', font=("Arial", 12),command=pausegame)
    pause_button.place(x=35, y=0)
    buttonBGpp = mainpage_canvas.create_rectangle(20, 0, 10, 3, fill="grey40", outline="grey60")
    buttonTXTpp = mainpage_canvas.create_text(50, 15, fill="white")
    save_button = Button(mainpage, text='Save', font=("Arial", 12),command=savegame)
    save_button.place(x=80, y=0)
    
    mainpage_canvas.tag_bind(buttonBG, "<Button-1>", clicked)
    mainpage_canvas.tag_bind(buttonTXT, "<Button-1>", clicked)
    mainpage_canvas.tag_bind(buttonBGp, "<Button-2>", clicked)
    mainpage_canvas.tag_bind(buttonTXTp, "<Button-2>", clicked)
    mainpage_canvas.tag_bind(buttonBGpp, "<Button-3>", clicked)
    mainpage_canvas.tag_bind(buttonTXTpp, "<Button-3>", clicked)


    global snake
    snake = []
    global snakeSize
    snakeSize = 15
    snake.append(mainpage_canvas.create_rectangle(snakeSize, snakeSize, snakeSize * 2, snakeSize * 2, fill="white"))
    global score
    score = 0
    global txt
    txt = "Score:" + str(score)
    global scoreText
    scoreText = mainpage_canvas.create_text(width / 2, 10, fill="white", font="Times 20 italic bold", text=txt)

   
    
    mainpage_canvas.bind("<Key>", pushkey)
    mainpage_canvas.focus_set()

    mainpage.bind("<Control-c>", cheat_code)
    mainpage.bind("<Control-z>", boss_key)
    
    global direction
    direction = "right"
    
    placeFood()
    moveSnake()

    

# config the welcome page
window = Tk()

window.title("My Game")
window.geometry("550x500")
canvas = Canvas(window, height=200, width=500)

background = PhotoImage(file="background.gif")  
image = canvas.create_image(0, 0, anchor="nw", image=background)
canvas.pack(side="top")

define_key_button = Button(window, text = "Define the keys", font=("Arial", 20), width=20, height=2, command=def_key)
name_button = Button(window, text="Input your name", font=("Arial", 20), width=20, height=2, command=def_name)
play_button = Button(window, text="Play", font=("Arial", 20), width=20, height=2, command=play)
Quit_button = Button(window, text="Quit", font=("Arial", 20), width=20, height=2, command=window.destroy)
load_button = Button(window, text="Load previous game", font=("Arial", 20), width=20, height=2, command=loadgame)
define_key_button.pack()
name_button.pack()
play_button.pack()
Quit_button.pack()
load_button.pack()




