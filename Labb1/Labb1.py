U = list(range(1, 31))

evens = [x for x in U if x % 2 == 0]
odds = [x for x in U if x % 2 != 0]

# Skapar delmängderna
# element = listan som vi väljer element från (evens eller odds)
# S = den delmängd som byggs upp
# start = indexet där sökningen ska börja
# size = hur många element kombinationen ska innehålla
# subsets = lista där de färdiga kombinationerna sparas
def create_subsets(element, S, start, size, subsets):

    # När S innehåller rätt antal element är kombinationen färdig.
    if len(S) == size:
        subsets.append(tuple(S))
        return

    # Loopar igenom elementen i listan och lägger till nuvarande i S
    # Sedan anropar funktionen rekursivt för att fortsätta bygga upp S (delmängden).
    # Pop tar bort det senaste elementet från S för att backa och prova nästa element i listan.
    for i in range(start, len(element)):
        S.append(element[i])
        create_subsets(element, S, i + 1, size, subsets)

        S.pop()

# Skapar alla möjliga kombinationer av 4 jämna och 3 udda tal
E_S = []
O_S = []

create_subsets(evens, [], 0, 4, E_S)
create_subsets(odds, [], 0, 3, O_S)

valid_subsets = []

# Loopar igenom alla delmängder
# Kontrollerar om summan av delmängden är 105 och om produkten är delbar med 360
# Om båda villkoren är uppfyllda läggs delmängden till i slutliga listan
for E in E_S:
    for O in O_S:

        S = E + O

        if sum(S) == 105:

            p = 1

            for num in S:
                p *= num

            if p % 360 == 0:
                valid_subsets.append(S)

print(f"Totala antalet giltiga delmängder S: {len(valid_subsets)}")

print("\nLista över alla giltiga delmängder:")
for subset in valid_subsets:
    print(subset)