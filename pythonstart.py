# 1
"""
imie = input("Podaj swoje imie")
wiek = int(input("Podaj wiek"))
ile = int(input("ile razy"))
data = 2120 - wiek
for i in range(ile):
    print(imie + " skończy 100 lat w roku ")
    print(data)
"""
# 2
"""
liczba = int(input("Podaj liczbę"))
if liczba % 4 ==0:
    print("podzielne przez 4")
else:
    if liczba % 2 == 0:
        print("liczba jest parzysta")
    else:
        print("liczba jest nieparzysta")
"""
# 3
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
i = 0
for i in range(i, len(a)):
    if a[i] < 5:
        print(a[i])

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([aa for aa in a if aa < 5])
"""
# 4 szukanie dzielników
"""
jaka = int(input("Dawaj liczbe"))
x = range(1, jaka + 1) #x=[1,2,3,4,5.....]
a = 1
for a in range(a, len(x) + 1):
    if jaka % a == 0:
        print(a)
"""
# 5
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commonlist = []
i=0
for i in range(0, len(a)): #pętla po liście a
    for x in range(0, len(b)):   #pętla po b
        if a[i] == b[x]:
            commonlist.append(b[x])
print(commonlist)
"""
# 6 skomplikawany palindrom
"""
wyraz = input("Czy jest palindromem?")
srodek = len(wyraz) // 2
i=0
palindrom = 0
while(i <= srodek):
    i += 1
    palindrom = 1
    if wyraz[i] != wyraz[len(wyraz) - i - 1]:
        print(wyraz + " nie jest palindromem")
        palindrom = 0
        i = srodek + 1

if palindrom == 1:
    print(wyraz + " jest palindromem")
"""
# 6 v2 troche mniej skomplikowany palindrom
"""
def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')
"""
# 7 zmniejszanie zapis list
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

listaparzystych = [liczba for liczba in a if liczba % 2 == 0]

print(listaparzystych)
"""
# 8 gra w kamień papier nożyce
"""
odpowiedzi = ["kamień", "papier", "nożyce"]
grasz = input("Grasz? tak v nie")
while(grasz == "tak"):
    codal1 = int(input("Napisz 1 graczu: kamień(1) v papier(2) v nożyce(3)"))
    codal2 = int(input("Napisz 2 graczu: kamień(1) v papier(2) v nożyce(3)"))
    
    
    codal1 = input("Napisz 1 graczu: kamień v papier v nożyce")
    codal2 = input("Napisz 2 graczu: kamień v papier v nożyce")
    if codal1 != "kamień" or "papier" or "nożyce" and codal2 != "kamień" or "papier" or "nożyce":
        print("Teraz zacznij od nowa i napisz poprawne odpowiedzi")
        break

    print(codal1, codal2)
    grasz = "nie"
"""
# 9
"""
import random

a = random.randint(1, 9)
print(a)
guess = 0
proby = 0
while(guess != "exit" and guess != a):
    guess = input("Podaj liczbę")
    proby += 1
    if guess == "exit":
        break
    guess = int(guess)
    if a == guess:
        proby = str(proby)
        print("trafiony! Ilość prób to: " +  proby)
        guess = "exit"
    elif guess < a:
        print("za mało")
    else:
        print("za dużo")
"""
# 10dwie listy i wspólne cyfry z mieszaniem list
"""
import random
a = random.sample(range(100), 50)
b = random.sample(range(100), 50)

listawspolna = [liczba_a for liczba_a in a  for liczba_b in b if liczba_a == liczba_b]
print(listawspolna)
"""
# 11 sprawdza czy liczba jest pierwsza
"""
liczba = int(input("Podaj liczbę, a ja sprawdzę, czy jest to liczba pierwsza."))
lista_dzielników = range(1, liczba + 1)
ilość_dzielników=0
a = 1
for a in range(a, len(lista_dzielników) + 1):
    if liczba % a == 0:
        ilość_dzielników += 1

if ilość_dzielników == 2:
    print("Jest to liczba pierwsza")
else:
    print("Nie jest to liczba pierwsza")
"""
# 12 pierwsze i ostatnie miejsce z listy użycie funkcji definicji
"""
def takeargument(number_fromlist):
    return a[number_fromlist]

a = [5, 10, 15, 20, 25]
b = []
b.append(takeargument(0))
b.append(takeargument(len(a) - 1))
print(b)
"""
# 13 generowanie fibbunaci czy jakos tak
"""
start = [1, 1]
def generowanie_nowych(ilość = "ile mam wygenerować tych liczb"):
    for x in range(2, ilość):
        start.append(start[x - 1] + start[x - 2])
    return print(start)

generowanie_nowych(int(input("ile mam ich wygenerować")))
"""
# 14 sets
"""
a = []
x = 0
while(x < 5):
    a.append(int(input("Podaj liczbe do tablicy, aby prerwać wpisz znak")))
    x += 1

a = set(a)
print(a)
"""
# 15 zamienia miejscami w tablicy
"""
def spliting_and_reversing():
    hasło = str(input("Podaj coś string najlepiej byq"))
    nowe = hasło.split()
    reverse  = []
    x = len(nowe)
    for i in range(1, x + 1):
        reverse.append(nowe[x - i])
    result = " ".join(reverse)
    print(result)
spliting_and_reversing()
"""
"""
def reverseWord(w):
  return ' '.join(w.split()[::-1])
"""
# 16 generowanie haseł
"""
import random


def generowanie(lenght):
    charsUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #1
    charsLow = "abcdefghijklmnopqrstuvwxyz"   #2
    charsNumber = "0123456789"                #3
    charsSpecial = "!@#$%&*()[]{}"            #4

    hasło = []
    for i in range(0, lenght):
        which = random.randint(1,4)
        if which == 1:
            hasło.append(random.choice(charsUpper))
        if which == 2:
            hasło.append(random.choice(charsLow))
        if which == 3:
            hasło.append(random.choice(charsNumber))
        if which == 4:
            hasło.append(random.choice(charsSpecial))
    hasło = ''.join(hasło)
    return hasło

lenght = int(input("Ile znaków?"))
print(generowanie(lenght))
"""
# 17 wypisywanie headtitles niedokończone
"""
from bs4 import  BeautifulSoup
import requests

r = requests.get('https://www.nytimes.com/').text
soup = BeautifulSoup(r, 'lxml')

for article in soup.find_all(class_="css-8atqhb"):
    headline = article.h2.text

    print(headline)
"""
# 18 cows and bulls nie zrobione
"""
import random

liczby = [0,1,2,3,4,5,6,7,8,9]
liczba = []
for i in range(0,4):
    liczba.append(random.choice(liczby))
liczba = [1,2,3,4]
print("liczba szukana: " , liczba)
print("Enter the number:")
cows = 0
bulls = 0
while cows < 4:
    cows = 0
    bulls = 0
    guess = str(input("Podaj 4 cyfry:"))
    for i in range(0,4):
        if guess[i] == liczba[i]:
            cows += 1
            print("jest")
        print(cows)

"""
# 19 łączenie dwóch stron http
"""from bs4 import  BeautifulSoup
import requests
pierwsza = "http://content.time.com/time/magazine/article/0,9171,2005869,00.html"
druga = "http://content.time.com/time/magazine/article/0,9171,2005869-2,00.html"
r1 = requests.get(pierwsza).text
r2 = requests.get(druga).text
soup1 = BeautifulSoup(r1, 'lxml')
soup2 = BeautifulSoup(r2, 'lxml')
for articles in soup1.find_all('p'):
    zawartosc = articles.text
    print(zawartosc)
for articles in soup2.find_all('p'):
    zawartosc = articles.text
    print(zawartosc)
"""
# 20
"""lista = [2, 4, 6, 8, 10]
numer = 1
def czy_jest_w_liscie(lista, numer):
    jest = False
    for i in range(len(lista)):
        if lista[i] == numer:
            jest = True

    print(jest)

czy_jest_w_liscie(lista, int(input("daj liczbę")))"""
# 21
"""nazwa_pliku = str(input("Podaj nazwę:"))

with open(nazwa_pliku + '.txt', 'w') as f:
    f.write("hello")
"""
# 22 słowniki
"""
imiona_ile = {}


with open('plik.txt', 'r') as plik:

    line = plik.readline()

    while line:
        line = line.strip()
        if line in imiona_ile:
            imiona_ile[line] += 1
        else:
            imiona_ile[line] = 1
        line = plik.readline()
print(imiona_ile)

"""
# 23 z dwóch plików czytanie
"""
with open('primenumbersunder1000.txt') as primes:
    lineprime = primes.readline()
    lineprime = lineprime.strip()
    while lineprime:
        with open('happynumbersunder1000.txt') as happy:
            linehappy = happy.readline()
            linehappy = linehappy.strip()
            while linehappy:
                if lineprime == linehappy:
                    print(linehappy)

                linehappy = happy.readline()
                linehappy = linehappy.strip()
        lineprime = primes.readline()
        lineprime = lineprime.strip()

"""
# 24
"""
def siatka(szerokość, długość):
    for l in range(długość):


        for w in range(szerokość):
            print("--- " +)
        for w in range(szerokość):
            print()
            print("|")
            print()


print(siatka(3, 3))


"""
# 28
"""
def największazliczb(liczba1, liczba2, liczba3):
    max = 0
    if liczba2 > liczba1:
        max = liczba2
        if liczba3 > max:
            max = liczba3
    else:
        max = liczba1
        if liczba3 > max:
            max = liczba3

    print(max)

liczba1 = int(input("Podaj liczbę 1:"))
liczba2 = int(input("Podaj liczbę 2:"))
liczba3 = int(input("Podaj liczbę 3:"))

największazliczb(liczba1, liczba2,liczba3)

"""
# 29
"""
import requests
import random
from bs4 import BeautifulSoup

url = 'http://norvig.com/ngrams/sowpods.txt'
r = requests.get(url).text

with open('pl')
"""


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# task 2 codewars

def countBits(n):
    inbits = []
    ile = 0
    while n > 0:
        inbits.append(n % 2)
        n = n // 2
    print(inbits)
    for i in inbits:
        if i == 1:
            ile += 1
    return ile

countBits(10)






