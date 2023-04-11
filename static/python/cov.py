# generic status list:
# 
# 0 ok
# 1 unknown command
# 2 unknown subcommand
# 3 unknown argument
# 4 user data error
# 5 user input error
# 6 history status
# 7 unknown status
# 8 recoverable intern error
# 9 unrecoverable intern error

def main(com):
    global ok
    global hists
    global histl
    tmp=0

    if com[0] == "quit":
        ok=False
        print("Au revoir !")
        return 0
    elif com[0] == "about" or com[0] == "version":
        tmp=about()
    elif com[0] == "aide":
        tmp=help(com)
    elif com[0] == "dec":
        tmp=dec(com)
    elif com[0] == "cov":
        tmp=cov(com)
    elif com[0] == "nicer":
        tmp=nicerc(com)
    elif com[0] == "history" or com[0] == "hist" or com[0] == "!!":
        tmp=histc(com, histl)
    else:
        print("ERR: commande inconnue : '" + com[0] + "'")
        return 1
    
    if type(tmp) != tuple:
        histl.append((com, tmp))
    elif tmp[1] == 6:
        True

    if len(histl) > hists:
        histl.pop(0)
    return tmp

def nicerc(com):
    argtype="num"
    number=[]
    base=False

    for i in range(len(com)):
        if com[i] == "nicer":
            True
        elif com[i] == "num" or com[i] == "n":
            argtype="num"
        elif com[i] == "base" or com[i] == "b":
            argtype="base"
        elif com[i].isnumeric():
            if argtype == "num":
                number.append(int(com[i]))
            elif argtype == "base":
                if base == False:
                    base=int(com[i])
                    argtype=False
                else:
                    print("ERR: base a déjà été définie")
                    return 5
            else:
                print("ERR: l'argument '" + com[i] + "' ne peut être assigné (aucune variable précisée)")
                return 3
        else:
            print("ERR: argument inconnu '" + com[i] + "'")
            return 2

    if not base:
        print("ERR: base inconnue")
        return 4
    if number == []:
        print("ERR: nombre inconnu")
        return 4
    if len(number) == 1:
        print(number)
        return True

    done=nicer(number, base)
    if done == False:
        print("ERR: une erreur interne s'est produite lors de l'affichage")
        print()
        print(str(number) + "." + str(base))
        return 8
    elif done == True:
        print(str(number) + "." + str(base))
    else:
        print(done)
    return 0

# util function, shouldn't be directly used by user (look at nicerc)
# altered returned generic status
def nicer(num, base):
    out = ""
    if base <= 10:
        for i in num:
            if i < base:
                out+=str(i)
            else:
                print("INT/ERR: num > base")
                return False
    elif base <= 35:
        global dico
        for i in num:
            if i < 10:
                out+=str(i)
            elif i < base:
                out+=dico.get(i)
            else:
                print("INT/ERR: num > base")
                return False
    else:
        return True

    if base == 2:
        out="0b" + out
    elif base == 8:
        out="0o" + out
    elif base == 16:
        out="0x" + out
    else:
        out="(base " + str(base) + ") : " + out
    return out

def help(com):
    if len(com) == 1:
        print("""liste des commandes :
  about version
  aide
  cov
  dec
  nicer
  quit
  !! history
exécuter 'aide COMMANDE' pour afficher de l'aide pour COMMANDE
exécuter 'aide err' pour afficher de l'aide concernant les status""")
    elif com[1] == "err":
        print("""aide concernant les status :
Chaque exécution de commande renvoie un status (code d'error numérique) (exit status)
Les status génériques possibles sont les suivants :
  0 : aucune erreur, valeur par défaut (true)
  1 : commande inconnue (unknown command)
  2 : sous-commande inconnue (unknown sub-command)
  3 : argument inconnu (unknown argument)
  4 : erreur de données utilisateur (user data error)
  5 : erreur d'entrée utilisateur (user input error)
  6 : status spécifique à la réexécution d'une commande par history
  7 : status inconnu (unknown status)
  8 : erreur interne contournable (recoverable intern error)
  9 : erreur interne nécessitant l'arrêt de la commande (unrecoverable intern error)
Le status de la commande précédente est affiché dans le prompt""")
    elif com[1] == "quit":
        print("""quit - quitter le programme
Note : revient à entrer EOF dans un prompt vide""")
    elif com[1] == "about" or com[1] == "version":
        print("about - version - afficher des informations sur le programme")
    elif com[1] == "aide":
        print("""aide - afficher de l'aide pour les commandes
arguments :
  COM
    le nom de la commande interne pour laquelle afficher de l'aide""")
    elif com[1] == "cov":
        print("""cov - convertir NUM de base 10 en base BASE
sous-commandes :
  num ARG
    spécifie le nombre à convertir
    ARG est un nombre
      NOTE: ARG ne doit contenir que des nombres/chiffres de 0 à 9
  base ARG
    spécifie la base vers laquelle convertir le nombre
    ARG est un nombre (en base 10)
exemples :
  convertir 12 de base 10 en base 16 :
    cov num 12 base 16""")
    elif com[1] == "dec":
        print("""dec - convertir NUM de base BASE en base 10
sous-commandes :
  num ARG
    spécifie le nombre à convertir
    ARG est un nombre ou une liste de nombres :
      si un seul nombre, ce nombre est utilisé
      si une liste de nombres, chaque nombre est utilisé comme chiffre du nombre final
      NOTE: ARG ne doit contenir que des nombres/chiffres de 0 à 9
  base ARG
    spécifie la base depuis laquelle convertir le nombre
    ARG est un nombre (en base 10)
exemples :
  convertir 12 de base 16 en base 10 :
    dec num 12 base 16
    dec num 1 2 base 16
  convertir 1A de base 16 en base 10 :
    dec num 1 10 base 16 """)
    elif com[1] == "!!" or com[1] == "history" or com[1] == "hist":
        print("""!! - history - historique des commandes
sous-commandes
  (un nombre)
    un nombre : réexécute la commande à l'indexe nombre de l'historique
  list
    affiche la liste de l'historique des commandes et de leur status
  set NUM
    définit la longueur de l'historique à NUM (par défaut vaut 20)
  get
    affiche la longueur de l'historique actuelle
exemple :
  réexécuter la 4e dernière commande :
    history 4
    !! 4
  définir la taille de l'historique à 12 :
    history set 12
    !! set 12""")
    elif com[1] == "nicer":
        print("""nicer - afficher une chaine de caractères améliorée pour une suite de chiffres
Renvoie l'affichage correct du nombre reçu en sa base
Remplace les chiffres supérieurs à 9 par des lettres : nicer ne prend pas en charge les nombres à base supérieure à 35
sous-commandes :
  num ARG
    spécifie le nombre à convertir
    ARG est un nombre ou une liste de nombres :
      si un seul nombre, ce nombre est utilisé
      si une liste de nombres, chaque nombre est utilisé comme chiffre du nombre final
      NOTE: ARG ne doit contenir que des nombres/chiffres de 0 à 9
  base ARG
    spécifie la base depuis laquelle convertir le nombre
    ARG est un nombre (en base 10)
exemple :
  afficher correctement le nombre ayant pour chiffres 12 0 8 15 en base 16 :
    nicer num 12 0 8 15 base 16
    (renvoie 0xA08F)""")
    else:
        print("ERR: pas d'aide pour '" + com[1] + "'")
        return 3
    return 0

def cov(com, p=False):
    argtype="num"
    number=False
    base=False
    out=[]
    rest=1

    for i in range(len(com)):
        if com[i] == "cov":
            True
        elif com[i] == "num" or com[i] == "n":
            argtype="num"
        elif com[i] == "base" or com[i] == "b":
            argtype="base"
        elif com[i].isnumeric():
            if argtype == "num":
                if number == False:
                    number=int(com[i])
                    argtype="base"
                else:
                    print("ERR: number a déjà été défini")
                    return 5
            elif argtype == "base":
                if base == False:
                    base=int(com[i])
                    argtype=False
                else:
                    print("ERR: base a déjà été définie")
                    return 5
            else:
                print("ERR: l'argument '" + com[i] + "' ne peut être assigné (aucune variable précisée)")
                return 3
        else:
            print("ERR: argument inconnu '" + com[i] + "'")
            return 2

    if not base:
        print("ERR: base inconnue")
        return 4
    if not number:
        print("ERR: nombre inconnu")
        return 4

    print("RECAP - cov")
    print("nombre :", number)
    print("base :", base)
    print()

    while number > 0:
        rest = number % base
        number //= base
        out.insert(0, rest)

        print(number, "x", base, "+", rest)

    if p:
        return (out, base)
    else:
        print()
        done=nicer(out, base)
        if done == False:
            print("ERR: une erreur interne s'est produite lors de l'affichage")
            print()
            print(str(out) + "." + str(base))
            return 8
        elif done == True:
            print(str(out) + "." + str(base))
        else:
            print(done)
    return 0

def dec(com, p=False):
    argtype="num"
    number=[]
    base=False
    out=0

    for i in range(len(com)):
        if com[i] == "dec":
            True
        elif com[i] == "num" or com[i] == "n":
            argtype="num"
        elif com[i] == "base" or com[i] == "b":
            argtype="base"
        elif com[i].isnumeric():
            if argtype == "num":
                number.append(int(com[i]))
            elif argtype == "base":
                if base == False:
                    base=int(com[i])
                    argtype=False
                else:
                    print("ERR: base a déjà été définie")
                    return 5
            else:
                print("ERR: l'argument '" + com[i] + "' ne peut être assigné (aucune variable précisée)")
                return 3
        else:
            print("ERR: argument inconnu '" + com[i] + "'")
            return 2

    if not base:
        print("ERR: base inconnue")
        return 4
    if number == []:
        print("ERR: nombre inconnu")
        return 4
    if len(number) == 1:
        number = [int(x) for x in str(number[0])]

    print("RECAP - dec")
    print("nombre :", number)
    print("base :", base)
    print()

    for i in range(len(number)):
        if number[i] < base:
            v = number[i] * (base ** (len(number) - 1 - i))
            out += v
            print("+", number[i], "x", str(base) + "^" + str(len(number) - 1 - i), "( = " + str(v) + ")")
        else:
            print("ERR: ce chiffre est plus grand que la base :", number[i])
            return 4

    if p:
        return (out, 10)
    else:
        print()
        print(out)
    return 0

def histc(com, histl):
    global hists
    if len(com) == 1 or com[1] == "l" or com[1] == "list":
        if len(com) > 2 and com[2].isnumeric():
            print(histl[len(histl) - int(com[2]) - 1][0])
        else:
            for i in range(len(histl)):
                print(len(histl) - i, ":", histl[i][0], histl[i][1])
            print("0 :", com, "[en cours, actuellement 0]")
    elif com[1].isnumeric():
        if int(com[1]) <= len(histl):
            print("réexécution de la suite", histl[len(histl) - int(com[1]) - 1][0], " (status", histl[len(histl) - int(com[1]) - 1][1], ") :")
            print()
            return (main(histl[len(histl) - int(com[1]) - 1][0]), 6)
        else:
            print("ERR: l'historique ne remonte pas jusqu'à", com[1])
            return 5
    elif com[1] == "set" and len(com) > 1:
        if com[2].isnumeric():
            hists = int(com[2])
            print("L'historique a maintenant une longueur de", hists)
        else:
            print("ERR: l'argument de set doit être un nombre")
            return 3
    elif com[1] == "get":
        print("L'historique a une longueur de", hists)
    else:
        print("ERR: argument inconnu :", com[1])
        return 2
    return 0

def about():
    global version
    global author
    print("cov - version""", version, "- écrit par", author)
    return 0

ok=True
status=0
hists=20
histl=[]
version="7fr"
author="lapingenieur"

from string import ascii_uppercase as letters
dico={}
for i in range(len(letters)):
    dico.update({i+10: letters[i]})

print("""Bienvenue dans le programme cov !
Convertisseur de bases numérales théoriquement infinies avec interface en ligne de commandes
Pour afficher de l'aide, utilisez la commande 'aide' dans le prompt ci-dessous

cov - version""", version, "- écrit par", author)

while ok:
    print()
    if type(status) == tuple:
        status=status[0]
    if status == None:
        status=7
    try:
        com=input(str(status) + " > ").split()

        if len(com) != 0:
            print()
            status=main(com)
    except EOFError:
        print("quit")
        print()
        main(["quit"])
