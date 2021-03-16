#coding:utf-8
# Importations
from tkinter import*
from random import *
from tkinter import ttk
from time import sleep

# Constantes du monde 
T_CASE = 20
NB_COL = 15
NB_LIG = 15
BG_COLOR='black'
SERPENTTETE_COLOR = 'red'
SERPENT_COLOR = 'green'
FPS = 500
NORD, EST, SUD, OUEST = 0, 1, 2, 3
BORDER = 50
WIDTH = 400
HEIGHT = 400
score = 0

# variables globales serpent
global snake, MARGGE,pomme,rayon, snake

#
dir = [NORD, EST, SUD, OUEST]
direction = choice(dir)
MARGE = 50
rayon = 10
snake = [(114,1), (99,2), (98,3), (97,4)]
#

pomme = (randrange(50,350,20),randrange(50,350,20))
run = False

# variables globales interface
fenApp = Tk()
fenApp.config(bg='black')
#fenApp.geometry('500x500')

canvas = Canvas(fenApp, width=WIDTH,height=HEIGHT,bg='gray')
canvas.place(x=0,y=0)
canvas.grid(row=1,column=1,columnspan=3)

# Fonctions coordonnées grille et direction (num_case = num_lig * nb_col + num_col)
def case_to_lc(num_case):
    return num_case // NB_COL , num_case%NB_COL


def lc_to_case(num_lig, num_col):
    num_case = num_lig * NB_COL + num_col
    return num_case

def case_to_xy(num_case):
    a, b = case_to_lc(num_case)
    return lc_to_xy(a, b)

def xy_to_lc(x, y):
    return (x-NB_COL)//T_CASE, (y-NB_LIG)//T_CASE

def lc_to_xy(num_lig, num_col):
    return MARGE + num_col*20, MARGE + num_lig*20

def xy_to_case(x, y):
    a, b = xy_to_lc(x, y)
    return lc_to_case(a, b)

def case_suivante(num_case, sens, nb_cases=1): # sur un tore
    l, c = case_to_lc(num_case)
    if sens == NORD:
        return lc_to_case((l-nb_cases)%NB_LIG,c)
    if sens == SUD:
        return lc_to_case((l+nb_cases)%NB_LIG,c)
    if sens == EST:
        return lc_to_case(l,(c+nb_cases)%NB_LIG)
    if sens == OUEST:
        return lc_to_case(l,(c-nb_cases)%NB_LIG)

def pivot_horaire(nb=1):
    return (direction + nb) % 4

# callbacks
def quitter():
    fenApp.destroy()

def reset():
    reset_interface()
       
def lancer(event):  # avec la barre espace
    global run
    if run == False:
        run = True
    build_interface()

STOP = False # Game stater

#tout ce qui est là est une parenthèse

def tourne_gauche(event):  # flèche fauche ou bouton gauche souris
    global direction
    
    direction = pivot_horaire(nb=3)
    #direction = 'LEFT'

def tourne_droite(event):  # flèche droite ou bouton droite souris
    global direction 
    direction = pivot_horaire(nb=1)
    #direction = 'RIGHT'

# Construction graphique du jeu
def peuple_frames(fen):
    frame = Frame(fen)
    return frame

def peuple_gestion(fen):
    btn1 = Button(canvas, text="Quitter", font=40, command=lambda: quitter())
    btn1.place(relx=0.67, rely=0.9,relheight=0.05, relwidth=0.3)
    
    btn2 = Button(canvas, text="Reset", font=40, command=lambda: reset())
    btn2.place(relx=0.35, rely=0.9,relheight=0.05, relwidth=0.3)
    
    btn3 = Button(canvas, text="Lancer", font=40)
    btn3.place(relx=0.03, rely=0.9,relheight=0.05, relwidth=0.3)


    

fenApp.bind("<Right>",tourne_droite)
fenApp.bind("<Left>", tourne_gauche) 
fenApp.bind("<space>",lancer)


def peuple_jeu(fen):
    global pomme,run,score,snake
    carreau = [[canvas.create_rectangle(BORDER+(num_lig*T_CASE),BORDER+(num_col*T_CASE),BORDER+(num_lig+1)*T_CASE, BORDER+(num_col+1)*T_CASE, fill="#FFFFFF") for num_lig in range(NB_COL)] for num_col in range(NB_LIG)]

    #création de la pomme
    canvas.create_oval(pomme[0],pomme[1], pomme[0]+T_CASE, pomme[1]+T_CASE, fill='red')
    
    
    for corps in snake:
            x_centre, y_centre = case_to_xy(corps[0])
            canvas.create_oval(x_centre, y_centre, x_centre + 20,
                            y_centre + 20, outline="green", fill="yellow")
   
    if case_to_xy(snake[0][0]) == (pomme):
        pomme = (randrange(50,350,20),randrange(50,350,20))
        print('la pomme est touchée')
        snake.append(pomme)
        score +=10
        scores.set(str(score))
        
    for i in range(1,len(snake)):
        if case_to_xy(snake[0][0])==case_to_xy(snake[i][0]):
            canvas.create_text(200,190,fill='red',font=('Times 20 italic bold',20), text="Game Over !")
            canvas.delete(serpentTete)
            canvas.after(10)
            run = False


def peuple_score(fen):
    global score,scores
    L = Label(canvas,text ="Score Player n º 1: " )
    L.place(relx=0.13, rely=0.05,relheight=0.05, relwidth=0.3)
    scores = StringVar()
    E = Entry(canvas, textvariable = scores,width=10)
    E.place(relx=0.5, rely=0.05,relheight=0.05, relwidth=0.3)
    scores.set('0')
    
    
def reset_interface():
    global snake, score
    score = 0
    snake.clear()
    snake = [(114,1), (99,2), (98,3), (97,4)]
    #pomme = [randrange(50,350,20),randrange(50,350,20)]
    canvas.create_oval(pomme[0],pomme[1], pomme[0]+T_CASE, pomme[1]+T_CASE, fill='red')
    #peuple_frames(fenApp)
    peuple_jeu(fenApp)
     


def build_interface():
    global run, canvas, score
    fenApp.title("Petit snake 2020")
    peuple_frames(fenApp)
    avance()
    canvas.delete('all')
    peuple_jeu(fenApp)
    init_serpent()
    fenApp.update()
    if run != False:
        fenApp.after(FPS,build_interface)

# Initialisations des variables globales
def init_globals():
    pass


# Construction du serpent
def init_serpent():
    global direction
    snake = [(114,1), (99,2), (98,3), (97,4)]



def avance():
    global snake, score
    snake = [(case_suivante(snake[0][0], direction, 1), snake[-1][1])] + snake[:-1]
    score += 1
    scores.set(str(score))
    
peuple_gestion(fenApp)
peuple_score(fenApp)


#POur  le second joueur
#Label(fenApp, text ="Score Player 2 : ").grid(row=0,column=2)
#Score2 = Entry(fenApp, textvariable=scores,width=10)
#Score2.grid(row=0,column=3)

def test_fonctions():
    pass

if __name__ == "__main__":
    test_fonctions()
    # build_interface()
    # fenApp.mainloop()

build_interface()
fenApp.mainloop()