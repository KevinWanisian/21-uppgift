# Importera random-modulen för att använda slumpmässiga funktioner
import random

# Definiera färgkoder för text i terminalen
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Initialisera variabler
SpelarVal = True  # Variabel för spelarens val
dealer_in = True  # Variabel för att hålla koll på dealerns tur
Spelarhand = []  # Lista för spelarens kort
Datorhand = []  # Lista för dealerns kort
ui = 15  # Bredden på gränssnittet

# Definiera en dictionary för kortleken
Deck = {
    "Hjärter": ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knäckt", "Dam", "Kung"],
    "Ruter": ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knäckt", "Dam", "Kung"],
    "Spader": ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knäckt", "Dam", "Kung"],
    "Klöver": ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knäckt", "Dam", "Kung"],
}

# Funktion för att beräkna kortvärden
def CardValue(turn):
    card_values = {"Kung": 13, "Dam": 12, "Knäckt": 11, "Ess": 14}
    total = 0
    ess_räknare = 0

    for kort in turn:
        card_value = card_values.get(kort, None)
        if card_value is not None:
            total += card_value
        else:
            total += int(kort)

        if kort == "Ess":
            ess_räknare += 1

    while total > 21 and ess_räknare > 0:
        total -= 13
        ess_räknare -= 1

    return total

# Funktion för att dela ut kort
def deal(turn):
    slumpa_mönster = random.choice(list(Deck.keys()))
    available_cards = Deck[slumpa_mönster]

    if available_cards:
        card = random.choice(available_cards)
        turn.append(card)
        available_cards.remove(card)

# Användargränssnitt
print(".: TJUGOETT :.")
print("*" * ui)
deal(Spelarhand)
input("Tryck Enter för att börja...")

# Spelarens val att ta kort eller stanna
while SpelarVal:
    print("-" * ui)
    print(BLUE + "Du drog:")
    for card in Spelarhand:
        print(card)
    print(BLUE + f"Totalpoäng: {CardValue(Spelarhand)}")

    if CardValue(Spelarhand) > 21:
        break

    if SpelarVal:
        print(RESET + "-" * ui)
        hit_or_stay = input(RESET + "Vill du: 1 = Ta kort  2 = Stanna> ")

        if hit_or_stay == "1":
            deal(Spelarhand)
        elif hit_or_stay == "2":
            print("Du väljer att stanna på: ")
            for card in Spelarhand:
                print(BLUE + card)
            print(RESET + "-" * ui)
            break
        else:
            input("Fel. Välj antingen 1 eller 2")
            continue

# Dealerns tur att spela
while dealer_in:
    if not Datorhand:
        deal(Datorhand)
        continue
    elif CardValue(Datorhand) > 16:
        dealer_in = False
        print(RED + "Dealern drog: ")
        for card in Datorhand:
            print(card)
        print(RED + f"Totalpoäng: {CardValue(Datorhand)}")

    elif dealer_in:
        deal(Datorhand)

    elif CardValue(Datorhand) > 21:
        break

# Beräkna spelarens och dealerns poäng
Spelaren = CardValue(Spelarhand)
Datorn = CardValue(Datorhand)

# Skriv ut resultatet
if Datorn and Spelaren > 21:
    print("Spelaren och Dealern gick över 21! Dealern vinner.")
elif Datorn == Spelaren:
    print("Dealern och Spelaren har lika mycket poäng. Dealern vinner!")
elif Datorn == 21:
    print("21! Dealern vinner.")
elif Spelaren == 21:
    print(GREEN + "WOOHOO 21! Spelaren vinner.")
elif Spelaren > 21:
    print("Du översteg 21! Dealern vinner.")
elif Datorn > 21:
    print(GREEN + "Dealern översteg 21! Du vinner.")
elif Datorn > Spelaren:
    print("Dealern vinner!")
else:
    print(GREEN + "Spelaren vinner!")
