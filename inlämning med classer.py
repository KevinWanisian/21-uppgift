import random

# Detta ändrar textens färg i terminalen
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"


# Variabler
class variabel:
    SpelarVal = True
    dealer_in = True
    Spelarhand = []
    Datorhand = []


ui = 15


# Kortlek med olika värden och färger
class kortlek:
    Deck = {
        "Hjärter": ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knäckt", "Dam", "Kung"],
        "Ruter": ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knäckt", "Dam", "Kung"],
        "Spader": ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knäckt", "Dam", "Kung"],
        "Klöver": ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knäckt", "Dam", "Kung"],
    }

    # Funktion för att beräkna poäng
    def CardValue(turn):
        # En dictionary som innehåller värden för "speciella" kort (inte kort med siffror)
        card_values = {
            "Kung": 13,
            "Dam": 12,
            "Knäckt": 11,
            "Ess": 14
        }

        # Variabel för START-poängen
        total = 0

        # Räknar antalet Ess i handen
        ess_räknare = 0

        # En For Loop för att gå igenom varje kort i spelarens eller datorns hand
        for kort in turn:
            card_value = card_values.get(kort, None)  # Hämtar värdet för det aktuella kortet från dictionaryn (kortlek.Deck)

            # Om kortet finns i dictionaryn, lägg till dess värde till den totala poängen
            if card_value is not None:
                total += card_value
            else:
                # Om kortet inte finns i dictionaryn, skapar ett numeriska värde till respektive kort (Kung, Dam, Knäckt)
                total += int(kort)

            # Om kortet är ett ess, öka räknaren
            if kort == "Ess":
                ess_räknare += 1

        # Om totala poängen överstiger 21 och det finns ess i handen, sänk essens värde från 14 till 1
        while total > 21 and ess_räknare > 0:
            total -= 13
            ess_räknare -= 1

        # Returnernar den totala poängen
        return total


# Funktion för att dela ut kort

def Deal(turn):
    # Random kort
    random_suit = random.choice(list(kortlek.Deck.keys()))  # Väljer ett slumpmässigt mönster t.ex "Hjärter", "Ruter"
    available_cards = kortlek.Deck[random_suit]  # Kollar efter tillgängliga kort i det valda mönstret

    if available_cards:
        card = random.choice(available_cards)  # Slumpa ett kort från den valda sviten
        turn.append(card)  # Lägger till det slumpade kortet i spelarens eller dealerns hand
        available_cards.remove(card)  # Ta bort kortet som blev slumpat från kortlek.Deck listan


# Användargränssnitt/ui
print(".: TJUGOETT :.")
print("*" * ui)

# Ger ett kort efter man har tryckt in "Enter"
Deal(variabel.Spelarhand)
input("Tryck Enter för att börja...")

# Spelarens väljer att stanna eller ta fler kort
while variabel.SpelarVal:
    print("-" * ui)
    print(BLUE + "Du drog:")
    for card in variabel.Spelarhand:
        print(card)
    print(BLUE + (f"Totalpoäng: {kortlek.CardValue(variabel.Spelarhand)}"))

    if kortlek.CardValue(variabel.Spelarhand) > 21:
        break

    if variabel.SpelarVal:
        print(RESET + "-" * ui)
        hit_or_stay = input(RESET + "Vill du: 1 = Ta kort  2 = Stanna> ")

        if hit_or_stay == "1":
            Deal(variabel.Spelarhand)
        elif hit_or_stay == "2":
            print("Du väljer att stanna på: ")
            for card in variabel.Spelarhand:
                print(BLUE + card)
            print(RESET + "-" * ui)
            break
        else:
            input("Fel. Välj antingen 1 eller 2")
            continue


# Dealerns/Datorn tur att spela
while variabel.dealer_in:
    if not variabel.Datorhand:
        Deal(variabel.Datorhand)
        continue
    elif kortlek.CardValue(variabel.Datorhand) > 16:
        variabel.dealer_in = False
        print(RED + "Dealern drog: ")
        for card in variabel.Datorhand:
            print(card)
        print(RED + f"Totalpoäng: {kortlek.CardValue(variabel.Datorhand)}")

    elif variabel.dealer_in:
        Deal(variabel.Datorhand)

    elif kortlek.CardValue(variabel.Datorhand) > 21:
        break

# Räknar poängen för Spelaren och Dealern/Datorn
Spelaren = kortlek.CardValue(variabel.Spelarhand)
Datorn = kortlek.CardValue(variabel.Datorhand)

# Skriver ut resultatet
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
