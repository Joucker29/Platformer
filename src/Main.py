# 3 SVATÁ PRAVIDLA  
# ----------------  
  
# - PÍŠEME V ČEŠTINĚ!  
# - KOMENTÁŘE!  
# - nebuď debil :)  
 
# Knihovny ------------------------------------------------------------------------------------  
import pygame, sys, random, time, math, csv, glob, os, pathlib, re, time  
from pygame.locals import *  
pygame.init()  
  
# Barvy ---------------------------------------------------------------------------------------  
Bílá = (255, 255, 255)  
Černá = (0, 0, 0)  
Šedá = (121, 116, 113)  
Hnědá = (145, 79, 59)  
Krémová = (249,235,209)  
Oranžová = (255, 190, 20)  
Červená = (235, 4, 44)  
Žlutá = (255, 238, 3)  
Zelená = (151, 207, 138)  
Cyane = (36, 230, 251)  
Fialová = (159, 43, 104)  
Random_barva = ((random.randint(50,170),random.randint(50,170),random.randint(50,170)))  
          
# Inicializace okna ---------------------------------------------------------------------------  
pygame.display.set_caption("Testík")  
TPS = 144 
  
# Proměnné okna -------------------------------------------------------------------------------  
Šířka_okna = 1600 # Dopuručujeme 1600  
Výška_okna = (Šířka_okna/16)*9 # 16:9  
Okno = pygame.display.set_mode((round(Šířka_okna), round(Výška_okna)))  
  
# Proměnné hráče ------------------------------------------------------------------------------  
Šířka_hráče_sprite = Šířka_okna/48  
Výška_hráče_sprite = Šířka_okna/40
Šířka_hráče = Šířka_okna/48
Výška_hráče = Šířka_okna/40 
Pozice_hráče_x = (Šířka_okna/2)-Šířka_hráče/2  
Pozice_hráče_y = (Výška_okna/2)-Výška_hráče/2  
Rychlost_hráče = ((Šířka_okna / TPS)/(3/2))/8  
max_rychlost = Šířka_okna/200  
Storage_max_rychlost = max_rychlost # tohle je pro booster kostku  
storage_Rychlost_hráče = Rychlost_hráče  
Výška_skoku = round(Šířka_okna/110)  
Gravitace = (Šířka_okna/2300)  
Hráč = pygame.Rect(Pozice_hráče_x, Pozice_hráče_y, Šířka_hráče, Výška_hráče)  
dx = Šířka_hráče/8 # Šířka_hráče/20  
dy = Výška_hráče/5 # Výška_hráče/20  
  
# Spuštění-------------------------------------------------------------------------------------  
hra = False  
editor = False  
výběr_levelu_menu = False  
nastavení = False  
hlavnímenu = True  
Upravení_levelu = False  
Vytvoření_levelu = False  
nastavení = False  
  
# Scroll----------------------------------------------------------------------------------------  
scroll_rychlost = (Šířka_okna/TPS) # Za 2s přejede obrazovku jednou  
zastaveni_scrollu_vlevo, zastaveni_scrollu_vpravo, zastaveni_scrollu_nahoru, zastaveni_scrollu_dolu = False, False, False, False  
Aktuální_řada = 0 # Proměnná, která nám říká na jaké řadě je aktuálně kurzor  
Max_sloupců = 300+1 # Počet sloupců (vertikálně) v editoru (+1, protože do posledního sloupce se nedá umístit kostka)  
Počet_řad = 30 # Počet řad (horizontálně) v editoru  
Velikost_čtverce = Šířka_okna/32  
překážky = []  
  
# Tlačítka ------------------------------------------------------------------------------------  
Šířka_tlačítka = round(Šířka_okna/4)  
Výška_tlačítka = round(Výška_okna/8,4375)  
Kliknutí = False  
Editor_menu_zapnuto = False  
Počet_tlačítek = 0  
Stisknuté_tlačítko = 0  
  
# Pozice a velikosti tlačítek -----------------------------------------------------------------  
tlacitko_zmacknuto = False  
Play = pygame.Rect(Šířka_okna/2 - Šířka_tlačítka*1.5/2, Výška_okna/2.5 - Výška_tlačítka*1.5 + Šířka_okna/32, Šířka_tlačítka*1.5, Výška_tlačítka*1.5)  
Editor = pygame.Rect(Šířka_okna/2 - Šířka_tlačítka*1.5/2, Výška_okna/1.5 - Výška_tlačítka*1.5 + Šířka_okna/32, Šířka_tlačítka*1.5, Výška_tlačítka*1.5)  
Zpět_menu = pygame.Rect(Šířka_okna/4.3 - Šířka_tlačítka*1.7/2, Výška_okna/7 - Výška_tlačítka*1.5 + Výška_tlačítka/2, Šířka_tlačítka/2, Výška_tlačítka/2)  
Uložit_tlačítko = pygame.Rect(Šířka_okna - Šířka_tlačítka*.6, Výška_okna - Výška_tlačítka*.6, Šířka_tlačítka/2, Výška_tlačítka/2)  
Editor_menu = pygame.Rect(Šířka_okna / 2 - Šířka_tlačítka*1.5/2, Výška_okna/2 - Výška_tlačítka*4/2, Šířka_tlačítka*1.5, Výška_tlačítka*4)  
Easy = pygame.Rect(Šířka_okna/2 - Šířka_tlačítka/.8/2, Výška_okna/2.5 - Výška_tlačítka/.8, Šířka_tlačítka/.8, Výška_tlačítka/.8)  
Medium = pygame.Rect(Šířka_okna/2 - Šířka_tlačítka/.8/2, Výška_okna/1.63 - Výška_tlačítka/.8, Šířka_tlačítka/.8, Výška_tlačítka/.8)  
Hard = pygame.Rect(Šířka_okna/2 - Šířka_tlačítka/.8/2, Výška_okna/1.2 - Výška_tlačítka/.8, Šířka_tlačítka/.8, Výška_tlačítka/.8)  
Editor_menu_tlacitka = [((Editor_menu[0] + (Editor_menu[2]*1)/12, Editor_menu[1] + (Editor_menu[3]*1)/12 , Editor_menu[2]/6, Editor_menu[3]/6)), ((Editor_menu[0] + (Editor_menu[2]*5)/12, Editor_menu[1] + (Editor_menu[3]*1)/12 , Editor_menu[2]/6, Editor_menu[3]/6)), ((Editor_menu[0] + (Editor_menu[2]*9)/12, Editor_menu[1] + (Editor_menu[3]*1)/12 , Editor_menu[2]/6, Editor_menu[3]/6)),  
                        ((Editor_menu[0] + (Editor_menu[2]*1)/12, Editor_menu[1] + (Editor_menu[3]*5)/12 , Editor_menu[2]/6, Editor_menu[3]/6)), ((Editor_menu[0] + (Editor_menu[2]*5)/12, Editor_menu[1] + (Editor_menu[3]*5)/12 , Editor_menu[2]/6, Editor_menu[3]/6)), ((Editor_menu[0] + (Editor_menu[2]*9)/12, Editor_menu[1] + (Editor_menu[3]*5)/12 , Editor_menu[2]/6, Editor_menu[3]/6)),  
                        ((Editor_menu[0] + (Editor_menu[2]*1)/12, Editor_menu[1] + (Editor_menu[3]*9)/12 , Editor_menu[2]/6, Editor_menu[3]/6)), ((Editor_menu[0] + (Editor_menu[2]*5)/12, Editor_menu[1] + (Editor_menu[3]*9)/12 , Editor_menu[2]/6, Editor_menu[3]/6)), ((Editor_menu[0] + (Editor_menu[2]*9)/12, Editor_menu[1] + (Editor_menu[3]*9)/12 , Editor_menu[2]/6, Editor_menu[3]/6))]  
  
Zpráva = pygame.Rect(Šířka_okna/2-Šířka_tlačítka, Výška_okna/2-Výška_tlačítka, Šířka_tlačítka*2, Výška_tlačítka*2) # Level XX byl vytvořen...  
Hrát_level = pygame.Rect(((Šířka_okna/2))-Šířka_tlačítka/2, Výška_okna/3 - Výška_tlačítka/2, Šířka_tlačítka*1.15, Výška_tlačítka*1.15)  
Upravit_level = pygame.Rect(((Šířka_okna/2))-Šířka_tlačítka/2, Výška_okna/1.75 - Výška_tlačítka/2, Šířka_tlačítka*1.15, Výška_tlačítka*1.15)  
Smazat_level = pygame.Rect(((Šířka_okna/2))-Šířka_tlačítka/2, Výška_okna/1.25 - Výška_tlačítka/2, Šířka_tlačítka*1.15, Výška_tlačítka*1.15)  
Tabule_level = pygame.Rect(Šířka_okna/2-Šířka_tlačítka, -Šířka_okna/50, Šířka_tlačítka*2, Výška_tlačítka*2) # Pro text :)  
Pause_rect = pygame.Rect(Šířka_okna/2 - Šířka_okna/4, 0, Šířka_okna/2, Výška_okna)  
Pause_label = pygame.Rect(Šířka_okna/2 - Šířka_okna/4, Výška_okna/3.2 - Výška_okna/16, Šířka_okna/2, Výška_okna/8)  
Zpět = pygame.Rect(Šířka_okna/2 - Šířka_tlačítka/2 - round(Šířka_okna/13,33), Výška_okna/1.4 - Výška_tlačítka, Šířka_tlačítka/2, Výška_tlačítka) # Použito pro výhru a prohru  
Reset = pygame.Rect(Šířka_okna/2 - Šířka_tlačítka/2 + round(Šířka_okna/5), Výška_okna/1.4 - Výška_tlačítka, Šířka_tlačítka/2, Výška_tlačítka) # Použito pro výhru a prohru  
Timer_lavel = pygame.Rect(Šířka_okna/2 - Šířka_tlačítka/2, Výška_okna/1.9 - Výška_tlačítka, Šířka_tlačítka, Výška_tlačítka)  
Pause_tlačítko_hra = pygame.Rect(Výška_tlačítka / 4, Výška_tlačítka / 8, Výška_tlačítka/3, Výška_tlačítka/1.5)  
Zpět_hra = pygame.Rect(Šířka_okna/2 - Šířka_tlačítka/2, Výška_okna/1.82 - Výška_tlačítka, Šířka_tlačítka, Výška_tlačítka) # Tlačítko pro vrácení se do hry z pause menu  
  
# Ostatní -------------------------------------------------------------------------------------  
max_rychlost_enemy = Šířka_okna/600  
Rychlost_enemák = Šířka_okna/600  
pause_povrch = pygame.Surface((Šířka_okna/2, Výška_okna/2), pygame.SRCALPHA) # Povrch pro pause menu, https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangle-in-pygame   
pause_povrch.set_alpha(200)   
pause_povrch.fill((100,100,100,250))  
výběr_povrch = pygame.Surface((Šířka_okna/2.5, Výška_okna/1.75), pygame.SRCALPHA)  
výběr_povrch.set_alpha(200)   
výběr_povrch.fill((100,100,100,250))  
dash_rychlost = 30  
Hráč_životy = 5 # Kolik životů má hráč  
Enemy_životy = 1 # kolik životů má Enemy  
Obtížnost = 0 # 0 = ez, 1 = med., 2 = hard  
_timer = 0  
scroll_rychlost_dělitel = 10  
vel_y = 0  
vel_x = 0  
scroll_x = 0  
scroll_y = 0  
reset_číslo = 0 # Pro funkci debounce  
Číslo = 0  
Časovač = 0  
Počet_levelů = 0  
Řada_tlačítka = 0 # Používá se pro tvorbu tlačítek v menu úprava levelů  
Respawn_kostka_pozice = 0  
Respawn_kostka_pozice_1 = 0  
Spawner_kostka_položena = 0  
typ_kolize_enemy = 0  
DB_alpha = 0  
otevřený_level = 0 # Aktuálně otevřený level  
Start, Stop, Start1, Stop1 = 0, 0, 0, 0  
Enemák = pygame.Rect(1, 1, 1, 1)# je jedno co tady je protože se to stejně později přepíše  
pohyb = [0, 0]  
pohyb_enemák = [0, 0]  
Kostky_rect_list = [] 
Kostky_rect_list_enemy = [] 
kostky = []  
ctverec = []  
prekazky = []  
Úprava_levelu_tlačítka = [] 
Soubory = [] # Jména levelů 
životy = [] 
Enemy_kostky = [] 
Reset_enemáky = [] 
animace_pohyb = [] 
Zprávy = ["Možná si zvol lehčí obtížnost", "To bylo omylem?", "Anoo, určitě to byla chyba počítače", "Máš vůbec zapojenou klávesnici?", "Tip: nedotýkej se červených kostek", "Ups", "Smůla :("]  
dash = False  
skok = True  
Real_pause = False  
spustit_jednou = True  
Enemy_kill = False  
Enemy_skok = False  
Obtížnost_menu = False  
změna = False  
Pause = False  
Death = False  
Pausnuto = False  
Fake_smrt = False  
Nápověda = False  
Death_msg = "" # Pro zprávu po (real) smrti  
Poslední_zmáčknutá_šipka = "Right" # aby se otočil správně podle toho co zmáčknete i když nic nedržíte (spawne se a bude koukat do Prava)  
# Poslední_zmáčknutá_šipka = "Left" or Poslední_zmáčknutá_šipka = "Right"  
Složka_levely = (str(pathlib.Path(__file__).resolve().parent)+"\\Levely")  
Složka_postava = (str(pathlib.Path(__file__).resolve().parent)+"\\Sprity\\Postava")  
Složka_sprity = (str(pathlib.Path(__file__).resolve().parent)+"\\Sprity")  
Složka_checkpoint = (str(pathlib.Path(__file__).resolve().parent)+"\\Sprity\\Checkpoint")  
Složka_enemy = (str(pathlib.Path(__file__).resolve().parent)+"\\Sprity\\Enemy")  
  
# Loadování animací ---------------------------------------------------------------------------  
os.chdir(Složka_postava)  
run_0 = pygame.image.load("run/0.png").convert_alpha()  
run_1 = pygame.image.load("run/1.png").convert_alpha()  
fall_0 = pygame.image.load("fall/0.png").convert_alpha()  
idle_0 = pygame.image.load("idle/0.png").convert_alpha()  
idle_1 = pygame.image.load("idle/1.png").convert_alpha()  
jump_0 = pygame.image.load("jump/0.png").convert_alpha()  
death_0 = pygame.image.load("death/0.png").convert_alpha()  
animace_list = [run_0, run_1, fall_0, idle_0, idle_1, jump_0, death_0]  
for i, animace in enumerate(animace_list):  
    animace_list[i] = pygame.transform.scale(animace_list[i], (int(Šířka_hráče_sprite + Šířka_hráče_sprite/3), int(Výška_hráče_sprite + Výška_hráče/5))) # Velikost spritu  
run_0 = animace_list[0]  
run_1 = animace_list[1]  
fall_0 = animace_list[2]  
idle_0 = animace_list[3]  
idle_1 = animace_list[4]  
jump_0 = animace_list[5]  
death_0 = animace_list[6]  
  
# Loadování spritů -------------------------------------------------------------------------  
os.chdir(Složka_sprity)  
  
brick = pygame.image.load("Brick/0.png").convert_alpha() # to .convert má prý zlepšit performance ale nwm   
kill_kostka = pygame.image.load("Kill/0.png").convert_alpha()  
secret = pygame.image.load("Secret/1.png").convert_alpha()  
booster_0 = pygame.image.load("Booster/0.png").convert_alpha()  
booster_1 = pygame.image.load("Booster/1.png").convert_alpha()  
elevator_0 = pygame.image.load("Elevator/0.png").convert_alpha()  
elevator_1 = pygame.image.load("Elevator/1.png").convert_alpha()  
finish_0 = pygame.image.load("Finish/0.png").convert_alpha()  
finish_1 = pygame.image.load("Finish/1.png").convert_alpha()  
spawn_0 = pygame.image.load("Spawn/0.png").convert_alpha()  
spawn_1 = pygame.image.load("Spawn/1.png").convert_alpha()  
heart = pygame.image.load("Heart/0.png").convert_alpha() 
 
os.chdir(Složka_checkpoint)  
chechpoint_idle_0 = pygame.image.load("idle/0.png").convert_alpha()  
chechpoint_idle_1 = pygame.image.load("idle/1.png").convert_alpha()  
checkpoint_0 = pygame.image.load("rise/0.png").convert_alpha()  
checkpoint_1 = pygame.image.load("rise/1.png").convert_alpha()  
checkpoint_2 = pygame.image.load("rise/2.png").convert_alpha()  
checkpoint_3 = pygame.image.load("rise/3.png").convert_alpha()  
checkpoint_4 = pygame.image.load("rise/4.png").convert_alpha()  
checkpoint_5 = pygame.image.load("rise/5.png").convert_alpha()  
  
os.chdir(Složka_enemy)  
enemy_run_0 = pygame.image.load("run/0.png").convert_alpha()  
enemy_run_1 = pygame.image.load("run/1.png").convert_alpha()  
Kostky_sprity_list = [brick, kill_kostka, secret, booster_0, booster_1, elevator_0, elevator_1, finish_0, finish_1, spawn_0, spawn_1, chechpoint_idle_0, chechpoint_idle_1, checkpoint_0, checkpoint_1, checkpoint_2, checkpoint_3, checkpoint_4, checkpoint_5, enemy_run_0, enemy_run_1, heart]  
for i, sprite in enumerate(Kostky_sprity_list):  
    Kostky_sprity_list[i] =  pygame.transform.scale(Kostky_sprity_list[i], (int(Velikost_čtverce), int(Velikost_čtverce))) # Velikost spritu  
brick = Kostky_sprity_list[0]  
kill_kostka = Kostky_sprity_list[1]  
secret = Kostky_sprity_list[2]  
booster_0 = Kostky_sprity_list[3]  
booster_1 = Kostky_sprity_list[4]  
elevator_0 = Kostky_sprity_list[5]  
elevator_1 = Kostky_sprity_list[6]  
finish_0 = Kostky_sprity_list[7]  
finish_1 = Kostky_sprity_list[8]  
spawn_0 = Kostky_sprity_list[9]  
spawn_1 = Kostky_sprity_list[10]  
chechpoint_idle_0 = Kostky_sprity_list[11]  
chechpoint_idle_1 = Kostky_sprity_list[12]  
checkpoint_0 = Kostky_sprity_list[13]  
checkpoint_1 = Kostky_sprity_list[14]  
checkpoint_2 = Kostky_sprity_list[15]  
checkpoint_3 = Kostky_sprity_list[16]  
checkpoint_4 = Kostky_sprity_list[17]  
checkpoint_5 = Kostky_sprity_list[18]  
enemy_run_0 = Kostky_sprity_list[19]  
enemy_run_1 = Kostky_sprity_list[20]  
heart = Kostky_sprity_list[21]  
  
# Animace timer -----------------------------------------------------------------------------  
timer_list = []   
for i in range(10): # 0 go brrrrr @&{#&}łŁŁłĐĐĐĐ  
    timer_list.append(0)  
      
# Animace přehrávání --------------------------------------------------------------------------  
animation_timer = 0  
animation_timer_idle = 0  
  
# Funkce --------------------------------------------------------------------------------------  
def Real_smrt(Obtížnost): # Když Umřeš A NEMÁŠ ŽIVOTY!  
    global hra, Death, reset_číslo, Zprávy, Death_msg, Fake_smrt, timer_list  
    Fake_smrt = False  
    timer_list[3] = 0  
    Death = True  
    hra = False  
    reset_číslo = 0  
    Death_msg = str(Zprávy[random.randint(0, len(Zprávy)-1)])  
  
# ---------------------------------------------------------------------------------------------  
def Výhra(): # Když vyhraješ....  
    global hra, Pause, reset_číslo, Stop, Stop1, Start1  
    Pause = True  
    hra = False  
    Stop = ((Stop1 - Start1)) + Stop  
    reset_číslo = 0  
  
# ---------------------------------------------------------------------------------------------  
def Čas(Sekundy): # Pro počítání minut a sekund ze sekund  
    global Stop1, Stop, Start1  
    Sekundy -= (Stop1 - Start1) # Odebere počet sekund strávených v menu od počtu celkových sekund (takto dostaneme čas strávený čistě hraním)  
    Minuty = 0  
    Minuty_msg = "Chyba!"  
    Sekundy_msg = "Chyba!"  
    Minuty, Sekundy = divmod(Sekundy, 60)  
    Sekundy, Minuty = round(Sekundy), round(Minuty)  
    if Sekundy <= 0: # Lazy fix, cry about it  
        Sekundy += (1 - Sekundy)  
  
    if Sekundy == 1:  
        Sekundy_msg = (str(Sekundy) + " sekundu")  
    if Sekundy > 1 and Sekundy < 5:  
        Sekundy_msg = (str(Sekundy) + " sekundy")  
    if Sekundy >= 5:  
        Sekundy_msg = (str(Sekundy) + " sekund")  
      
    if Minuty == 1:  
        Minuty_msg = (str(Minuty) + " minutu")  
    if Minuty > 1 and Minuty < 5:  
        Minuty_msg = (str(Minuty) + " minuty")  
    if Minuty >= 5:  
        Minuty_msg = (str(Minuty) + " minut")  
      
    if Sekundy == 0 and Minuty != 0:  
        return(Minuty_msg)  
    if Sekundy != 0 and Minuty == 0:  
        return(Sekundy_msg)  
    if Sekundy != 0 and Minuty != 0:  
        return(str(Minuty_msg) + " a " + str(Sekundy_msg))  
      
# ---------------------------------------------------------------------------------------------  
def timer(délka): # délka ve frame (délka*TPS) = 1 sekunda  
    global _timer  
    Timer = False  
    _timer += 1  
    if _timer > délka + 1:#reset  
        _timer = 0  
          
    if _timer > délka:  
        Timer = True  
          
    if _timer < délka:  
        Timer = False  
    return Timer   
   
# ---------------------------------------------------------------------------------------------  
def vytvořit_tlačítka_úprav_levelů():  
    global Úprava_levelu_tlačítka, Počet_levelů, Řada_tlačítka  
      
    Úprava_levelu_tlačítka.clear()  
    Soubory.clear()  
    Počet_levelů = 0  
    Řada_tlačítka = 0  
      
    os.chdir(Složka_levely)  
    for soubor in glob.glob("*.txt"): # Zjistí, kolik levelů již existuje  
        Úprava_levelu_tlačítka.append(pygame.Rect(((Šířka_okna/5.7)-Šířka_tlačítka/2)+((Šířka_okna/3.2)*Počet_levelů), ((Výška_okna/4)-Výška_tlačítka/2)+((Výška_okna/6)*Řada_tlačítka), Šířka_tlačítka, Výška_tlačítka))  
        Počet_levelů += 1  
  
        if Počet_levelů >= 3: # Aby se správně vytvářely řady  
            Počet_levelů = 0  
            Řada_tlačítka += 1  
  
        txt = (str(soubor)) # Vezme název souboru  
        souborbeztxt = txt.rsplit(".", 1) # Vše za tečkou "odebere"  
        res = [re.findall(r'(\w+?)(\d+)', souborbeztxt[0])[0]] # https://www.geeksforgeeks.org/python-splitting-text-and-number-in-string :)  
        finalnistring = (str(res[0][0]) + " " + str(res[0][1]))   
  
        Soubory.append(finalnistring) # Appenduje  
        Soubory.sort(key = len) # Řazení podle délky stringu  
          
    Úprava_levelu_tlačítka.append(pygame.Rect(((Šířka_okna/5.7)-Šířka_tlačítka/2)+((Šířka_okna/3.2)*Počet_levelů), ((Výška_okna/4)-Výška_tlačítka/2)+((Výška_okna/6)*Řada_tlačítka), Šířka_tlačítka, Výška_tlačítka))  
  
# --------------------------------------------------------------------------------------  
def vytvořit_level():  
    Počet_levelů = 0  
    os.chdir(Složka_levely)  
      
    for soubor in glob.glob("*.txt"):  
        Počet_levelů += 1  
      
    level = open("Level" + str(Počet_levelů + 1) + ".txt", "w+")  
      
    return (Počet_levelů+1)  
  
# --------------------------------------------------------------------------------------  
def debounce():  
    global reset_číslo  
    vysledek = False  
    reset_číslo+=1  
    if reset_číslo == 1:  
        vysledek = True  
    if reset_číslo != 1:  
        vysledek = False  
    return vysledek  
      
# ---------------------------------------------------------------------------------------------  
def teleport(x, y):  
    global Výška_hráče, Šířka_hráče  
    rect = pygame.Rect(x, y, Šířka_hráče, Výška_hráče)  
      
    return rect  
      
# ---------------------------------------------------------------------------------------------   
def draw():  
    global scroll, Max_sloupců  
    for sloupec in range(Max_sloupců + 1):  
        pygame.draw.line(Okno, Bílá, (sloupec * Velikost_čtverce - scroll_x, 0), (sloupec * Velikost_čtverce - scroll_x, Výška_okna))  
    for řada in range(Počet_řad + 1):  
        pygame.draw.line(Okno, Bílá, (0, řada * Velikost_čtverce - scroll_y), (Šířka_okna, řada * Velikost_čtverce - scroll_y))  
          
# ---------------------------------------------------------------------------------------------      
def test_kolizí(rect, kostky):  
    kolize = []  
    for kostka in kostky:  
        if rect.colliderect(kostka):  
            kolize.append(kostka)  
    return kolize  
  
# ---------------------------------------------------------------------------------------------  
def move(rect, pohyb, kostky, skok):   
    global Gravitace, Šířka_okna, Výška_okna, _timer, scroll_x, scroll_y   
    typ_kolize = {'zhora' : False, 'zdola' : False, 'zleva' : False, 'zprava' : False}  
    rect.x += pohyb[0]  
    kolize = test_kolizí(rect,kostky)  
      
    for kostka in kolize:  
        if pohyb[0] > 0:  
            pohyb[0] = 0  
            rect.right = kostka.left  
            typ_kolize['zprava'] = True  
              
        if pohyb[0] < 0:  
            pohyb[0] = 0  
            rect.left = kostka.right  
            typ_kolize['zleva'] = True  
      
    rect.y += pohyb[1]  
    kolize = test_kolizí(rect,kostky)  
      
    for kostka in kolize:  
        if pohyb[1] > 0:  
            pohyb[1] = 0  
            rect.bottom = kostka.top  
            skok = False  
            typ_kolize['zdola'] = True  
              
        if pohyb[1] < 0:  
            pohyb[1] = 0  
            rect.top = kostka.bottom  
            typ_kolize['zhora'] = True  
              
    if kolize == []:  
        if timer(TPS/20): # po tom co spadnete tak máte 50ms času kde ještě můžete skočit  
            skok = True  
    else:  
        _timer = 0  
          
    return rect, typ_kolize, skok  
  
# ---------------------------------------------------------------------------------------------  
def dekodovat(kodovane):  
    kodovane = kodovane.replace(" ","") # Vymazání případných mezer  
    leveldata = []  
    for cislo in kodovane:  
        cislo = int(cislo) # Konvertování do int  
        leveldata.append(cislo)  
    kostruktovat(leveldata) # Funkce pro vypsání dat do překážek  
  
# ---------------------------------------------------------------------------------------------  
def kostruktovat(leveldata):  
    global překážky, Velikost_čtverce, Max_sloupců, Počet_řad, editor, Upravení_levelu  
    překážky = []  
    nasobitelx, nasobitely = 0, 0  
    for i, Číslo in enumerate(leveldata):  
        nasobitelx += 1  
        if nasobitelx > Max_sloupců - 1: # -1 protože nahoře přidáváme + 1.  
            nasobitelx = 0  
            nasobitely += 1  
        if Číslo != 9:  
            překážka = [(Velikost_čtverce*(nasobitelx - 1), Velikost_čtverce*nasobitely, Velikost_čtverce, Velikost_čtverce), Číslo]  
            překážky.append(překážka)  
              
# ---------------------------------------------------------------------------------------------  
def uložit_level(Číslo_levelu):  
    global překážky, kostka, Max_sloupců, Počet_řad, Velikost_čtverce  
      
    Level = (str(pathlib.Path(__file__).parent.resolve())+"\\Level"+(str(Číslo_levelu + 1))+".txt") # Cesta pro level soubor  
      
    with open(str(Level), 'w') as file: # zapisování do ".txt" protože tam je "with" tak se to pak automaticky zavírá složka.  
      
        ctverec = []  
        for řada in range(Počet_řad - 1):   
            for sloupec in range(Max_sloupců):  
                ctverec.append((int((sloupec) * Velikost_čtverce), int(řada * Velikost_čtverce), 9))  
          
        for číslo in range(len(překážky)):  
            for i in range(len(ctverec)):  
                if ctverec[i][:2] == (překážky[číslo][0][0], překážky[číslo][0][1]):  
                    ctverec[i] = (ctverec[i][0], ctverec[i][1], překážky[číslo][1])  
                      
        for i in range(len(ctverec)):   
            ctverec[i] = ctverec[i][2]  
      
        for row in ctverec:  
            file.write(str(row))  
    return ctverec  
  
# ---------------------------------------------------------------------------------------------  
def Konec_loopu():  
    pygame.display.update()  
    pygame.display.flip()  
    clock = pygame.time.Clock()  
    clock.tick(TPS)  
  
# ---------------------------------------------------------------------------------------------  
def Exit():  
    print("Exit")  
    pygame.quit()  
    sys.exit()  
  
# ---------------------------------------------------------------------------------------------  
def Text_objekty(zpráva, barva, velikost_fontu): # <--  Funkce z našeho minulého projektu  
    Font = pygame.font.Font("freesansbold.ttf", int((Šířka_okna/10)/velikost_fontu))  
    TextPovrch = pygame.font.Font.render(Font ,zpráva, True, barva)  
    return TextPovrch, TextPovrch.get_rect()  
  
# ---------------------------------------------------------------------------------------------  
def Vykreslit_text(zpráva, barva, velikost_fontu, čtverec_x, čtverec_y ):# <--  Funkce z našeho minulého projektu  
    TextPovrch, TextČtverec = Text_objekty(zpráva, barva, velikost_fontu)  
    TextČtverec.center = (Šířka_okna/čtverec_x, Výška_okna/čtverec_y)  
    Okno.blit(TextPovrch, TextČtverec)  
  
# ---------------------------------------------------------------------------------------------  
def Vykreslit_text_do_rect(zpráva, barva, velikost_fontu, Tlačítko):   
    čtverec_x = Tlačítko[0]  
    čtverec_y = Tlačítko[1]  
    TextPovrch, TextČtverec = Text_objekty(zpráva, barva, velikost_fontu)  
    Stín, TextČtverec = Text_objekty(zpráva, Šedá, velikost_fontu)  
    TextČtverec.center = (čtverec_x+(Tlačítko[2]/2), čtverec_y+(Tlačítko[3]/2))  
    Okno.blit(Stín, (TextČtverec[0]+Šířka_okna/160/1.5/velikost_fontu, TextČtverec[1]+Šířka_okna/160/1.5/velikost_fontu))# <-- Vzdálenost stínu od původního textu  
    Okno.blit(TextPovrch, TextČtverec)  
  
# ---------------------------------------------------------------------------------------------  
def Zaoblený_obdelník(Tlačítko, Barva, Barva2):  
    global mx, my, mouseleft, Kliknutí  
  
    obdelník = pygame.Rect(Tlačítko)  
    pygame.draw.rect(Okno,Barva,obdelník)  
      
    pygame.draw.circle(Okno, Barva, (Tlačítko[0]-(Tlačítko[3]/50), Tlačítko[1]+Tlačítko[3]/4), Tlačítko[3]/4)  
    pygame.draw.circle(Okno, Barva, (Tlačítko[0]+Tlačítko[2]+Tlačítko[3]/50, Tlačítko[1]+Tlačítko[3]/4), Tlačítko[3]/4)  
    pygame.draw.circle(Okno, Barva, (Tlačítko[0]+Tlačítko[2]+Tlačítko[3]/50, Tlačítko[1]+Tlačítko[3]/4+Tlačítko[3]-Tlačítko[3]/2), Tlačítko[3]/4)  
    pygame.draw.circle(Okno, Barva, (Tlačítko[0]-(Tlačítko[3]/50), Tlačítko[1]+Tlačítko[3]/4+Tlačítko[3]-Tlačítko[3]/2), Tlačítko[3]/4)  
    ctverecleft = pygame.Rect(Tlačítko[0]-Tlačítko[3]/3.65, Tlačítko[1] + (Tlačítko[3]/4), Tlačítko[3]/2, Tlačítko[3]/2)  
    pygame.draw.rect(Okno, Barva, (ctverecleft))  
    ctverecright = pygame.Rect((Tlačítko[0]+Tlačítko[2]-Tlačítko[3]/4.5) , Tlačítko[1] + (Tlačítko[3]/4), Tlačítko[3]/2, Tlačítko[3]/2)  
    pygame.draw.rect(Okno, Barva, (ctverecright))  
    Kolize_Tlačítko = pygame.Rect(Tlačítko[0] - Tlačítko[3]/3.65 , Tlačítko[1], Tlačítko[2] + (Tlačítko[3]/1.8), Tlačítko[3])  
      
    if Kolize_Tlačítko.collidepoint((mx, my)): # Funkce používá jen obdelníky pro kolize (to znamená, že se dá tlačítko aktivovat i když na něm přesně myší nejsme)  
            pygame.draw.rect(Okno,Barva2,obdelník)  
            pygame.draw.circle(Okno, Barva2, (Tlačítko[0]-(Tlačítko[3]/50), Tlačítko[1]+Tlačítko[3]/4), Tlačítko[3]/4)  
            pygame.draw.circle(Okno, Barva2, (Tlačítko[0]+Tlačítko[2]+Tlačítko[3]/50, Tlačítko[1]+Tlačítko[3]/4), Tlačítko[3]/4)  
            pygame.draw.circle(Okno, Barva2, (Tlačítko[0]+Tlačítko[2]+Tlačítko[3]/50, Tlačítko[1]+Tlačítko[3]/4+Tlačítko[3]-Tlačítko[3]/2), Tlačítko[3]/4)  
            pygame.draw.circle(Okno, Barva2, (Tlačítko[0]-(Tlačítko[3]/50), Tlačítko[1]+Tlačítko[3]/4+Tlačítko[3]-Tlačítko[3]/2), Tlačítko[3]/4)  
            ctverecleft = pygame.Rect(Tlačítko[0]-Tlačítko[3]/3.65, Tlačítko[1] + (Tlačítko[3]/4), Tlačítko[3]/2, Tlačítko[3]/2)  
            pygame.draw.rect(Okno, Barva2, (ctverecleft))  
            ctverecright = pygame.Rect((Tlačítko[0]+Tlačítko[2]-Tlačítko[3]/4.5) , Tlačítko[1] + (Tlačítko[3]/4), Tlačítko[3]/2, Tlačítko[3]/2)  
            pygame.draw.rect(Okno, Barva2, (ctverecright))  
            if mouseleft == True: # Tohle je tady, aby se tlačítko spustilo po tom, co přestaneme držet levé tlačítko myši  
                pygame.draw.rect(Okno,Barva,obdelník)  
                pygame.draw.circle(Okno, Barva, (Tlačítko[0]-(Tlačítko[3]/50), Tlačítko[1]+Tlačítko[3]/4), Tlačítko[3]/4)  
                pygame.draw.circle(Okno, Barva, (Tlačítko[0]+Tlačítko[2]+Tlačítko[3]/50, Tlačítko[1]+Tlačítko[3]/4), Tlačítko[3]/4)  
                pygame.draw.circle(Okno, Barva, (Tlačítko[0]+Tlačítko[2]+Tlačítko[3]/50, Tlačítko[1]+Tlačítko[3]/4+Tlačítko[3]-Tlačítko[3]/2), Tlačítko[3]/4)  
                pygame.draw.circle(Okno, Barva, (Tlačítko[0]-(Tlačítko[3]/50), Tlačítko[1]+Tlačítko[3]/4+Tlačítko[3]-Tlačítko[3]/2), Tlačítko[3]/4)  
                pygame.draw.rect(Okno, Barva, (ctverecleft))  
                pygame.draw.rect(Okno, Barva, (ctverecright))  
                Kliknutí = True  
            if Kliknutí == True:  
                if mouseleft == False:  
                    Kliknutí = False  
                    return True  
                else:  
                    return False  
  
# ---------------------------------------------------------------------------------------------  
def Životy(Hráč_životy):  
    global životy, Obtížnost  
    životy.clear()  
      
    if Obtížnost != 0:  
        if not životy:  
            for i in range(Hráč_životy):  
                životy.append(pygame.Rect(Šířka_okna/2 - Velikost_čtverce/2 + ((Velikost_čtverce+Šířka_okna/800) * i), Výška_okna/15 - Velikost_čtverce/2, Velikost_čtverce, Velikost_čtverce))  
                rozdílx = životy[0][0] - (životy[-1][0]) + Velikost_čtverce  
              
            for život in životy:  
                život[0] -= (abs(int(rozdílx/2)))  
                  
            if Hráč_životy != len(životy):  
                if životy != []:  
                    životy.pop()  
                      
# ---------------------------------------------------------------------------------------------  
def fake_smrt(): # Když se dotknu červené kostky nebo enemáka nebo spadnu z mapy atd...  
    global Obtížnost, Hráč_životy, pohyb, překážky, Respawn_kostka_pozice, Hráč, timer_list, Fake_smrt, scroll_rychlost_dělitel  
    timer_list[3] += 1  
    pohyb = [0, 0]  
    if timer_list[3] >= 50:  
        timer_list[3] = 0 # Resetování časovače  
        scroll_rychlost_dělitel = 1 #aby se teleportovala kamera a hráče  
        if Obtížnost != 0:  
            Hráč_životy -= 1  
        Fake_smrt = False  
        for i in překážky:  
            if i[1] == 7 and Respawn_kostka_pozice != 0:  
                Hráč = teleport(Respawn_kostka_pozice[0][0], Respawn_kostka_pozice[0][1])  
            elif i[1] == 8 and Respawn_kostka_pozice == 0:  
                Hráč = teleport(i[0][0], i[0][1])  
                 
# ---------------------------------------------------------------------------------------------  
def Vymazat_level(Číslo_levelu):  
    global Počet_levelů, Upravení_levelu, výběr_levelu_menu  
    Číslo_levelu += 1  
    Čísla_levelů = []  
    Levely_na_přejmenování = []  
    Čísla_levelů_na_přejmenování = []  
      
    os.chdir(Složka_levely)  
    for soubor in glob.glob("*.txt"):  
        txt = (str(soubor)) # Vezme název souboru  
        souborbeztxt = txt.rsplit(".", 1) # Vše za tečkou "odebere"  
        res = [re.findall(r'(\w+?)(\d+)', souborbeztxt[0])[0]] # https://www.geeksforgeeks.org/python-splitting-text-and-number-in-string :)  
        Čísla_levelů.append(res[0][1])  
          
    for pořadí in Čísla_levelů:   
        if int(pořadí) > Číslo_levelu:  
            Čísla_levelů_na_přejmenování.append(pořadí) # Všechna čísla levelů, které musíme přejmenovat  
            os.chdir(Složka_levely)  
            Level = (str(os.getcwd())+"\\Level"+str(pořadí)+".txt")      
            Levely_na_přejmenování.append(Level)  
              
    os.chdir(Složka_levely) # Asi to tady být nemusí, ale funguje to takže to mazat nebudu :)  
    Cesta_soubor_smazani = (str(os.getcwd())+"\\Level"+str(Číslo_levelu)+".txt")  
    Soubor = open(Cesta_soubor_smazani, "w")  
      
    if (os.path.isfile(Cesta_soubor_smazani)) == True: # Pokud soubor existuje...  
        if Soubor.closed == False:  
            Soubor.close()  
        os.remove(Cesta_soubor_smazani) # Mazání aktivního levelu  
  
    for level in enumerate(Levely_na_přejmenování):  
        os.rename(level[1], str(pathlib.Path(level[1]).resolve().parent) + "\\Level" + str(int(Čísla_levelů_na_přejmenování[level[0]])-1) +".txt") # Přejmenování všech vyšších levelů  
          
    Okno.fill(Bílá)  
    Vykreslit_text_do_rect("Level " + str(Číslo_levelu) +" byl úspěšně smazán, všechny levely s vyšším pořadím byly přejmenovány." , Random_barva, 5, Zpráva)  
      
    Konec_loopu() # aby se obrazovka updatovala před tím než se program zmrazí  
    time.sleep(4) # zmražení programu na x sekund  
          
    výběr_levelu_menu = False  
    Upravení_levelu = True  
  
# Loop ----------------------------------------------------------------------------------------  
while True:  
    # Definování stisknutí ----------------------------------  
    stisknuto = pygame.key.get_pressed()  
    for událost in pygame.event.get():  
            if událost.type == pygame.QUIT: # Ukončení křížkem  
                Exit()  
            if stisknuto[pygame.K_ESCAPE]: # Ukončení escapem  
                Exit()  
      
    # Myš ---------------------------------------------------     
    mx, my = pygame.mouse.get_pos()  # Pozice kurzoru  
    mouseleft, mousemiddle, mouseright = pygame.mouse.get_pressed() # Kliknutí
    
    #LYGMA
    if (stisknuto[pygame.K_r]):
        Real_pause = False  
        hra = True  
        os.chdir(Složka_levely)  
        load = open(str(os.getcwd())+"\\Level"+str(otevřený_level+1)+".txt")  
        leveldata = load.read() # Čtení level souboru a ukládání ho do leveldata  
        dekodovat(leveldata)  
        load.close()  
        Start = time.time()  
        reset_číslo = 0 # LOGIKU PRO RESET SEM <---
        DB_alpha = 0  
        Stop1 = time.time()  
    
  
    # HLAVNÍ MENU ------------------------------------------------------------------------------  
    if hlavnímenu:  
        Okno.fill(Bílá)  
        reset_číslo = 0  
        Respawn_kostka_pozice = 0  
        Vykreslit_text_do_rect("UNTITLED GAME", Random_barva, 1.5, Tabule_level)  
  
        if Zaoblený_obdelník(Play, Černá, Random_barva) == True:  
            hlavnímenu = False  
            Upravení_levelu = True  
        Vykreslit_text_do_rect("Výběr levelu", Bílá, 1.7, Play)  
          
        if Zaoblený_obdelník(Editor, Černá, Random_barva) == True:  
            hlavnímenu = False  
            nastavení = True  
        Vykreslit_text_do_rect("Nastavení", Bílá, 1.7, Editor)  
  
        if Zaoblený_obdelník(Pause_tlačítko_hra, Černá, Random_barva) == True:  
            Nápověda = True  
            hlavnímenu = False  
        Vykreslit_text_do_rect("?", Bílá, 2.5, Pause_tlačítko_hra)  
          
    # NASTAVENÍ -----------------------------------------------------------------------------  
    if nastavení:  
        Okno.fill(Bílá)  
          
        if Zaoblený_obdelník(Zpět_menu, Černá, Random_barva) == True:  
           hlavnímenu = True  
           nastavení = False  
        Vykreslit_text_do_rect("<-", Bílá, 4, Zpět_menu)  
          
        if Zaoblený_obdelník(Play, Černá, Random_barva) == True:  
            Obtížnost_menu = True  
            nastavení = False  
        Vykreslit_text_do_rect("Obtížnost", Bílá, 2, Play)  
          
        Vykreslit_text_do_rect("Nastavení", Černá, 1.5, Tabule_level)  
   # Obtížnost menu -------------------------------------------------------------------------  
    if Obtížnost_menu:  
        Okno.fill(Bílá)  
        Vykreslit_text_do_rect("Obtížnost", Černá, 1.5, Tabule_level)  
          
        if Zaoblený_obdelník(Zpět_menu, Černá, Random_barva) == True: # Tlačítko zpět  
           nastavení = True  
           Obtížnost_menu = False  
        Vykreslit_text_do_rect("<-", Bílá, 4, Zpět_menu)  
          
        if Zaoblený_obdelník(Easy, Černá, Random_barva) == True:  
            Obtížnost = 0  
        Vykreslit_text_do_rect("Lehká", Bílá, 2, Easy)  
  
        if Zaoblený_obdelník(Medium, Černá, Random_barva) == True:  
            Obtížnost = 1      
        Vykreslit_text_do_rect("Střední", Bílá, 2, Medium)  
  
        if Zaoblený_obdelník(Hard, Černá, Random_barva) == True:  
            Obtížnost = 2  
        Vykreslit_text_do_rect("Těžká", Bílá, 2, Hard)  
  
        if Obtížnost == 0:  
            Zaoblený_obdelník(Easy, Zelená, Random_barva)  
            Vykreslit_text_do_rect("Lehká", Bílá, 2, Easy)  
        if Obtížnost == 1:  
            Zaoblený_obdelník(Medium, Oranžová, Random_barva)  
            Vykreslit_text_do_rect("Střední", Bílá, 2, Medium)  
        if Obtížnost == 2:  
            Zaoblený_obdelník(Hard, Červená, Random_barva)  
            Vykreslit_text_do_rect("Těžká", Bílá, 2, Hard)  
  
          
    # HRA -----------------------------------------------------------------------------------  
    if hra:  
        Okno_rect = pygame.Rect(0 + scroll_x, 0 + scroll_y, Šířka_okna, Výška_okna) #definuju kde je "obrazovka"
        Životy(Hráč_životy)  
        Okno.fill(Krémová)
        # Hráč začíná nahoře v pravo --------------------------------------------------------  
        if debounce():
            Kostky_rect_list_enemy = []
            Kostky_rect_list = []
            Fake_smrt = False  
            spustit_jednou = True  
            timer_list[3] = 0  
            Enemy_životy = 1  
            Hráč_životy = 1 # Nekonečno životů (jen pro ez)  
            pohyb = [0, 0]  
            Hráč[0] = 600  
            Hráč[1] = 0  
            scroll_x = 0  
            scroll_y = 0  
            Respawn_kostka_pozice = 0 # resetování checkpointu  
            for i in překážky:  
                if i[1] == 8:  
                    Hráč = teleport(i[0][0], i[0][1])  
                      
            # Nastavení Obtížnosti  
            if Obtížnost == 0: # Easy  
                Hráč_životy = 1  
                max_rychlost_enemy = Šířka_okna/1600  
                Rychlost_enemák = Šířka_okna/1600  
                  
            if Obtížnost == 1: # Medium  
                Hráč_životy = 10  
                max_rychlost_enemy = (Šířka_okna/1600)*2 # Nwm proč ale nefungujou desetiný čísla (protože to je int a ne float ty koště - Jirka)  
                Rychlost_enemák = Šířka_okna/1600  
                  
            if Obtížnost == 2: # Hard  
                Hráč_životy = 4  
                max_rychlost_enemy = (Šířka_okna/1600)*2  
                Rychlost_enemák = (Šířka_okna/1600)*2  
                Enemy_životy = 2  
        max_rychlost = Storage_max_rychlost #aby se resetovala max_rychlost potom co se to změní  
          
        # Real smrt --------------------------------------------------------------------------  
        if Hráč_životy == 0:  
            Real_smrt(Obtížnost)  
            Stop = time.time()  
        # Fake smrt --------------------------------------------------------------------------  
        if Fake_smrt:  
            fake_smrt()  
            timer_list[4] = 0  
            #scroll_rychlost_dělitel  
        if Fake_smrt == False:  
            timer_list[4] += 1  
            if timer_list[4] > 50: #po 50f se resetuje rychlost scrollování  
                scroll_rychlost_dělitel = 10  
   
        # scroll -----------------------------------------------------------------------------  
        scroll_x += (Hráč[0] - scroll_x - (Šířka_okna/2 - Velikost_čtverce/2))/(scroll_rychlost_dělitel*2) # najdu jak je daleku hráč od porostředka obrazovky a pak posouvám obrazovku blíže k hráči  
        scroll_y += (Hráč[1] - scroll_y - (Výška_okna/2 - Velikost_čtverce/2))/scroll_rychlost_dělitel #dělím to 10 aby tam byl trochu lag mezi tím co se posune hráč a obrazovka  
        scroll_x = int(scroll_x) # aby se všechny kostky posouvaly najednou  
        scroll_y = int(scroll_y)  
        #limitování scrollu -----------------------------------------------------------------  
        if Max_sloupců * Velikost_čtverce < Šířka_okna + scroll_x + Velikost_čtverce:  
            scroll_x = Max_sloupců * Velikost_čtverce - Šířka_okna - Velikost_čtverce  
  
        if 0 > scroll_x:  
            scroll_x = 0  
          
        # osa y  
        if scroll_y < 0:  
            scroll_y = 0  
          
        if Počet_řad * Velikost_čtverce < Výška_okna + scroll_y + Velikost_čtverce:  
            zastaveni_scrollu_dolu = True  
            scroll_y = Počet_řad * Velikost_čtverce - Výška_okna - Velikost_čtverce  
              
        # Limitování pádu--------------------------------------------------------------------  
        if Hráč[1] + Výška_hráče > Počet_řad * Velikost_čtverce:  
            Fake_smrt = True  
  
        # Pohyb -----------------------------------------------------------------------------  
        if (stisknuto[pygame.K_RIGHT] and Fake_smrt == False) or (stisknuto[pygame.K_d] and Fake_smrt == False):  
            pohyb[0] += Rychlost_hráče  
            Poslední_zmáčknutá_šipka = "Right"  
              
        if (stisknuto[pygame.K_LEFT] and Fake_smrt == False) or (stisknuto[pygame.K_a] and Fake_smrt == False):  
            pohyb[0] -= Rychlost_hráče  
            Poslední_zmáčknutá_šipka = "Left"  
              
        # Zpomalování ------------------------------------------------------------------------  
        if (stisknuto[pygame.K_LSHIFT] or stisknuto[pygame.K_RSHIFT]) and Fake_smrt == False: #Fake_smrt aby se nemohl hýbat když je mrtvý  
            max_rychlost = Storage_max_rychlost/3  
          
        if (stisknuto[pygame.K_UP] and skok == False and Fake_smrt == False) or (stisknuto[pygame.K_w] and skok == False and Fake_smrt == False):  
            pohyb[1] -= Výška_skoku  
            skok = True  
              
        if pohyb[0] > 0:  
            pohyb[0] -= Rychlost_hráče/2  
          
        if pohyb[0] < 0:  
            pohyb[0] += Rychlost_hráče/2  
          
        if pohyb[0] > max_rychlost:  
            pohyb[0] -= Rychlost_hráče # - rychlost hráče aby se zpomaloval hráč ale nezastavil ihned (není momentum)  
        if pohyb[0] < -max_rychlost:  
            pohyb[0] -= -Rychlost_hráče  

        # Přidání gravitace -----------------------------------------------------------------  
        pohyb[1] += Gravitace    
          
        if spustit_jednou == True:  
            Enemy_kostky = []  
              
        # Kolize ---------------------------------------------------------------------------------   
        změna = False  
        if Respawn_kostka_pozice_1 != Respawn_kostka_pozice:  
            změna = True  
            Respawn_kostka_pozice_1 = Respawn_kostka_pozice  
        Respawn_kostka_pozice_1 = Respawn_kostka_pozice  
  
        for kostka in překážky:  
            # kostka[1] (číslo zmáčknutého tlačítka když je zmáčknuté "r")  
            if kostka[1] == 0 and spustit_jednou: # Klasická kostička  
                Kostky_rect_list.append(pygame.Rect(kostka[0][0], kostka[0][1], kostka[0][2], kostka[0][3])) # tady jsem odebral - scroll protože kalkulujeme kolize podle pozice hráče a pozice hráče je absolutní souřadnice
                Kostky_rect_list_enemy.append(pygame.Rect(kostka[0][0], kostka[0][1], kostka[0][2], kostka[0][3])) 
            if kostka[1] == 4 and spustit_jednou == True:  
                Enemy_kostky.append([kostka[0][0], kostka[0][1], [0, 0], Rychlost_enemák, Enemy_životy]) #přidávání kostek do listu  
            if kostka[1] == 5 and spustit_jednou:  
                Kostky_rect_list_enemy.append(pygame.Rect(kostka[0][0], kostka[0][1], kostka[0][2], kostka[0][3]))  
                      
            if Hráč.colliderect(kostka[0][0], kostka[0][1], kostka[0][2], kostka[0][3]):
                if kostka[1] == 1: # Kill kostička  
                    Fake_smrt = True  
                if kostka[1] == 2: # Booster kostička  
                    max_rychlost = Storage_max_rychlost*5 # aby mohl booster zrychlyt hráče více  
                    pohyb[0] += Rychlost_hráče  
                          
                if kostka[1] == 3: # Elevator kostička  
                    pohyb[1] = -(Rychlost_hráče)*10  
                      
                if kostka[1] == 6: # konec hry kostka  
                    Výhra()  
                    Stop = time.time()  
                if kostka[1] == 7: # Respawn kostička  
                    Respawn_kostka_pozice = kostka  
          
        spustit_jednou = False  
          
        # Logika pro enemy  
        timer_list[2] += 1  
        for cislo, enemy in enumerate(Enemy_kostky):  
            Enemy_kostky[cislo][2][0] += Enemy_kostky[cislo][3] #Enemy_kostky[cislo][2] = pohyb, Enemy_kostky[cislo][3] = enemy_rychlost  
            #Enemy_kostky[cislo][2][1] += 1  
            #Enemy_kostky[cislo][4] = Enemy_životy  
            #pohyb_enemák[1] += Gravitace    # ještě nebudu přídávat gravitaci kvůli skákání  
              
            Enemák = pygame.Rect(Enemy_kostky[cislo][0], Enemy_kostky[cislo][1], Velikost_čtverce, Velikost_čtverce)  
            Enemák, typ_kolize_enemy, Enemy_skok = move(Enemák, Enemy_kostky[cislo][2], Kostky_rect_list_enemy, Enemy_skok) # kolize  
            Enemy_kostky[cislo] = [Enemák[0], Enemák[1], Enemy_kostky[cislo][2], Enemy_kostky[cislo][3], Enemy_kostky[cislo][4]] #kolize  
            if Enemy_kostky[cislo][2][0] == 0: # Enemy_kostky[cislo][2] = pohyb  
                Enemy_kostky[cislo][3] = -Enemy_kostky[cislo][3] # Enemy_kostky[cislo][3] = enemy_rychlost  
              
            # limitování maximální rychlosti enemáka  
            if Enemy_kostky[cislo][2][0] > max_rychlost_enemy: #osa x  
                Enemy_kostky[cislo][2][0] = max_rychlost_enemy  
            if Enemy_kostky[cislo][2][0] < -max_rychlost_enemy/2: #NEVÍM PROČ ALE KDYŽ VYNÁSOBÝM TUHLE HODNOTU -1 TAK TO JE NAJEDNOU ZDVOJNÁSOBENÝ PROOOOČČČČČČČČČ  
                Enemy_kostky[cislo][2][0] = -max_rychlost_enemy/2 #tohle je lazy fix ALE hledám chybu už minimálně 40 minut a nic jsem nenašel a už mě to fakt nebaví  
                  
            if Enemy_kostky[cislo][2][1] >= Šířka_okna/1600: # osa y  
                Enemy_kostky[cislo][2][1] = Šířka_okna/1600  
            if Enemy_kostky[cislo][2][1] <= -(Šířka_okna/1600):  
                Enemy_kostky[cislo][2][1] = -(Šířka_okna/1600)  
              
            if Hráč.colliderect(Enemák) and pohyb[1] <= 40: #smrt  
                Fake_smrt = True  
              
            if Hráč.colliderect(Enemák) and pohyb[1] > 40: # když hráč narazí do enemáka moc rychle za zhora tak umře hráč a né enemák  
                pohyb[1] = 0 # jestli tohle neudělám a jeho y velocita bude dost vysoká tak hráč nevyskočí ale jenom ho to zpomalí  
                pohyb[1] -= Výška_skoku  
                Enemy_kostky[cislo][4] -= 1  
                  
            if Hráč.colliderect(Enemák[0], Enemák[1] - Velikost_čtverce/2, Enemák[2], Enemák[3]/2) and pohyb[1] > 0 and Enemy_kill == False and Fake_smrt == False: # Když skocím na enemáka: # Velikost_čtverce/5 = hitbox nad enemákama  
                pohyb[1] = 0 # jestli tohle neudělám a jeho y velocita bude dost vysoká tak hráč nevyskočí ale jenom ho to zpomalí  
                pohyb[1] -= Výška_skoku  
                Enemy_kostky[cislo][4] -= 1  
                Enemy_kill = True  
            else:  
                Enemy_kill = False #tohle jsem udělal dopředu protože bude přidávat životy  
                  
            # Animace  
            if int(Enemy_kostky[cislo][2][0]) > 0:  
                if timer_list[2] >= 0 and timer_list[2] <= 30:  
                    Okno.blit(enemy_run_0, (Enemák[0] - scroll_x, Enemák[1] - scroll_y, Enemák[2], Enemák[3]))  
                if timer_list[2] >= 30 and timer_list[2] <= 60:  
                    Okno.blit(enemy_run_1, (Enemák[0] - scroll_x, Enemák[1] - scroll_y, Enemák[2], Enemák[3]))  
              
            if int(Enemy_kostky[cislo][2][0]) <= 0:  
                if timer_list[2] >= 0 and timer_list[2] <= 30:  
                    Okno.blit(pygame.transform.flip(enemy_run_0, True, False) , (Enemák[0] - scroll_x, Enemák[1] - scroll_y, Enemák[2], Enemák[3]))  
                if timer_list[2] >= 30 and timer_list[2] <= 60:  
                    Okno.blit(pygame.transform.flip(enemy_run_1, True, False) , (Enemák[0] - scroll_x, Enemák[1] - scroll_y, Enemák[2], Enemák[3]))  
                      
            if Enemy_kostky[cislo][4] <= 0: # Když enemák nemá životy odeber ho z existence :)  
                Enemy_kostky.remove(Enemy_kostky[cislo]) # tohle by mělo být poslední protože tohle odebere enemáka z listu a pak budou "out of range" errory  
            # konec for loopu (logika pro enemáky)  
              
        if timer_list[2] >= 60: # resetováni timeru  
            timer_list[2] = 0  
  
            #Debug Hitbox kde umře enemák když se ho dotknete  
            #pygame.draw.rect(Okno, (Zelená), (Enemák[0] - scroll_x, Enemák[1] - Velikost_čtverce/2 - scroll_y, Enemák[2], Enemák[3]/2))  
              
        # VYKRESLOVÁNÍ ----------------------------------------------------------------------------  
        timer_list[1] += 1  
        for kostka in překážky:  
            if Okno_rect.colliderect(kostka[0]): #když je kostka na obrazovce tak:  
                if kostka[1] == 0:  
                    Okno.blit(brick, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                if kostka[1] == 1:  
                    Okno.blit(kill_kostka, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                if kostka[1] == 2:  
                    Okno.blit(booster_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                if kostka[1] == 3:  
                    Okno.blit(elevator_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                #if kostka[1] == 4: #enemy  
                #    pass # vykreslování pro enemy je napsáno pod tímhle  
                if kostka[1] == 5: # secret kostka (nemá kolize)  
                    if Hráč.colliderect(pygame.Rect(kostka[0])): 
                        Kostky_rect_list_enemy = [] # mazání listu pro enemy 
                        překážky.remove(kostka) 
                        for block in překážky: # resetování listu pro enemy 
                            if block[1] == 5 or block[1] == 0: 
                                Kostky_rect_list_enemy.append(pygame.Rect(block[0][0], block[0][1], block[0][2], block[0][3])) 
                    Okno.blit(secret, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                if kostka[1] == 6: # konec kostka  
                    if timer_list[1] >= 0 and timer_list[1] <= 60: # TPS * 1 = 1s  
                        Okno.blit(finish_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                    if timer_list[1] >= 61 and timer_list[1] <= 120:  
                        Okno.blit(finish_1, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                          
                if kostka[1] == 7: # Checkpoint kostička  
                    if Respawn_kostka_pozice == 0 and timer_list[0] == 0:  
                        Okno.blit(checkpoint_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                    if Respawn_kostka_pozice != 0:  
                        if (pygame.Rect(kostka[0])).colliderect(pygame.Rect(Respawn_kostka_pozice[0][0], Respawn_kostka_pozice[0][1], Respawn_kostka_pozice[0][2], Respawn_kostka_pozice[0][3])) and timer_list[0] >= 150: # idle  
                            if timer_list[1] >= 0 and timer_list[1] <= 60: # TPS * 1 = 1s  
                                Okno.blit(chechpoint_idle_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                            if timer_list[1] >= 61 and timer_list[1] <= 120:  
                                Okno.blit(chechpoint_idle_1, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                        elif not (pygame.Rect(kostka[0])).colliderect(pygame.Rect(Respawn_kostka_pozice[0][0], Respawn_kostka_pozice[0][1], Respawn_kostka_pozice[0][2], Respawn_kostka_pozice[0][3])):  
                            Okno.blit(checkpoint_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
  
                if Respawn_kostka_pozice != 0 and(pygame.Rect(kostka[0])).colliderect(pygame.Rect(Respawn_kostka_pozice[0][0], Respawn_kostka_pozice[0][1], Respawn_kostka_pozice[0][2], Respawn_kostka_pozice[0][3])) and timer_list[0] <= 150:  
                    timer_list[0] += 1/len(kostka)  
                    if timer_list[0] > 0 and timer_list[0] <= 30:  
                        Okno.blit(checkpoint_1, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                    if timer_list[0] >= 30 and timer_list[0] <= 60:  
                        Okno.blit(checkpoint_2, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                    if timer_list[0] >= 60 and timer_list[0] <= 90:  
                        Okno.blit(checkpoint_3, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                    if timer_list[0] >= 90 and timer_list[0] <= 120:  
                        Okno.blit(checkpoint_4, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                    if timer_list[0] >= 120 and timer_list[0] <= 150:  
                        Okno.blit(checkpoint_5, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
              
            if kostka[1] == 8: # spawn kostka  
                if timer_list[1] >= 0 and timer_list[1] <= 60: # TPS * 1 = 1s  
                    Okno.blit(spawn_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                if timer_list[1] >= 61 and timer_list[1] <= 120:  
                    Okno.blit(spawn_1, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                if timer_list[1] >= 120:  
                    timer_list[1] = 0  
                  
        for život in životy: # Vykreslování životů  
            Okno.blit(heart, (život))  
          
        if změna == True:  
            timer_list[0] = 0  
              
        if Zaoblený_obdelník(Pause_tlačítko_hra, Bílá, Random_barva) == True or (stisknuto[pygame.K_p] and Pausnuto == False): # PAUSE TLAČÍTKO  
            hra = False  
            Real_pause = True  
            Start1 = time.time()  
            Pausnuto = True # aby se nepřepínalo mezi Real_pause a hra každý frame když držíme "p"  
        if not stisknuto[pygame.K_p]:  
            Pausnuto = False  
              
        Vykreslit_text_do_rect("||", Černá, 3, Pause_tlačítko_hra) # PAUSE TLAČÍTKO  
               
        Hráč, typ_kolize, skok = move(Hráč,pohyb, Kostky_rect_list, skok) # Pohyb?  
          
        #pygame.draw.rect(Okno,(255,255,255),(Hráč[0] - scroll_x, Hráč[1] - scroll_y, Hráč[2], Hráč[3]))  # hitbox hráče  
          
        # Animace hráče -------------------------------------------------------------------------------  
        animace_pohyb = [int(pohyb[0]), int(pohyb[1])] # tohle dělám protože i když hráč je na místě tak pohyb[0] != 0 ale nějákému desetinému císlu.  
          
        if Fake_smrt == False: # když hráč není mrtvý  
            # Pohyb pravo  
            if animace_pohyb[0] > 0 and skok == False: # if do prava  
                animation_timer_idle = 0 #resetuju timer  
                if animation_timer < 0: # aby nezmizel hráč  
                    animation_timer = 0  
                      
                animation_timer += 1  
                if animation_timer >=1 and animation_timer <= 15:  
                    Okno.blit(run_0 , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3])) # Vykreslení hráče  
                if animation_timer >= 16 and animation_timer <= 31:  
                    Okno.blit(run_1 , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3])) # Vykreslení hráče  
                if animation_timer == 31:# resetuju timer  
                    animation_timer = 0  
                  
            # Pohyb vlevo  
            if animace_pohyb[0] < 0 and skok == False: # if do leva  
                animation_timer_idle = 0 #resetuju timer  
                if animation_timer > 0: # aby nezmizel hráč  
                    animation_timer = 0  
                      
                animation_timer -= 1  
                if animation_timer <=-1 and animation_timer >= -15:  
                    Okno.blit(pygame.transform.flip(run_0, True, False) , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3])) #Otáčení hráče  
                if animation_timer <= -16 and animation_timer >= -31:  
                    Okno.blit(pygame.transform.flip(run_1, True, False) , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3])) #Otáčení hráče  
                if animation_timer == -31:# resetuju timer  
                    animation_timer = 0  
              
            # Skok  
            if (skok == True and animace_pohyb[1] <= 0) or animace_pohyb[1] < 0: # "<=" protože když vyskočí a nehejbe se aby se vykreslil skok a né idle # tohle tady musí být 2x protože v amplitůdě skoku se nevykresloval 
                if Poslední_zmáčknutá_šipka == "Right":  
                    Okno.blit(jump_0 , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3]))  
                if Poslední_zmáčknutá_šipka == "Left":  
                    Okno.blit(pygame.transform.flip(jump_0, True, False) , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3])) 
 
            # Idle  
            elif animace_pohyb[0] == 0 and animace_pohyb[1] == 0:# if idle  
                animation_timer_idle += 1  
                if animation_timer_idle >= 1 and animation_timer_idle <= 60:  
                    if Poslední_zmáčknutá_šipka == "Right": # aby se otočil správně podle toho co zmáčknete  
                        Okno.blit(idle_0 , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3])) # Vykreslení hráče  
                    if Poslední_zmáčknutá_šipka == "Left":  
                        Okno.blit(pygame.transform.flip(idle_0, True, False) , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3]))  
                if animation_timer_idle >= 61 and animation_timer_idle <= 120:  
                    if Poslední_zmáčknutá_šipka == "Right":  
                        Okno.blit(idle_1 , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3])) # Vykreslení hráče  
                    if Poslední_zmáčknutá_šipka == "Left":  
                        Okno.blit(pygame.transform.flip(idle_1, True, False) , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3]))  
                      
                if animation_timer_idle == 120: # resetuju timer  
                    animation_timer_idle = 0  
  
            # Fall  
            if animace_pohyb[1] > 0:  
                if Poslední_zmáčknutá_šipka == "Right":  
                    Okno.blit(fall_0 , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3]))  
                if Poslední_zmáčknutá_šipka == "Left":  
                    Okno.blit(pygame.transform.flip(fall_0, True, False) , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3]))  
        if Fake_smrt: # když hráč je mrtvý  
            if Poslední_zmáčknutá_šipka == "Right":  
                Okno.blit(death_0 , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3]))  
            if Poslední_zmáčknutá_šipka == "Left":  
                Okno.blit(pygame.transform.flip(death_0, True, False) , (Hráč[0] - dx - scroll_x, Hráč[1] - dy - scroll_y, Hráč[2], Hráč[3]))  
    # Výběr levelu menu ---------------------------------------------------------------------------  
    if výběr_levelu_menu:  
        Okno.fill(Bílá)  
        reset_číslo = 0 # Aby debounce funkce fungovala   
        spustit_jednou = True   
        Respawn_kostka_pozice = 0   
        životy.clear()  
          
        if Zaoblený_obdelník(Zpět_menu, Černá, Random_barva) == True:  
            výběr_levelu_menu = False  
            hlavnímenu = True  
        Vykreslit_text_do_rect("<-", Bílá, 4, Zpět_menu)  
          
        if Zaoblený_obdelník(Hrát_level, Černá, Random_barva) == True: # HRANÍ LEVELU  
            os.chdir(Složka_levely)  
            load = open(str(os.getcwd())+"\\Level"+str(otevřený_level+1)+".txt")  
            leveldata = load.read() # Čtení level souboru a ukládání ho do leveldata  
            dekodovat(leveldata)  
            load.close()  
            Start = time.time()  
            výběr_levelu_menu = False  
            hra = True  
        Vykreslit_text_do_rect("Hrát level", Bílá, 2.2, Hrát_level)  
          
        if int(otevřený_level) not in range(0,8): # Aby levely 1-8 (default levely) nešli upravit  
            if Zaoblený_obdelník(Upravit_level, Černá, Random_barva) == True: # ÚPRAVA LEVELU  
                os.chdir(Složka_levely)  
                load = open(str(os.getcwd())+"\\Level"+str(otevřený_level+1)+".txt")  
                leveldata = load.read() # Čtení level souboru a ukládání ho do leveldata  
                dekodovat(leveldata)  
                load.close()  
                výběr_levelu_menu = False  
                editor = True  
            Vykreslit_text_do_rect("Upravit level", Bílá, 2.2, Upravit_level)  
  
        if int(otevřený_level) not in range(0,8): # Aby levely 1-8 nešli smazat  
            if Zaoblený_obdelník(Smazat_level, Černá, Random_barva) == True: # SMAZÁNÍ LEVELU  
                Vymazat_level(otevřený_level)  
            Vykreslit_text_do_rect("Smazat level", Bílá, 2.2, Smazat_level)  
          
        Vykreslit_text_do_rect("Level "+str(otevřený_level+1), Černá, 2.2, Tabule_level) # Název levelu se kterým momentálně pracujeme  
          
    # TVORBA LEVELU --------------------------------------------------------------------------------       
    if Vytvoření_levelu:  
        Okno.fill(Bílá)  
        reset_číslo = 0 # Aby debounce funkce fungovala  
        spustit_jednou = True  
        Respawn_kostka_pozice = 0  
          
        Vykreslit_text_do_rect("Level " + str(vytvořit_level()) + " byl úspěšně vytvořen.", Random_barva, 3, Zpráva)  
          
        vytvořit_tlačítka_úprav_levelů()  
          
        Konec_loopu() # aby se obrazovka updatovala před tím než se program zmrazí  
        time.sleep(1.5) # zmražení programu na x sekund  
        Vytvoření_levelu = False  
        Upravení_levelu = True  
          
    # ÚPRAVA LEVELU --------------------------------------------------------------------------------  
    if Upravení_levelu:  
        Okno.fill(Bílá)  
        if debounce():  
            vytvořit_tlačítka_úprav_levelů()  
          
        for i in range(len(Úprava_levelu_tlačítka)-1):  
            if i in range(0,2):  
                Barva = Zelená  
            elif i in range(2,4):  
                Barva = Oranžová  
            elif i in range(4,6):  
                Barva = Červená  
            elif i in range(6,8):  
                Barva = Fialová  
            else:  
                Barva = Černá  
  
            if Zaoblený_obdelník(Úprava_levelu_tlačítka[i], Barva, Random_barva) == True:  
                otevřený_level = i # můj nápad je že když vím jakej je otevřenej level tak pak když se ukládá level tak vím jakej level uložit  
                Upravení_levelu = False  
                výběr_levelu_menu = True  
            Vykreslit_text_do_rect(Soubory[i], Bílá, 3, Úprava_levelu_tlačítka[i])  
  
        if Zaoblený_obdelník(Zpět_menu, Černá, Random_barva) == True: # Vracení se do menu  
            hlavnímenu = True  
            Upravení_levelu = False    
        Vykreslit_text_do_rect("<-", Bílá, 4, Zpět_menu)  
          
        Vykreslit_text_do_rect("Vyber level", Černá, 2.2, Tabule_level) # Text  
          
        for i in range(len(Úprava_levelu_tlačítka)):  
            if Zaoblený_obdelník(Úprava_levelu_tlačítka[-1], Černá, Random_barva): # Tlačítko na tvorbu levelů!!!  
                    Vytvoření_levelu = True  
                    výběr_levelu_menu = False  
                    reset_číslo = 0 #aby debounce funkce fungovala  
                    Respawn_kostka_pozice = 0  
                    spustit_jednou = True  
            Vykreslit_text_do_rect("Vytvořit level", Bílá, 3, Úprava_levelu_tlačítka[-1])  
          
    # EDITOR ---------------------------------------------------------------------------------------  
    if editor:  
        Okno.fill(Hnědá)  
        if debounce(): # Aby se vždy začínalo nahoře v pravo.  
            scroll_x = 0  
            scroll_y = Výška_okna  
          
        draw() # Vykreslení gridu!  
          
        mx += scroll_x  
        my += scroll_y  
  
        if stisknuto[pygame.K_LSHIFT] or stisknuto[pygame.K_RSHIFT]:  
            scroll_rychlost = ((Šířka_okna/TPS))*4  
        else:  
            scroll_rychlost = ((Šířka_okna/TPS))  
  
        # Scrollování ------------------------------------------------------------------------------  
        if stisknuto[pygame.K_LEFT] and zastaveni_scrollu_vpravo == False:    
            scroll_x -= scroll_rychlost  
        if stisknuto[pygame.K_RIGHT] and zastaveni_scrollu_vlevo == False:  
            scroll_x += scroll_rychlost  
        if stisknuto[pygame.K_UP] and zastaveni_scrollu_nahoru == False:  
            scroll_y -= scroll_rychlost  
        if stisknuto[pygame.K_DOWN] and zastaveni_scrollu_dolu == False:  
            scroll_y += scroll_rychlost  
          
        # Limitování scrollu -----------------------------------------------------------------------  
        # Na ose x  
        if Max_sloupců * Velikost_čtverce < Šířka_okna + scroll_x + Velikost_čtverce:  
            zastaveni_scrollu_vlevo = True  
            scroll_x = Max_sloupců * Velikost_čtverce - Šířka_okna - Velikost_čtverce  
        else:  
            zastaveni_scrollu_vlevo = False  
        if 0 > scroll_x:  
            zastaveni_scrollu_vpravo = True  
            scroll_x = 0  
        else:  
            zastaveni_scrollu_vpravo = False  
          
        # Na ose y  
        if 0 > scroll_y:  
            zastaveni_scrollu_nahoru = True  
            scroll_y = 0  
        else:  
            zastaveni_scrollu_nahoru = False  
          
        if Počet_řad * Velikost_čtverce < Výška_okna + scroll_y + Velikost_čtverce:  
            zastaveni_scrollu_dolu = True  
            scroll_y = Počet_řad * Velikost_čtverce - Výška_okna - Velikost_čtverce  
        else:  
            zastaveni_scrollu_dolu = False  
        # oprava scrollu ---------------------------------------------------------------------------  
        scroll_x = int(scroll_x) # aby se všechny kostky posouvaly najednou  
        scroll_y = int(scroll_y)  
        # GRID --------------------------------------------------------------------------------------  
        for řada in range(Počet_řad):  
            if my <= řada * Velikost_čtverce and my >= (řada * Velikost_čtverce) - Velikost_čtverce:  
                Aktuální_řada = řada  
                  
        for sloupec in range(Max_sloupců):  
            kostka = [0, Počet_tlačítek]  
            kostka[0] = pygame.Rect((sloupec * Velikost_čtverce) - Velikost_čtverce, (Aktuální_řada * Velikost_čtverce) - Velikost_čtverce, Velikost_čtverce, Velikost_čtverce)  
              
            # Pokládání kostek ----------------------------------------------------------------------  
            if mx > 0 and mx < Šířka_okna + scroll_x and Editor_menu_zapnuto == False and not (pygame.Rect(Uložit_tlačítko[0] - Uložit_tlačítko[3]/3 + scroll_x, Uložit_tlačítko[1] + scroll_y, Uložit_tlačítko[2] + (Uložit_tlačítko[3]/3)*2, Uložit_tlačítko[3])).collidepoint((mx, my)) and not (pygame.Rect(Zpět_menu[0] - Zpět_menu[3]/3 + scroll_x, Zpět_menu[1] + scroll_y, Zpět_menu[2] + (Zpět_menu[3]/3)*2, Zpět_menu[3])).collidepoint((mx, my)):  
                if kostka[0].collidepoint((mx, my)) and mouseleft == True and kostka not in překážky:  
                    překážky.append(kostka)  
                      
                # Odstranění kostek pomocí "mouseright" ----------------------------------------------  
                if kostka[0].collidepoint((mx, my)) and kostka in překážky and mouseright == True:  
                    překážky.remove(kostka)  
                # Zvýraznění kurzoru v editoru  
                if kostka[0].collidepoint((mx, my)):  
                    pygame.draw.rect(Okno, Bílá, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                    
        # VYKRESLENÍ POLOŽENÝCH KOSTEK ----------------------------------  
        Spawner_kostka_položena = 0  
        for kostka in překážky:  
            if kostka[1] == 0:  
                Okno.blit(brick, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
            if kostka[1] == 1:  
                Okno.blit(kill_kostka, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
            if kostka[1] == 2:  
                Okno.blit(booster_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
            if kostka[1] == 3:  
                Okno.blit(elevator_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
            if kostka[1] == 4:  
                Okno.blit(enemy_run_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
            if kostka[1] == 5:  
                Okno.blit(secret, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
            if kostka[1] == 6:  
                Okno.blit(finish_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
            if kostka[1] == 7:  
                Okno.blit(chechpoint_idle_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
            if kostka[1] == 8:  
                Okno.blit(spawn_0, (kostka[0][0] - scroll_x, kostka[0][1] - scroll_y, kostka[0][2], kostka[0][3]))  
                Spawner_kostka_položena += 1  
              
        for kostka in překážky:  
            if Spawner_kostka_položena >= 2:  
                if kostka[1] == 8:  
                    překážky.remove(kostka)  
          
        # VYKRESLENÍ TLAČÍTEK--------------------------------------------  
        mx -= scroll_x # Nulování scrollu, aby se daly používat tlačítka kdekoliv (já vim že to není potřeba ale připadalo mi to vhodné pro tohle udělat svojí vlastní sekci)  
        my -= scroll_y # Nulování scrollu (y)  
  
        if Zaoblený_obdelník(Zpět_menu, Černá, Random_barva) == True:  
            výběr_levelu_menu = False  
            hlavnímenu = True  
            editor = False  
  
        Vykreslit_text_do_rect("<-", Bílá, 4, Zpět_menu)  
          
        # Vykreslování tabulky s kostičkami -------------------------------  
        if stisknuto[pygame.K_r]:  
            Okno.blit(výběr_povrch, (Šířka_okna/2 - Šířka_okna/5, Výška_okna/2 - Výška_okna/3))  
            Vykreslit_text_do_rect("Vyber si kostku", Bílá, 3, (Editor_menu[0], Editor_menu[1] - Editor_menu[3]/1.85, Editor_menu[2], Editor_menu[3]))  
            Editor_menu_zapnuto = True  
              
            for tlačítko in Editor_menu_tlacitka:    
                pygame.draw.rect(Okno, Bílá, pygame.Rect(tlačítko))   
                  
            for Stisknuté_tlačítko, tlačítko in enumerate(Editor_menu_tlacitka):  
                if Zaoblený_obdelník(tlačítko, Bílá, Random_barva) == True:  
                    Počet_tlačítek = Stisknuté_tlačítko  
  
                # Vykreslování textu do tlačítek v menu, kde se vybírá kostička  
                if Stisknuté_tlačítko == 0:  
                    Vykreslit_text_do_rect("Klasická", Černá, 5, tlačítko)  
                if Stisknuté_tlačítko == 1:  
                    Vykreslit_text_do_rect("Zabíjecí", Černá, 5, tlačítko)  
                if Stisknuté_tlačítko == 2:  
                    Vykreslit_text_do_rect("Booster", Černá, 5, tlačítko)  
                if Stisknuté_tlačítko == 3:  
                    Vykreslit_text_do_rect("Elevator", Černá, 5, tlačítko)  
                if Stisknuté_tlačítko == 4:  
                    Vykreslit_text_do_rect("Enemák", Černá, 5, tlačítko)  
                if Stisknuté_tlačítko == 5:  
                    Vykreslit_text_do_rect("Secret", Černá, 5, tlačítko)  
                if Stisknuté_tlačítko == 6:    
                    Vykreslit_text_do_rect("Konec", Černá, 5, tlačítko)  
                if Stisknuté_tlačítko == 7:  
                    Vykreslit_text_do_rect("Checkpoint", Černá, 7, tlačítko)  
                if Stisknuté_tlačítko == 8:  
                    Vykreslit_text_do_rect("Spawn", Černá, 5, tlačítko)  
                      
        if not stisknuto[pygame.K_r]:  
            Editor_menu_zapnuto = False  
              
        # Slidery ------------------------------------------------------------------  
        slider_x = scroll_x/8.34375 - Šířka_tlačítka/4  
        slider_y = scroll_y*1.63 - Šířka_tlačítka/20  
          
        Slider_x = pygame.Rect(slider_x, Výška_okna-Výška_tlačítka/20, Šířka_tlačítka/2, Výška_tlačítka/10)  
        Slider_y = pygame.Rect(-Šířka_tlačítka/4, slider_y, Výška_tlačítka/1.05, Šířka_tlačítka/2)  
          
        pygame.draw.rect(Okno, Bílá, Slider_x)  
        pygame.draw.rect(Okno, Bílá, Slider_y)  
          
        # Ukládání levelů -----------------------------------------------------------          
        if Zaoblený_obdelník(Uložit_tlačítko, Krémová, Zelená) == True:  
            ctverec = uložit_level(otevřený_level) # + 1 protože python počítá od 0 ale my počítáme od 1  
              
        Vykreslit_text_do_rect("Uložit level", Černá, 4, Uložit_tlačítko)  
          
        # Scroll -----------------------------------------------------------          
        mx += scroll_x # Konec nulování scrollu (x)  
        my += scroll_y # konec nulování scrollu (y)  
          
# ----------------------------------------------------------------------  
    if Pause: # VÝHRA  
        if DB_alpha == 0:  
            Okno.blit(pause_povrch, (Šířka_okna/2 - Šířka_okna/4, Výška_okna/2 - Výška_okna/4))  
        DB_alpha += 1  
        pygame.draw.rect(Okno, Random_barva, (Pause_label))  
        Vykreslit_text_do_rect("Výhra", Bílá, 2, Pause_label)  
          
        if Zaoblený_obdelník(Zpět, Bílá, Random_barva) == True: # ZPĚT DO MENU  
            hra = False  
            hlavnímenu = True  
            Pause = False  
            DB_alpha = 0  
        Vykreslit_text_do_rect("Zpět do menu", Černá, 4.4, Zpět)  
          
        if Zaoblený_obdelník(Reset, Bílá, Random_barva) == True: # RESET  
            os.chdir(Složka_levely)  
            load = open(str(os.getcwd())+"\\Level"+str(otevřený_level+1)+".txt")  
            leveldata = load.read() # Čtení level souboru a ukládání ho do leveldata  
            dekodovat(leveldata)  
            load.close()  
            Start = time.time()  
            reset_číslo = 0 # LOGIKU PRO RESET SEM <--- (jen potřebuju aby se level spustil znovu s plnýma životama, všema enemákama a secretama....)  
            hra = True  
            Pause = False  
            Start, Start1, Stop, Stop1 = time.time(), time.time(), time.time(), time.time();  
            DB_alpha = 0  
        Vykreslit_text_do_rect("Hrát znovu", Černá, 4.2, Reset)  
          
        Vykreslit_text_do_rect("Level ti trval " + str(Čas(Stop - Start)), Bílá, 3.5, Timer_lavel)  
# ----------------------------------------------------------------------  
    if Death: # PROHRA  
        if DB_alpha == 0:  
            Okno.blit(pause_povrch, (Šířka_okna/2 - Šířka_okna/4, Výška_okna/2 - Výška_okna/4))  
  
        DB_alpha += 1  
        pygame.draw.rect(Okno, Random_barva, (Pause_label))  
        Vykreslit_text_do_rect("Porážka", Bílá, 2, Pause_label)  
          
        if Zaoblený_obdelník(Zpět, Bílá, Random_barva) == True: # ZPĚT DO MENU  
            hra = False  
            hlavnímenu = True  
            Death = False  
            DB_alpha = 0  
        Vykreslit_text_do_rect("Zpět do menu", Černá, 4.4, Zpět)  
          
        if Zaoblený_obdelník(Reset, Bílá, Random_barva) == True: # RESET  
            os.chdir(Složka_levely)  
            load = open(str(os.getcwd())+"\\Level"+str(otevřený_level+1)+".txt")  
            leveldata = load.read() # Čtení level souboru a ukládání ho do leveldata  
            dekodovat(leveldata)  
            load.close()  
            Start = time.time()  
            reset_číslo = 0 # LOGIKU PRO RESET SEM <---  
            Death = False  
            hra = True  
            DB_alpha = 0  
        Vykreslit_text_do_rect("Hrát znovu", Černá, 4.2, Reset)  
          
        Vykreslit_text_do_rect(Death_msg, Bílá, 3.5, Timer_lavel)  
          
# ----------------------------------------------------------------------  
    if Real_pause: # PAUZA  
        if DB_alpha == 0:  
            Okno.blit(pause_povrch, (Šířka_okna/2 - Šířka_okna/4, Výška_okna/2 - Výška_okna/4))  
        DB_alpha += 1  
        pygame.draw.rect(Okno, Random_barva, (Pause_label))  
        Vykreslit_text_do_rect("Pauza", Bílá, 2, Pause_label)  
          
        if Zaoblený_obdelník(Zpět_hra, Bílá, Random_barva) == True or (stisknuto[pygame.K_p] and Pausnuto == False): # ZPĚT DO HRY   
            hra = True  
            Real_pause = False  
            DB_alpha = 0  
            Pausnuto = True  
            Stop1 = time.time()  
        Vykreslit_text_do_rect("Zpět do hry", Černá, 3.5, Zpět_hra)  
          
        if not stisknuto[pygame.K_p]: # resetuje pause  
            Pausnuto = False  
          
        if Zaoblený_obdelník(Zpět, Bílá, Random_barva) == True: # ZPĚT DO MENU  
            hra = False  
            hlavnímenu = True  
            Real_pause = False  
            DB_alpha = 0  
            Stop1 = time.time()  
        Vykreslit_text_do_rect("Zpět do menu", Černá, 4.4, Zpět)  
          
        if Zaoblený_obdelník(Reset, Bílá, Random_barva) == True: # RESET  
            Real_pause = False  
            hra = True  
            os.chdir(Složka_levely)  
            load = open(str(os.getcwd())+"\\Level"+str(otevřený_level+1)+".txt")  
            leveldata = load.read() # Čtení level souboru a ukládání ho do leveldata  
            dekodovat(leveldata)  
            load.close()  
            Start = time.time()  
            reset_číslo = 0 # LOGIKU PRO RESET SEM <---
            DB_alpha = 0  
            Stop1 = time.time()  
        Vykreslit_text_do_rect("Hrát znovu", Černá, 4.2, Reset)  
  
    if Nápověda:  
        Okno.fill(Bílá)  
        Vykreslit_text_do_rect("Nápověda", Černá, 1.5, Tabule_level)  
        Vykreslit_text("OBECNÉ", Černá, 4, 2, 5) # Podnadpis  
        Vykreslit_text("- Zvolte si level kliknutím na: výběr levelu", Černá, 5, 2, 4)  
        Vykreslit_text("- V nastavení najdete obtížnost", Černá, 5, 2, 3.3)  
        Vykreslit_text("HRA", Černá, 4, 2, 2.6) # Podnadpis  
        Vykreslit_text("- Ve hře se dá zpomalit shiftem", Černá, 5, 2, 2.35)  
        Vykreslit_text("- Enemáci se dají zabít skočením na jejich hlavu (podle obtížnosti jednou nebo dvakrát)", Černá, 5, 2, 2.1)  
        Vykreslit_text("- Zelená vlajka je váš cíl, modré vlajky jsou vaše checkpointy", Černá, 5, 2, 1.9)  
        Vykreslit_text("- Ve hře jsou různé secrety :)", Černá, 5, 2, 1.73)  
        Vykreslit_text("EDITOR", Černá, 4, 2, 1.5) # Podnadpis  
        Vykreslit_text("- V editoru se dá sprintovat shiftem", Černá, 5, 2, 1.4)  
        Vykreslit_text("- Kostky si můžete vybírat podržením klávesy R", Černá, 5, 2, 1.31)  
        Vykreslit_text("- Kostky se dají pokládat levým tlačítkem myši a mazat pravým tlačítkem myši", Černá, 5, 2, 1.23)  
        Vykreslit_text("Pokud vám nejdou ukládat levely, zkuste hru otevřít v Thonnym", Černá, 4.5, 2, 1.1)  
        Vykreslit_text("Pokud i to nejde tak si level asi neuložíte :(", Černá, 8, 2, 1.05)  
  
        if Zaoblený_obdelník(Zpět_menu, Černá, Random_barva) == True:  
            Nápověda = False  
            hlavnímenu = True  
        Vykreslit_text_do_rect("<-", Bílá, 4, Zpět_menu)  
          
    Konec_loopu()