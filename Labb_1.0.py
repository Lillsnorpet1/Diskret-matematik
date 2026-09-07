U = list(range(1, 31))

evens = [x for x in U if x % 2 == 0]
odds = [x for x in U if x % 2 != 0]


def create_groups(numbers, size):
    groups = []

    if size == 3:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                for k in range(j + 1, len(numbers)):
                    group = (numbers[i], numbers[j], numbers[k])
                    groups.append((group, sum(group)))

    elif size == 4:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                for k in range(j + 1, len(numbers)):
                    for l in range(k + 1, len(numbers)):
                        group = (numbers[i], numbers[j], numbers[k], numbers[l])
                        groups.append((group, sum(group)))

    return groups


def product(S):
    p = 1

    for num in S:
        p *= num

    return p


valid_subsets = []


#4 jämna + 3 udda
even_group_4 = create_groups(evens, 4)
odd_group_3 = create_groups(odds, 3)

for eg in even_group_4:
    for og in odd_group_3:

        if eg[1] + og[1] == 105:

            S = eg[0] + og[0]

            if product(S) % 360 == 0:
                if S not in valid_subsets:
                    valid_subsets.append(S)


print(f"Totala antalet giltiga delmängder S: {len(valid_subsets)}")

print("\nLista över alla giltiga delmängder:")
for subset in valid_subsets:
    print(subset)