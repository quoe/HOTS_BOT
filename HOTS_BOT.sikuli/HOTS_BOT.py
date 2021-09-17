from datetime import datetime
import shutil
import random
#from sys import argv
#HOTS = App.open("E:\Heroes of the Storm\Support64\HeroesSwitcher_x64.exe")
#HOTS.focus()
Settings.MoveMouseDelay = 0.02
Settings.LogTime = False
Settings.UserLogs = False
Settings.UserLogTime = False
LogInPass = "LogInPass"
timeWait = 60
LoadGameWait = 300
sleepTime = 7.7
WhileRepeat = 0
GameCount = 0
CurrentMap = "Карта не определена" #Текущая карта
LogFilePath = "D:\\"
ScreenshotFilePath = "D:/"
LogFileName = "Sikuli_HOTS_Log_" + datetime.strftime(datetime.now(), "%Y.%m.%d %H_%M_%S") + ".txt"
log = file(LogFilePath + LogFileName, "w")
defLoc_x = 521 #Нажатие по умолчанию в центр окна HOTS
defLoc_y = 403
defLoc_dx = 10
defLoc_dy = 10
defMidLoc_x = 881 #Нажатие по умолчанию в центр карты
defMidLoc_y = 643
defMidLoc_dx = 10
defMidLoc_dy = 10

Map1 = "Бухта Черносерда"
Map2 = "Драконий край"
Map3 = "Проклятая лощина"
Map4 = "Призрачные копи"
Map5 = "Сад ужасов"
Map6 = "Небесный храм"
Map7 = "Гробница королевы пауков"
Map8 = "Вечная битва"
Map9 = "Осквернённые святилища"
Map10 = "Башни Рока"

def latinizator(letter):
    legend = {
    #' ':'_',
    #',':'',
    'а':'a',
    'б':'b',
    'в':'v',
    'г':'g',
    'д':'d',
    'е':'e',
    'ё':'yo',
    'ж':'zh',
    'з':'z',
    'и':'i',
    'й':'y',
    'к':'k',
    'л':'l',
    'м':'m',
    'н':'n',
    'о':'o',
    'п':'p',
    'р':'r',
    'с':'s',
    'т':'t',
    'у':'u',
    'ф':'f',
    'х':'h',
    'ц':'c',
    'ч':'ch',
    'ш':'sh',
    'щ':'shch',
    'ъ':'y',
    'ы':'y',
    'ь':"'",
    'э':'e',
    'ю':'yu',
    'я':'ya',
    
    'А':'A',
    'Б':'B',
    'В':'V',
    'Г':'G',
    'Д':'D',
    'Е':'E',
    'Ё':'Yo',
    'Ж':'Zh',
    'З':'Z',
    'И':'I',
    'Й':'Y',
    'К':'K',
    'Л':'L',
    'М':'M',
    'Н':'N',
    'О':'O',
    'П':'P',
    'Р':'R',
    'С':'S',
    'Т':'T',
    'У':'U',
    'Ф':'F',
    'Х':'H',
    'Ц':'Ts',
    'Ч':'Ch',
    'Ш':'Sh',
    'Щ':'Shch',
    'Ъ':'Y',
    'Ы':'Y',
    'Ь':"'",
    'Э':'E',
    'Ю':'Yu',
    'Я':'Ya',
    }
    for i, j in legend.items():
        letter = letter.replace(i, j)
    return letter

def WriteLog(t):
    nl = "\n" # new line character
    log = open(LogFilePath + LogFileName, "a")
    TD = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + "\t"
    log.write(TD + t + nl)
    log.close()
    print(TD + latinizator(t))
    #Debug.user(TD + latinizator(t));

def randomClick(image, max_dx, max_dy):
    dx = random.randrange(-max_dx, max_dx)
    dy = random.randrange(-max_dy, max_dy)
    click(image.targetOffset(dx , dy))

def randomLocationClick(x, y, max_dx, max_dy):
    dx = random.randrange(-max_dx, max_dx)
    dy = random.randrange(-max_dy, max_dy)
    click(Location(x + dx, y + dy))
    
def randomLocationRightClick(x, y, max_dx, max_dy):
    dx = random.randrange(-max_dx, max_dx)
    dy = random.randrange(-max_dy, max_dy)
    rightClick(Location(x + dx, y + dy))

def randomRegionClick(Reg, max_dx, max_dy):
    randomLocationClick(round(Reg.getW()/2), round(Reg.getH()/2), max_dx, max_dy)
    
def KeyPress(key):
    keyDown(key)
    WriteLog("Нажата кнопка " + key)
    keyUp(key)
    WriteLog("Отпущена кнопка " + key)
    
def UseSkill(Reg, coord, base_x, base_y):
    baseOffset_x = base_x #28
    baseOffset_y = base_y #68
    max_dx = 20
    max_dy = 30
    dx = random.randrange(-max_dx, max_dx)
    dy = random.randrange(-max_dy, max_dy)
    WriteLog("Начало использования способностей")
    KeyPress("q")
    try:
        #click(coord)
        click(coord.targetOffset(baseOffset_x + dx, baseOffset_y + dy)) 
        WriteLog("Нажат объект для способности q")
    except:
        #click(Location(round(Reg.getW()/2), round(Reg.getH()/2)))
        randomRegionClick(Reg, max_dx, max_dy)
        WriteLog("Ошибка. Нажаты координаты по умолчанию")
        pass
    sleep(0.5)
    dx = random.randrange(-max_dx, max_dx)
    dy = random.randrange(-max_dy, max_dy)
    KeyPress("w")
    try:
        click(coord.targetOffset(baseOffset_x + dx, baseOffset_y + dy)) 
        WriteLog("Нажат объект для способности w")
    except:
        #click(Location(521, 403))
        #randomLocationClick(round(Reg.getW()/2), round(Reg.getH()/2), max_dx, max_dy)
        randomRegionClick(Reg, max_dx, max_dy)
        WriteLog("Ошибка. Нажаты координаты по умолчанию")
        pass
    sleep(0.5)
    dx = random.randrange(-max_dx, max_dx)
    dy = random.randrange(-max_dy, max_dy)
    KeyPress("e")
    try:
        click(coord.targetOffset(baseOffset_x + dx, baseOffset_y + dy)) 
        WriteLog("Нажат объект для способности e")
    except:
        randomRegionClick(Reg, max_dx, max_dy)
        WriteLog("Ошибка. Нажаты координаты по умолчанию")
        pass
    sleep(0.5)
    dx = random.randrange(-max_dx, max_dx)
    dy = random.randrange(-max_dy, max_dy)
    KeyPress("r")
    try:
        click(coord.targetOffset(baseOffset_x + dx, baseOffset_y + dy)) 
        WriteLog("Нажат объект для способности r")
    except:
        randomRegionClick(Reg, max_dx, max_dy)
        WriteLog("Ошибка. Нажаты координаты по умолчанию")
        pass
    sleep(0.5)
    keyUp()
    WriteLog("Конец использования способностей")
    
def CheckBots(HOTS):
    WriteLog("Проверка ботов")
    if HOTS.exists(Pattern("1460728184588.png").similar(0.98)):
        click(Pattern("1460728184588.png").similar(0.98).targetOffset(-45,-1))
        WriteLog("Поставлены союзники ИИ")
    if not HOTS.exists(Pattern("1460728073758.png").similar(0.90)):
        randomClick(Pattern("1460728073758.png").similar(0.75), 106, 9)
        randomClick(Pattern("1460728293641.png").similar(0.95), 54, 5)
        WriteLog("Выбрана сложность Новичок")
    if HOTS.exists(Pattern("1462033144228.png").similar(0.90)):
        WriteLog("Текущая сложность Адепт. Меняю сложность")
        randomClick(Pattern("1462033144228.png").similar(0.90), 106, 9)
        randomClick(Pattern("1460728293641.png").similar(0.95), 54, 5)
        WriteLog("Выбрана сложность Новичок")
    WriteLog("Конец проверки ботов")

def UpdateGameMode():
    sleep(2)
    randomClick(Pattern("1460728920454.png").similar(0.80), 36, 3)
    sleep(2)
    randomClick(Pattern("1460728957178.png").similar(0.80), 34, 4)
    sleep(2)
    
def LogIn():
    WriteLog("Начало авторизации")
    try:
        HOTS.wait(Pattern("1460727608234.png").similar(0.85), timeWait)
        paste(Pattern("1460727608234.png").similar(0.85), LogInPass)
        WriteLog("Введён пароль")
        randomClick(Pattern("1460727730727.png").similar(0.80), 56, 10)
        WriteLog("Подключение")
        sleep(6)
        if HOTS.exists(Pattern("1461733261130.png").similar(0.85)):
            WriteLog("Переподключение к игре")
            click(Pattern("1461733272455.png").similar(0.85)) 
            return
        if HOTS.exists(Pattern("1461074599787.png").similar(0.85)):
            WriteLog("Несовпадение версий. Выхожу из игры")
            randomClick(Pattern("1461074621210.png").similar(0.85), 56, 9)
            randomClick(Pattern("1461074675595.png").similar(0.85), 56, 9)
        HOTS.wait(Pattern("1460727826217.png").similar(0.85), timeWait)
        WriteLog("Подключение успешно")
        click(Pattern("1460727826217.png").similar(0.85).targetOffset(137,-4))
        UpdateGameMode()
    except:
        WriteLog("Ошибка при авторизации")
        pass
    WriteLog("Конец авторизации")
    
def SelectMap():
    WriteLog("Начало выбора карты")
    Map = "Карта не определена"
    if HOTS.exists(Pattern("1460730752977.png").exact()):
        Map = Map1
    if HOTS.exists(Pattern("1460730845585.png").exact()):
        Map = Map2
    if HOTS.exists(Pattern("1460730927513.png").exact()):
        Map = Map3
    if HOTS.exists(Pattern("1460731008716.png").exact()):
        Map = Map4
    if HOTS.exists(Pattern("1460731069343.png").exact()):
        Map = Map5
    if HOTS.exists(Pattern("1460731136221.png").exact()):
        Map = Map6
    if HOTS.exists(Pattern("1460731199310.png").exact()):
        Map = Map7
    if HOTS.exists(Pattern("1460729301600.png").exact()):
        Map = Map8
    if HOTS.exists(Pattern("1460731273230.png").exact()):
        Map = Map9
    if HOTS.exists(Pattern("1460731330733.png").exact()):
        Map = Map10
    WriteLog("Конец выбора карты")
    return Map

def takeScreenshot(Reg):
    try:
        img = capture(Reg) # img is an image file .png in temp folder now
        ScreenshotFileName = "Sikuli_HOTS_Log_" + datetime.strftime(datetime.now(), "%Y.%m.%d %H_%M_%S") + ".png"
        shutil.move(img, ScreenshotFilePath + ScreenshotFileName) # the target directory must exist
        return ScreenshotFilePath + ScreenshotFileName
    except:
        return "Снимок экрана не удался"

def StartFromDesktop():
    WriteLog("Запускаю HOTS через ярлык")
    if exists(Pattern("1461735092731.png").similar(0.85)):
        doubleClick(Pattern("1461735092731.png").similar(0.85))
        WriteLog("HOTS запущена через ярлык")
    WriteLog("HOTS не запущена через ярлык")

def CheckHP(HOTS, x, y, max_dx, max_dy):
    #Pattern("1462037768486.png").similar(0.97)
    result = False
    if HOTS.exists(Pattern("1462548602593.png").similar(0.97)):
        WriteLog("Мало жизней. Телепортация на базу")
        #rightClick(HeroPos)
        randomLocationRightClick(x, y, max_dx, max_dy)
        sleep(3)
        KeyPress("b")
        sleep(6.5)
        result = True
    return result

def UseSkillOnUnits(HOTS, img):
    units = []
    try:
        f = HOTS.findAll(img)
    except:
        return
    while f.hasNext(): # loop as long there is a first and more matches
        units.append(f.next())        # access next match and add to matches
    if len(units) > 0:
        WriteLog("Найдены юниты: " + str(len(units)))
        try:
            rightClick(img)
            sleep(2)
            UseSkill(HOTS, img, 0, 47)
        except:
            UseSkill(HOTS, img, 0, 47)
            pass

def ExitFromGameAndBot():
    WriteLog("Выход из игры") 
    randomClick(Pattern("1460372522086.png").similar(0.85), 30, 14)
    sleep(2)
    randomClick(Pattern("1460798201925.png").similar(0.85), 10, 12)
    sleep(1)
    randomClick(Pattern("1460798241017.png").similar(0.75), 66, 10)
    WriteLog("Выход из программы") 
    exit()

def FindSelf(HOTS, HOTS_map):
    if HOTS.exists(Pattern("1462508486661.png").similar(0.85)): #Найден бокс с положением героя на карте
        try:
            HeroPos = HOTS.find(Pattern("1462508486661.png").similar(0.85).targetOffset(0,17))
            hover(HeroPos)
            WriteLog("Найдена позиция героя: " + HeroPos)
            return HeroPos
        except:
            HeroPos = Location(round(HOTS_map.getW()/2), round(HOTS_map.getH()/2))
            return HeroPos
            pass

def FindSelfAndSleep(HOTS, HOTS_map, sleepTime):
    HeroPos = FindSelf(HOTS, HOTS_map)
    #randomLocationRightClick(HeroPos.x, HeroPos.y, 8, 8)
    #randomLocationClick(round(Reg.getW()/2), round(Reg.getH()/2), max_dx, max_dy)
    sleep(sleepTime)
    return HeroPos

def DeathClick():
    if HOTS.exists(Pattern("1462550194244.png").similar(0.80)):
        try:
            randomClick(Pattern("1462550247258.png").similar(0.90), 6, 7)
        except:
            pass
    
WriteLog("Начало")


HOTS = Region(4,22,1030,728)


HeroPos = Location(defMidLoc_x, defMidLoc_y)

if not (HOTS.exists(Pattern("1460380966426.png").targetOffset(-61,-5)) or HOTS.exists(Pattern("1460379321998.png").similar(0.85))):
    WriteLog("HOTS не запущена до главного цикла. Запускаю")
    StartFromDesktop()
    if HOTS.exists(Pattern("1460727608234.png").similar(0.85), timeWait):
        LogIn()
    
while True:
    WhileRepeat += 1
    WriteLog("Цикл: " + str(WhileRepeat))
    sleep(1)
    if HOTS.exists(Pattern("1460379321998.png").similar(0.85)):
        if HOTS.exists(Pattern("1460959014502.png").similar(0.85)):
            UpdateGameMode()
            
        if HOTS.exists(Pattern("1460372223956.png").similar(0.85)):
            WriteLog("Найдена кнопка начать игру")
            try:
                CheckBots(HOTS)
                randomClick(Pattern("1460372223956.png").similar(0.85), 84, 14)
                GameCount += 1
                WriteLog("Нажата кнопка начать игру. Игра: " + str(GameCount))
                sleep(7)
                CurrentMap = SelectMap()
                WriteLog(str(WhileRepeat) + "\t" + "Карта: " + CurrentMap + "\t" + str(GameCount))
            except:
                WriteLog("Не удалось нажать на начало игры. Нажимаю координатами")
                randomLocationClick(515, 695, 14, 14)
                pass

        if HOTS.exists(Pattern("1460798017005.png").similar(0.85)):
            WriteLog("Кончились доступные игры")  
            click(Pattern("1460798017005.png").similar(0.85).targetOffset(1,93))
            sleep(2)
            ExitFromGameAndBot()
        if HOTS.exists(Pattern("1460372522086.png").similar(0.85)):
            if HOTS.exists(Pattern("1460732413254.png").similar(0.85)):
                WriteLog("Матч не закончен. Выкинуло из игры")  
            else:
                WriteLog("Матч закончен успешно.")
                if HOTS.exists(Pattern("1461916973790.png").similar(0.85)):
                    WriteLog("Результат:\t" + "Победа")
                else:
                    WriteLog("Результат:\t" + "Поражение")
                    
                try:
                    hover(Pattern("1461044643637.png").similar(0.85))
                    sleep(1)
                    WriteLog("Сделан снимок сводки: " + takeScreenshot(HOTS))
                    randomClick(Pattern("1461044021289.png").similar(0.85), 33, 4)
                    sleep(2)
                    WriteLog("Сделан снимок статистики: " + takeScreenshot(HOTS))
                except:
                    WriteLog("Не удалось сделать снимки статистики")
                    pass
                
            WriteLog("Найдена кнопка выйти из сражения")
            randomClick(Pattern("1460372522086.png").similar(0.85), 56, 14)
            WriteLog("Нажата кнопка выйти из сражения")
            if GameCount == 5:
                WriteLog("Закончилась " + str(GameCount) + " игра. Перезагружаюсь")
                ExitFromGameAndBot()
    else:
        if HOTS.exists(Pattern("1460388929682.png").similar(0.98)):
            WriteLog("Найдена кнопка сесть на лошадь")
            try:
                click(Pattern("1460388929682.png").similar(0.98))
                WriteLog("Нажата кнопка на сесть на лошадь")
                sleep(1.2)
            except:
                #randomLocationClick(521, 403, 1, 1)
                KeyPress("z")
                WriteLog("Ошибка. Нажаты координаты по умолчанию")
                pass
        if CheckHP(HOTS, defMidLoc_x, defMidLoc_y, 8, 8):
            continue
        if HOTS.exists(Pattern("1460386418697.png").similar(0.87)):
            WriteLog("Найдена башня 1")
            KeyPress("a")
            try:
                randomClick(Pattern("1460386418697.png").similar(0.87), 6, 9)
                WriteLog("Нажата кнопка на башне 1")
                sleep(sleepTime)
            except:
                #randomLocationClick(defLoc_x, defLoc_y, defLoc_dx, defLoc_dy)
                #randomLocationClick(round(HOTS.getW()/2), round(HOTS.getH()/2), defLoc_dx, defLoc_dy)
                #randomRegionClick(HOTS_map, defMidLoc_dx, defMidLoc_dy)
                randomLocationClick(defMidLoc_x, defMidLoc_y, defMidLoc_dx, defMidLoc_dy)
                WriteLog("Ошибка. Нажаты координаты на карте по умолчанию")
                pass
            #UseSkill()
            #KeyPress("z")
        elif HOTS.exists(Pattern("1460625663740.png").similar(0.73)):
            WriteLog("Найдена башня 2")
            KeyPress("a")
            try:
                randomClick(Pattern("1460625663740.png").similar(0.73), 6, 9)
                WriteLog("Нажата кнопка на башне 2")
                sleep(sleepTime)
            except:
                #randomRegionClick(HOTS_map, defMidLoc_dx, defMidLoc_dy)
                randomLocationClick(defMidLoc_x, defMidLoc_y, defMidLoc_dx, defMidLoc_dy)
                WriteLog("Ошибка. Нажаты координаты на карте по умолчанию")
                pass
        elif HOTS.exists(Pattern("1460386592585.png").similar(0.85)):
            WriteLog("Найдена цитадель с соответствием 85")
            KeyPress("a")
            try:
                randomClick(Pattern("1460386592585.png").similar(0.85), 12, 10)
                WriteLog("Нажата кнопка на цитадели с соответствием 85")
                sleep(sleepTime)
            except:
                randomLocationClick(defMidLoc_x, defMidLoc_y, defMidLoc_dx, defMidLoc_dy)
                WriteLog("Ошибка. Нажаты координаты на карте по умолчанию")
                pass

        elif HOTS.exists(Pattern("1460625702443.png").similar(0.75)):
            WriteLog("Найдена цитадель с соответствием 75")
            KeyPress("a")
            try:
                randomClick(Pattern("1460625702443.png").similar(0.75), 12, 10)
                WriteLog("Нажата кнопка на цитадели с соответствием 75")
                sleep(sleepTime)
            except:
                #randomLocationClick(defLoc_x, defLoc_y, defLoc_dx, defLoc_dy)
                randomLocationClick(defMidLoc_x, defMidLoc_y, defMidLoc_dx, defMidLoc_dy)
                WriteLog("Ошибка. Нажаты координаты на карте по умолчанию")
                pass
        elif HOTS.exists(Pattern("1462549278874.png").similar(0.87)):
            WriteLog("Найден вражеский фонтан 1 с соответствием 87")
            KeyPress("a")
            try:
                randomClick(Pattern("1462549278874.png").similar(0.87), 5, 7)
                WriteLog("Нажат вражеский фонтан 1 с соответствием 87")
                sleep(sleepTime)
            except:
                randomLocationClick(defMidLoc_x, defMidLoc_y, defMidLoc_dx, defMidLoc_dy)
                WriteLog("Ошибка. Нажаты координаты на карте по умолчанию")
                pass
        elif HOTS.exists(Pattern("1462550591301.png").similar(0.88)):
            WriteLog("Найден вражеский фонтан 2 с соответствием 88")
            KeyPress("a")
            try:
                randomClick(Pattern("1462550591301.png").similar(0.88), 4, 5)
                WriteLog("Нажат вражеский фонтан 2 с соответствием 88")
                sleep(sleepTime)
            except:
                randomLocationClick(defMidLoc_x, defMidLoc_y, defMidLoc_dx, defMidLoc_dy)
                WriteLog("Ошибка. Нажаты координаты на карте по умолчанию")
                pass
        else: 
            WriteLog("Не найдено объектов. Иду в цент карты.")
            KeyPress("a")
            try:
                randomLocationClick(defMidLoc_x, defMidLoc_y, defMidLoc_dx, defMidLoc_dy)
                sleep(sleepTime)
            except:
                randomRegionClick(HOTS, defLoc_dx, defLoc_dy)
                WriteLog("Ошибка. Нажаты координаты центра окна по умолчанию")
                pass
            continue
        #if WhileRepeat % 1 == 0: 
            #HeroPos = FindSelf(HOTS)
        while HOTS.exists(Pattern("1460625792087.png").similar(0.94).targetOffset(31,87)):
            WriteLog("Найдены жизни врага")
            UseSkill(HOTS, Pattern("1460625792087.png").similar(0.94), 28, 68)
        while HOTS.exists(Pattern("1460626025154.png").similar(0.85).targetOffset(31,88)):
            WriteLog("Найдены жизни башни")
            UseSkill(HOTS, Pattern("1460626025154.png").similar(0.93), 33, 145)
        while HOTS.exists(Pattern("1462481496303.png").similar(0.80)):    
            UseSkillOnUnits(HOTS, Pattern("1462481496303.png").similar(0.80))

            
        if WhileRepeat % 10 == 0:     
            if HOTS.exists(Pattern("1460625999994.png").similar(0.85)):
                WriteLog("Найдена кнопка закрытия окна")
                try:
                    randomClick(Pattern("1460625999994.png").similar(0.85), 6, 3)
                    WriteLog("Нажата кнопка закрытия окна")
                except:
                    type(Key.TAB)
                    WriteLog("Ошибка. Нажата кнопка TAB")
                    pass
        if HOTS.exists("1460382029325.png"):
            WriteLog("Найден новый талант")
            if HOTS.exists("1460380202682.png"):
                WriteLog("Найдено сообщение с выбором таланта")
                click(Pattern("1460380966426.png").targetOffset(-61,-5)) 
                click(Pattern("1460381094880.png").targetOffset(-6,-349)) 
                click(Pattern("1460381094880.png").targetOffset(-6,-300)) 
                click(Pattern("1460381094880.png").targetOffset(-4,-248)) 
                click(Pattern("1460381094880.png").targetOffset(-5,-198)) 
                WriteLog("Выбран талант из сообщения с выбором таланта")
            else:
                click(Pattern("1460381094880.png").targetOffset(-6,-349)) 
                click(Pattern("1460381094880.png").targetOffset(-6,-300)) 
                click(Pattern("1460381094880.png").targetOffset(-4,-248)) 
                click(Pattern("1460381094880.png").targetOffset(-5,-198)) 
                WriteLog("Выбран новый талант")
    if WhileRepeat % 25 == 0:
        if HOTS.exists(Pattern("1461918637455.png").similar(0.85)):  
            click(Pattern("1461918637455.png").similar(0.85).targetOffset(91,0))
            UpdateGameMode()
            
        if exists(Pattern("1461734966847.png").similar(0.95)):
            WriteLog("HOTS вылетела")
            click(Pattern("1461734966847.png").similar(0.95))
            sleep(5)
            StartFromDesktop()
            
        if exists("1461074157680.png"):
            WriteLog("HOTS вылетела с ошибкой")
            try:
                if HOTS.exists(Pattern("1461940154596.png").similar(0.85)):
                    WriteLog("Неизвестная ошибка. Переустановите игру")
                if HOTS.exists(Pattern("1460727456762.png").similar(0.80)):
                    WriteLog("Непредусмотрительная фатальная ошибка")
                if HOTS.exists(Pattern("1461074233727.png").similar(0.80)):
                    WriteLog("Ядро: попытка расширить, перегруппировать или освободить неизвестный блок памяти")
            except:
                pass
            if exists(Pattern("1460727491914.png").similar(0.97).targetOffset(-63,0)):
                click(Pattern("1460727491914.png").similar(0.97).targetOffset(-63,0))
            WriteLog("Перезапуск игры")
            click("1460727557766.png")
            LogIn()
        elif exists(Pattern("1461735092731.png").similar(0.85)):
            WriteLog("Найден ярлык на рабочем столе")
            StartFromDesktop()
    















    

    
    