import numpy as np
import random
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox  
from tkinter import ttk 

win = Tk()
win.geometry('430x450')

title = random.randint(1,5)
if title == 1:
    win.title("Синдикат бест ивент эвер!")
elif title == 2:
    win.title("Не поставиш воричи в исследование, я твою мать закорапчу.")
elif title == 3:
    win.title("А че запомнить все 68 позиций слабо?")
elif title == 4:
    win.title("Смотри чтобы тебя не убили, пока ты альтабаешся.")
elif title == 5:
    win.title("Олды все равно не оценят -_-")
            
flagred = 0
ChoChar = 0
ChoChar2 = 0
ChoPage = 1

tabs = ttk.Notebook(win)  
tab1 = ttk.Frame(tabs)  
tab2 = ttk.Frame(tabs)  
tabs.add(tab1, text='Калькулятор')
tabs.add(tab2, text='Приоритет')
tabs.pack(expand=1, fill='both')  

def load():
    global BD,Table
    try:
        print('Поиск файла...')
        if BDLoad1Ent.get() == '':
            BD = open('BDMainTable.gol','r')
        else:
            BD = open(BDLoad1Ent.get()+'.gol','r')
        print('Фаил найден. Генерация пустой таблицы...')
        MainText.delete(1.0, END)  
    except Exception as e:
        print('Фаил не найден')
        MainText.delete(1.0, END)  
        MainText.insert(INSERT,'Фаил не найден')
    linenum = 0
    objnum = 0
    try:
        Table = np.array([['                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','',''],
            ['','','','']])
        print('Таблица создана. Начинаю заполнение...')
    except Exception as e:
        print(e)

    for line in BD:
        try:
            Table[linenum,objnum] = line
            print(str(linenum)+' '+str(objnum)+' '+str(line))
        except Exception as e:
            print(e)
        objnum = objnum + 1
        if objnum == 4:
            linenum = linenum + 1
            objnum = 0
    print('Заполнение окончено. Результат ниже.')
    print(Table)
    BDLoad1Ent.configure(state='disabled')
    BDLoadButton.configure(state='disabled')
    ListName1.configure(state='active')
    ListName2.configure(state='active')
    SearchEnt.configure(state='normal')
    SearchBut.configure(state='active')  
    
    MainText.insert(INSERT,'*Готов к работе*')
    SearchText.insert(INSERT,'*Готов к работе*')
    
def detect(event):
    global Table
    a = b = 0
    if ListName1.get() == 'Перевозка':
        a = 0
    elif ListName1.get() == 'Укрепление':
        a = 1
    elif ListName1.get() == 'Исследование':
        a = 2
    elif ListName1.get() == 'Нападение':
        a = 3
        
    if ListName2.get() == 'Ашлинг':
        b = 0
    elif ListName2.get() == 'Камериа':
        b = 1
    elif ListName2.get() == 'Элрон':
        b = 2
    elif ListName2.get() == 'Гравиций':
        b = 3
    elif ListName2.get() == 'Гафф':
        b = 4
    elif ListName2.get() == 'Хиллок':
        b = 5
    elif ListName2.get() == 'Хаку':
        b = 6
    elif ListName2.get() == 'То-Что-Сбежало':
        b = 7
    elif ListName2.get() == 'Янус':
        b = 8
    elif ListName2.get() == 'Йоргин':
        b = 9
    elif ListName2.get() == 'Корелл':
        b = 10
    elif ListName2.get() == 'Лео':
        b = 11
    elif ListName2.get() == 'Райкер':
        b = 12
    elif ListName2.get() == 'Рин':
        b = 13
    elif ListName2.get() == 'Тора':
        b = 14
    elif ListName2.get() == 'Ваган':
        b = 15
    elif ListName2.get() == 'Воричи':
        b = 16
    try:
        MainText.delete(1.0, END)   
        MainText.insert(INSERT,Table[b,a])
        print(Table[b,a])
    except Exception as e:
        print(e)
    
def search():
    global Table,textb,nameb,numpage,allnumpage
    SearchText.delete(1.0, END) 
    a = b = c = 0
    textb = []
    nameb = []
    name = ''
    for line in range(4):
        for elem in range(17):
            if SearchEnt.get() in Table[elem,line]:
                c += 1 
                if elem == 0:
                    name = 'Ашлинг >>> '
                elif elem == 1:
                    name = 'Камериа >>> '
                elif elem == 2:
                    name = 'Элрон >>> '
                elif elem == 3:
                    name = 'Гравиций >>> '
                elif elem == 4:
                    name = 'Гафф >>> '
                elif elem == 5:
                    name = 'Хаку >>> '
                elif elem == 6:
                    name = 'Хиллок >>> '
                elif elem == 7:
                    name = 'То-Что-Сбежало >>> '
                elif elem == 8:
                    name = 'Янус >>> '
                elif elem == 9:
                    name = 'Йоргин >>> '
                elif elem == 10:
                    name = 'Корелл >>> '
                elif elem == 11:
                    name = 'Лео >>> '
                elif elem == 12:
                    name = 'Райкер >>> '
                elif elem == 13:
                    name = 'Рин >>> '
                elif elem == 14:
                    name = 'Тора >>> '
                elif elem == 15:
                    name = 'Ваган >>> '
                elif elem == 16:
                    name = 'Воричи >>> ' 
                    
                if line == 0:
                    name = name + 'Перевозка'
                elif line == 1:
                    name = name + 'Укрепление'
                elif line == 2:
                    name = name + 'Исследование'
                elif line == 3:
                    name = name + 'Нападение'
                textb.append(Table[elem,line])
                nameb.append(str(name))
    
    print('Найдено '+str(c))
    print('------------------------------')
    if textb == []:
        print('Не найдено')
        FindedLable.configure(text='0/0')
        NameLabel.configure(text='>>>')
        UpBut.configure(state='disabled')
        DownBut.configure(state='disabled')
        SearchText.delete(1.0, END)   
        SearchText.insert(INSERT,'Не найдено')
    else:
        numpage = 1
        allnumpage = c
        SearchText.delete(1.0, END)   
        SearchText.insert(INSERT,textb[0])
        FindedLable.configure(text='1/'+str(c))
        NameLabel.configure(text=nameb[numpage-1])
        UpBut.configure(state='active')
        DownBut.configure(state='active')
    
def up():
    global numpage,allnumpage
    if numpage >= allnumpage:
        numpage = 1
        SearchText.delete(1.0, END)   
        SearchText.insert(INSERT,textb[numpage-1])
        FindedLable.configure(text=str(numpage)+'/'+str(allnumpage))
        NameLabel.configure(text=nameb[numpage-1])
    else:
        numpage += 1
        SearchText.delete(1.0, END)   
        SearchText.insert(INSERT,textb[numpage-1])
        FindedLable.configure(text=str(numpage)+'/'+str(allnumpage))
        NameLabel.configure(text=nameb[numpage-1])
    
def down():
    global numpage,allnumpage
    if numpage <= 1:
        numpage = allnumpage
        SearchText.delete(1.0, END)   
        SearchText.insert(INSERT,textb[numpage-1])
        FindedLable.configure(text=str(numpage)+'/'+str(allnumpage))
        NameLabel.configure(text=nameb[numpage-1])
    else:
        numpage -= 1
        SearchText.delete(1.0, END)   
        SearchText.insert(INSERT,textb[numpage-1])
        FindedLable.configure(text=str(numpage)+'/'+str(allnumpage))
        NameLabel.configure(text=nameb[numpage-1])

def update(): #Обновление кнопок во второй вкладке
    Char1But.configure(text=TableLike[ChoPage-1,1-1][0:len(TableLike[ChoPage-1,1-1])-1]+' :1')
    Char2But.configure(text=TableLike[ChoPage-1,2-1][0:len(TableLike[ChoPage-1,2-1])-1]+' :2')
    Char3But.configure(text=TableLike[ChoPage-1,3-1][0:len(TableLike[ChoPage-1,3-1])-1]+' :3')
    Char4But.configure(text=TableLike[ChoPage-1,4-1][0:len(TableLike[ChoPage-1,4-1])-1]+' :4')
    Char5But.configure(text=TableLike[ChoPage-1,5-1][0:len(TableLike[ChoPage-1,5-1])-1]+' :5')
    Char6But.configure(text=TableLike[ChoPage-1,6-1][0:len(TableLike[ChoPage-1,6-1])-1]+' :6')
    Char7But.configure(text=TableLike[ChoPage-1,7-1][0:len(TableLike[ChoPage-1,7-1])-1]+' :7')
    Char8But.configure(text=TableLike[ChoPage-1,8-1][0:len(TableLike[ChoPage-1,8-1])-1]+' :8')
    Char9But.configure(text=TableLike[ChoPage-1,9-1][0:len(TableLike[ChoPage-1,9-1])-1]+' :9')
    Char10But.configure(text=TableLike[ChoPage-1,10-1][0:len(TableLike[ChoPage-1,10-1])-1]+' :10')
    Char11But.configure(text=TableLike[ChoPage-1,11-1][0:len(TableLike[ChoPage-1,11-1])-1]+' :11')
    Char12But.configure(text=TableLike[ChoPage-1,12-1][0:len(TableLike[ChoPage-1,12-1])-1]+' :12')
    Char13But.configure(text=TableLike[ChoPage-1,13-1][0:len(TableLike[ChoPage-1,13-1])-1]+' :13')
    Char14But.configure(text=TableLike[ChoPage-1,14-1][0:len(TableLike[ChoPage-1,14-1])-1]+' :14')
    Char15But.configure(text=TableLike[ChoPage-1,15-1][0:len(TableLike[ChoPage-1,15-1])-1]+' :15')
    Char16But.configure(text=TableLike[ChoPage-1,16-1][0:len(TableLike[ChoPage-1,16-1])-1]+' :16')
    if '\n' in TableLike[ChoPage-1,17-1]:
        Char17But.configure(text=TableLike[ChoPage-1,17-1][0:len(TableLike[ChoPage-1,17-1])-1]+' - 17')
    else:
        Char17But.configure(text=TableLike[ChoPage-1,17-1][0:len(TableLike[ChoPage-1,17-1])]+' - 17')
    for elemred in range(17):
        if butredBD[ChoPage-1,elemred] == 1:
            butget(elemred+1).configure(bg='red',activebackground='red')
        else:
            butget(elemred+1).configure(bg='grey94',activebackground='grey94')
        
def fileupdate(): #Обновление файла
    global TableLike,filename
    BD2 = open(filename,'w')
    for line in range(4):
        for elem in range(17):  
            BD2.write(TableLike[line,elem])           
    for line in range(4):
        for elem in range(17):  
            BD2.write(str(butredBD[line,elem])+'\n')  
           
def butget(num): #Спец. фукция по возвращению нужной кнопки при получении номера кнопки 1-17
    global Char1But,Char2But,Char3But,Char4But,Char5But,Char6But,Char7But,Char8But,Char9But,Char10But,Char11But,Char12But,Char13But,Char14But,Char15But,Char16But,Char17But
    if num == 1:
        return Char1But
    elif num == 2:
        return Char2But
    elif num == 3:
        return Char3But
    elif num == 4:
        return Char4But
    elif num == 5:
        return Char5But
    elif num == 6:
        return Char6But
    elif num == 7:
        return Char7But
    elif num == 8:
        return Char8But
    elif num == 9:
        return Char9But
    elif num == 10:
        return Char10But
    elif num == 11:
        return Char11But
    elif num == 12:
        return Char12But
    elif num == 13:
        return Char13But
    elif num == 14:
        return Char14But
    elif num == 15:
        return Char15But
    elif num == 16:
        return Char16But
    elif num == 17:
        return Char17But
        
def charpat(num,but): #Функция всех кнопок
    global ChoChar,ChoPage,ChoChar2
    if flagred == 0:
        if ChoChar == 0:
            ChoChar = num
            print(TableLike[ChoPage-1,ChoChar-1])
            MainText2.delete(1.0,END)
            MainText2.insert(INSERT,TableLike[ChoPage-1,ChoChar-1]+'('+str(ChoChar)+')\n')
            butget(ChoChar).configure(bg='light goldenrod',activebackground='light goldenrod')
        else:
            ChoChar2 = num
            myname = TableLike[ChoPage-1,num-1]
            print(myname)
            TableLike[ChoPage-1,num-1] = TableLike[ChoPage-1,ChoChar-1]
            TableLike[ChoPage-1,ChoChar-1] = myname
            print(str(butredBD[ChoPage-1,ChoChar-1])+' '+str(butredBD[ChoPage-1,ChoChar2-1]))
            butredBD[ChoPage-1,ChoChar2-1],butredBD[ChoPage-1,ChoChar-1]=butredBD[ChoPage-1,ChoChar-1],butredBD[ChoPage-1,ChoChar2-1]
            print(TableLike)
            MainText2.insert(INSERT,'<>\n'+myname+'('+str(num)+')')
            print(butredBD)
            update()
            fileupdate()
            ChoChar = 0
    else:
        if butredBD[ChoPage-1,num-1] == 0:
            butredBD[ChoPage-1,num-1] = 1
            but.configure(bg='red',activebackground='red')
        else:
            butredBD[ChoPage-1,num-1] = 0
            but.configure(bg='grey94',activebackground='grey94')
        fileupdate()

def char1(): 
    charpat(1,Char1But)

def char2():
    charpat(2,Char2But)

def char3():
    charpat(3,Char3But)

def char4():
    charpat(4,Char4But)

def char5():
    charpat(5,Char5But)

def char6():
    charpat(6,Char6But)

def char7():
    charpat(7,Char7But)

def char8():
    charpat(8,Char8But)

def char9():
    charpat(9,Char9But)

def char10():
    charpat(10,Char10But)

def char11():
    charpat(11,Char11But)

def char12():
    charpat(12,Char12But)

def char13():
    charpat(13,Char13But)

def char14():
    charpat(14,Char14But)

def char15():
    charpat(15,Char15But)

def char16():
    charpat(16,Char16But)

def char17():
    charpat(17,Char17But)
    
def load2():
    global TableLike,filename,butredBD
    try:
        print('Поиск файла...')
        if BDLoad2Ent.get() == '':
            BD2 = open('BDLikes.gol','r')
            filename = 'BDLikes.gol'
        else:
            BD2 = open(BDLoad2Ent.get()+'.gol','r')
            filename = BDLoad2Ent.get()+'.gol'
        print('Фаил найден. Генерация пустых таблиц...') 
    except Exception as e:
        print('Фаил не найден')
    try:
        TableLike = np.array([['                                                                                                                                                                                                            ','','','','','','','','','','','','','','','',''],
                                ['','','','','','','','','','','','','','','','',''],
                                ['','','','','','','','','','','','','','','','',''],
                                ['','','','','','','','','','','','','','','','','']])
        butredBD = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
        print('Таблицы создана. Результат ниже')
        print(TableLike)
        print(butredBD)
    except Exception as e:
        print(e)
    linenum2 = 0
    objnum2 = 0
    g = 1
    for line in BD2:
        if g <= 68:
            try:
                TableLike[linenum2,objnum2] = line
                # print(str(linenum2)+' '+str(objnum2)+' '+str(line))
            except Exception as e:
                print(e)
            objnum2 = objnum2 + 1
            if objnum2 == 17:
                linenum2 = linenum2 + 1
                objnum2 = 0
            if g == 68:
                linenum2 = 0
                objnum2 = 0    
        if g >= 69:
            try:
                print(str(line))
                butredBD[linenum2,objnum2] = line
                # print(str(linenum2)+' '+str(objnum2)+' '+str(line))
            except Exception as e:
                print(e)
            objnum2 = objnum2 + 1
            if objnum2 == 17:
                linenum2 = linenum2 + 1
                objnum2 = 0
        g += 1
    print('Заполнение окончено. Результат ниже.')
    print(TableLike)
    print(butredBD)
    Char1But.configure(state='active')
    Char2But.configure(state='active')
    Char3But.configure(state='active')
    Char4But.configure(state='active')
    Char5But.configure(state='active')
    Char6But.configure(state='active')
    Char7But.configure(state='active')
    Char8But.configure(state='active')
    Char9But.configure(state='active')
    Char10But.configure(state='active')
    Char11But.configure(state='active')
    Char12But.configure(state='active')
    Char13But.configure(state='active')
    Char14But.configure(state='active')
    Char15But.configure(state='active')
    Char16But.configure(state='active')
    Char17But.configure(state='active')
    ButRed.configure(state='active')
    Pages.configure(state='normal')
    ButReset.configure(state='active')
    MainText2.delete(1.0, END)  
    MainText2.insert(INSERT,'*готов к работе*')
    BDLoad2But.configure(state='disabled')
    BDLoad2Ent.configure(state='disabled')
    ref()

def ref(): #Смена подразделения
    global ChoChar,ChoPage
    if Pages.get() == 'Перевозка':
        ChoPage = 1
        print('Выбрана '+str(ChoPage))
    elif Pages.get() == 'Укрепление':
        ChoPage = 2
        print('Выбрана '+str(ChoPage))
    elif Pages.get() == 'Исследование':
        ChoPage = 3
        print('Выбрана '+str(ChoPage))
    elif Pages.get() == 'Нападение':
        ChoPage = 4
        print('Выбрана '+str(ChoPage))
    update()
    
def red():
    global flagred
    if flagred == 0:
        flagred = 1
        ButRed.configure(bg='yellow')
    else:
        flagred = 0
        ButRed.configure(bg='grey94')
    
        

def selected(event):
    ref()

def reset1():
    ButReset.configure(bg="black", fg="red",text='Уверен?',command=reset2)
    
def reset2():
    global TableLike,butredBD
    try:
        for num in range(4):
            TableLike[num,0] = 'Ашлинг\n'
            TableLike[num,1] = 'Ваган\n'
            TableLike[num,2] = 'Воричи\n'   
            TableLike[num,3] = 'Гафф\n'   
            TableLike[num,4] = 'Гравиций\n'   
            TableLike[num,5] = 'Йоргин\n'   
            TableLike[num,6] = 'Корелл\n'   
            TableLike[num,7] = 'Камериа\n'   
            TableLike[num,8] = 'Лео\n'   
            TableLike[num,9] = 'Райкер\n'   
            TableLike[num,10] = 'Рин\n'   
            TableLike[num,11] = 'Тора\n'   
            TableLike[num,12] = 'То-Что-Сбежало\n'   
            TableLike[num,13] = 'Хаку\n'   
            TableLike[num,14] = 'Хиллок\n'   
            TableLike[num,15] = 'Элрон\n'   
            TableLike[num,16] = 'Янус\n'   
        for line in range(4):
            for elem in range(17):  
                butredBD[line,elem] = 0
        ref()
        fileupdate()
        ButReset.configure(bg="grey94", fg="black",text='По умолчанию',command=reset1)
        print('Произведен сброс.')
    except Exception as e:
        print(e)
BDLable = Label(tab1, text='БД >>>') #Раздел поиска по подразделению
BDLable.grid(column=0,row=0)
BDLoad1Ent = Entry(tab1)
BDLoad1Ent.grid(column=1,row=0)
BDLoadButton = Button(tab1, text='Load', command=load)
BDLoadButton.grid(column=2,row=0)
ListName1 = Combobox(tab1,state='disabled')
ListName1.bind('<<ComboboxSelected>>', detect)
ListName1['values']=('Перевозка','Укрепление','Исследование','Нападение')
ListName1.current(0)
ListName1.grid(column=0, row=1)  
ListName2 = Combobox(tab1,state='disabled')
ListName2.bind('<<ComboboxSelected>>', detect)
ListName2['values']=('Ашлинг','Камериа','Элрон','Гравиций','Гафф','Хиллок','Хаку','То-Что-Сбежало','Янус','Йоргин','Корелл','Лео','Райкер','Рин','Тора','Ваган','Воричи')
ListName2.current(0)
ListName2.grid(column=1, row=1) 
MainText = scrolledtext.ScrolledText(tab1,width=50,height=5)
MainText.grid(column=0,row=2,columnspan=3)
MainText.insert(INSERT,'                           ^                      Введите название базы, либо оставте свободным если вы ничего не меняли.')

SearchLable = Label(tab1, text='Ключевое слово >>> ') #Раздел поиска по слову
SearchLable.grid(column=0, row=4)
SearchEnt = Entry(tab1,state='disabled')
SearchEnt.grid(column=1,row=4)
SearchBut = Button(tab1, text='Поиск', command=search, state='disabled')
SearchBut.grid(column=2,row=4)
SearchText = scrolledtext.ScrolledText(tab1,width=50,height=5)
SearchText.grid(column=0,row=5,columnspan=3)
UpBut = Button(tab1, text='>>>',command=up, state='disabled')
UpBut.grid(column=2,row=6)
DownBut = Button(tab1, text='<<<',command=down, state='disabled')
DownBut.grid(column=0,row=6)
FindedLable = Label(tab1, text='0/0')
FindedLable.grid(column=1, row=6)
NameLabel = Label(tab1, text='>>>')
NameLabel.grid(column=1, row=7)

pix = 22 #Координаты 'y' кнопок
hei = 22 #Высота кнопок

Char1But = Button(tab2,text='',command=char1,state='disabled') #Вторая вкладка
Char1But.place(x=2,y=pix*1, height=hei, width=100)
Char2But = Button(tab2,text='',command=char2,state='disabled')
Char2But.place(x=2,y=pix*2, height=hei, width=100)
Char3But = Button(tab2,text='',command=char3,state='disabled')
Char3But.place(x=2,y=pix*3, height=hei, width=100)
Char4But = Button(tab2,text='',command=char4,state='disabled')
Char4But.place(x=2,y=pix*4, height=hei, width=100)
Char5But = Button(tab2,text='',command=char5,state='disabled')
Char5But.place(x=2,y=pix*5, height=hei, width=100)
Char6But = Button(tab2,text='',command=char6,state='disabled')
Char6But.place(x=2,y=pix*6, height=hei, width=100)
Char7But = Button(tab2,text='',command=char7,state='disabled')
Char7But.place(x=2,y=pix*7, height=hei, width=100)
Char8But = Button(tab2,text='',command=char8,state='disabled')
Char8But.place(x=2,y=pix*8, height=hei, width=100)
Char9But = Button(tab2,text='',command=char9,state='disabled')
Char9But.place(x=2,y=pix*9, height=hei, width=100)
Char10But = Button(tab2,text='',command=char10,state='disabled')
Char10But.place(x=2,y=pix*10, height=hei, width=100)
Char11But = Button(tab2,text='',command=char11,state='disabled')
Char11But.place(x=2,y=pix*11, height=hei, width=100)
Char12But = Button(tab2,text='',command=char12,state='disabled')
Char12But.place(x=2,y=pix*12, height=hei, width=100)
Char13But = Button(tab2,text='',command=char13,state='disabled')
Char13But.place(x=2,y=pix*13, height=hei, width=100)
Char14But = Button(tab2,text='',command=char14,state='disabled')
Char14But.place(x=2,y=pix*14, height=hei, width=100)
Char15But = Button(tab2,text='',command=char15,state='disabled')
Char15But.place(x=2,y=pix*15, height=hei, width=100)
Char16But = Button(tab2,text='',command=char16,state='disabled')
Char16But.place(x=2,y=pix*16, height=hei, width=100)
Char17But = Button(tab2,text='',command=char17,state='disabled')
Char17But.place(x=2,y=pix*17, height=hei, width=100)

LabelChar1 = Label(tab2,text='Выше')
LabelChar1.place(x=104,y=30)
LabelChar2 = Label(tab2,text='Ниже')
LabelChar2.place(x=104,y=364)
LabelChar3 = Label(tab2,text='Приоритет')
LabelChar3.place(x=104,y=180)
LabelChar4 = Label(tab2,text='||||')
LabelChar4.place(x=115,y=30*2)
LabelChar5 = Label(tab2,text='||||')
LabelChar5.place(x=115,y=30*3)
LabelChar6 = Label(tab2,text='||||')
LabelChar6.place(x=115,y=30*4)
LabelChar7 = Label(tab2,text='||||')
LabelChar7.place(x=115,y=30*5)
LabelChar8 = Label(tab2,text='||||')
LabelChar8.place(x=115,y=30*7)
LabelChar9 = Label(tab2,text='||||')
LabelChar9.place(x=115,y=30*8)
LabelChar10 = Label(tab2,text='||||')
LabelChar10.place(x=115,y=30*9)
LabelChar11 = Label(tab2,text='||||')
LabelChar11.place(x=115,y=30*10)
LabelChar12 = Label(tab2,text='||||')
LabelChar12.place(x=115,y=30*11)

Pages = Combobox(tab2,state='disabled') #Остальное на второй вкладке
Pages.bind('<<ComboboxSelected>>', selected)
Pages['values']=('Перевозка','Укрепление','Исследование','Нападение')
Pages.current(0)
Pages.place(x=0,y=0) 
BDLoad2Ent = Entry(tab2)
BDLoad2Ent.place(x=145,y=1)
BDLoad2But = Button(tab2,text='Load',command=load2)
BDLoad2But.place(x=250,y=0, height=21)
MainText2 = scrolledtext.ScrolledText(tab2,width=28,height=5)
MainText2.place(x=145,y=22)
MainText2.insert(INSERT,'^ Введите название базы, либо оставте свободным если вы ничего не меняли.')
ButRed = Button(tab2,text='Красная отметка',command=red,state='disabled')
ButRed.place(x=143,y=110)
ButReset = Button(tab2,text='По умолчанию',command=reset1,state='disabled')
ButReset.place(x=0,y=400)
win.mainloop()