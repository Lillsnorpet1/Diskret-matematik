U = list(range(1, 61))

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

E_S_raw = []
O_S = []

create_subsets(evens, [], 0, 5, E_S_raw)
create_subsets(odds, [], 0, 6, O_S)

print("subsets created")

# 1. FÖRFILTRERA E_S: Kräver minst ett tal delbart med 4 för att nå 2^6
E_S = [E for E in E_S_raw if any(x % 4 == 0 for x in E)]

# 2. Skapa dictionary och förberäkna ALLT för O (produkt, femmor, treor, sjuor)
O_dict = {}
for O in O_S:
    O_sum = sum(O)
    
    p_O = 1
    for num in O:
        p_O *= num
        
    O_7 = any(x % 7 == 0 for x in O)
    O_5 = sum(1 for x in O if x % 5 == 0)
    O_3 = sum(1 for x in O if x % 3 == 0)
    
    if O_sum not in O_dict:
        O_dict[O_sum] = []
    O_dict[O_sum].append((O, p_O, O_7, O_5, O_3)) 

print("dictionary created")

valid_subsets = []
product = (2 ** 6) * (3 ** 3) * (5 ** 2) * 7

for E in E_S:
    required_sum = 330 - sum(E)
    if required_sum not in O_dict:
        continue

    p_E = 1
    for num in E:
        p_E *= num

    # Förberäkna E
    E_7 = any(x % 7 == 0 for x in E)
    E_5 = sum(1 for x in E if x % 5 == 0)
    E_3 = sum(1 for x in E if x % 3 == 0)

    for O, p_O, O_7, O_5, O_3 in O_dict[required_sum]:

        # Byt ut tunga looper mot färdiga variabler!
        if not E_7 and not O_7:
            continue

        if E_5 + O_5 < 2:
            continue

        if E_3 + O_3 < 3:
            continue

        if (p_E * p_O) % product != 0:
            continue

        valid_subsets.append(E + O)

print("valid subsets created")

valid_subsets.sort()
smallest_subset = valid_subsets[0] if valid_subsets else []
largest_subset = valid_subsets[-1] if valid_subsets else []

print("sorting done")

d_values = []
for subsets in valid_subsets:
  evens_sum = sum(x for x in subsets if x % 2 == 0)
  odds_sum = sum(x for x in subsets if x % 2 != 0)
  d = abs(evens_sum - odds_sum)
  d_values.append(d)

print("D(S) values calculated")

min_d = min(d_values) if d_values else 0
max_d = max(d_values) if d_values else 0

print(f"Totala antalet giltiga delmängder S: {len(valid_subsets)}")
print(f"2. Lexikografiskt minsta delmängd: {smallest_subset}")
print(f"2. Lexikografiskt största delmängd: {largest_subset}")
print(f"3. Minsta värdet av D(S): {min_d}")
print(f"3. Maxima värdet av D(S): {max_d}")

#print("\nLista över alla giltiga delmängder:")
#for subset in valid_subsets:
#   print(subset)