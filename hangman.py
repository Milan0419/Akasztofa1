import random
import os
import time
import platform


#Base dir. meghatározása
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HANGMAN = [
    """
     -----
     |   |
         |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    """
]

#Dominik
def guessing_letter(word, guess):
    used_letters = set()
    wrong_letters = set()
    tries = 0
    MAX_TRIES = 5
    
    while "".join(guess).lower() != word.lower() and tries < MAX_TRIES:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        
        print(HANGMAN[tries])
        print("Szó:", " ".join(guess))
        print("Hibás betűk:", ", ".join(sorted(wrong_letters)))
        print(f"Hátralévő próbálkozások: {MAX_TRIES - tries}")
        
        #Milán
        while True:
            user_guess = input("Tippelj egy betűt: ").lower()
            if len(user_guess) == 1 and user_guess.isalpha():
                break
            else:
                print("Csak EGY darab BETŰT adj meg!")
        
        if user_guess in used_letters:
            print("Erre már tippeltél!")
            time.sleep(1.5)
            continue
        
        used_letters.add(user_guess)
            
        if user_guess == word.lower():
            guess[:] = list(word)
            break
            
        if len(user_guess) != 1:
            print("Csak egy betűt írj be!")
            time.sleep(1.5)
            continue
            
        if user_guess in word.lower():
            for i, char in enumerate(word):
                if char.lower() == user_guess:
                    guess[i] = char
        else:
            wrong_letters.add(user_guess)
            tries += 1
    # Dominik
    # Végeredmény
    if "".join(guess).lower() == word.lower():
        print("Gratulálok, nyertél!")
        for i in range(10):
            time.sleep(10)
    else:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        print(HANGMAN[MAX_TRIES])
        print("Vesztettél!")
        print("A szó ez volt:", word)
    
    print("\nNyomj ENTER-t az új játékhoz...")
    input()

def load_words(filename):
    path = os.path.join(BASE_DIR, filename) #Base directory meghatározása, így bármilyen eszközön megtalálja a fájlokat
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


# Functionok a szó kiválasztásához, 
def easy():
    return random.choice(load_words("konnyu.txt"))

def medium():
    return random.choice(load_words("kozepes.txt"))

def hard():
    return random.choice(load_words("nehez.txt"))

def mixed():
    return random.choice(load_words("vegyes.txt"))

def book():
    return random.choice(load_words("irodalom.txt"))


welcome_text = """
                    Üdvözlünk az akasztófa játékunkban!
                
        Kis ismertető a témákról:
        - Van a könnyű téma (Egyszerű, gyakori szavak).
        - Van a közepes szavak listája.
        - Van a nehezebb, ritkábban használatos szavak listája.
        - Van a vegyes téma, amelyben országok és foglalkozások nevei találhatók.
        - És legvégül van az irodalmi téma, ahol művek és művek szereplői vannak.

        A szabályok nagyon egyszerűek:
        - Minden szó magyar szó, lehetnek ékezetek.
        - Az olyan betűket, mint gy, sz, ty és társait külön kell tippelni.
        - Ügyeljünk, hogy ne számot és ne speciális jelet tippeljünk.
        - A hibázási lehetőségek száma: 5.

        A konzol 10 másodperc múlva törlődik.
"""

print(welcome_text)
word = ""

# Fél perc várakozás
for i in range(10, 0, -1):
    print(f"\rTörlés {i} másodperc múlva...", end="")
    time.sleep(1)

# Konzol törlése OS-től függően
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

# Fő loop
while True:
    rnd_while = True   
    guess = []
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    # Game loop
    # Milan
    while rnd_while:

        # Témaválasztás
        print("Témák: könnyű, közepes, nehéz, vegyes, irodalom")
        choice = str(input("Rendben van, eljött az ideje hogy kiválassza a témát: "))
        choice = choice.lower()

        #Téma szerint egy véletlenSZERŰ szó kiválasztása
        if choice == "könnyű" or choice == "konnyu":
            word = easy()
            rnd_while = False
        elif choice == "közepes" or choice == "kozepes":
            word = medium()
            rnd_while = False
        elif choice == "nehéz" or choice == "nehez":
            word = hard()
            rnd_while = False
        elif choice == "vegyes":
            word = mixed()
            rnd_while = False
        elif choice == "irodalom":
            word = book()
            rnd_while = False
        else: 
            print("Kérlek jól írd be! ")
    
    #Konzol törlés (Esztétikai okokból)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    
    #A kiírandó (amit ki kell találni) kreálása
    guess = []
    for x in word:
        if x in " -:":
            guess.append(x)
        else:
            guess.append("_")

    #A FŐ FŐ function meghívása, itt történik az egész játék
    guessing_letter(word, guess)
    
    #Tesztrész