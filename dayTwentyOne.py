seen = set()
allergens = {}
all_chunks = set()
sets_of_chunks = []
mapping = {}
with open("dayTwentyOne.txt") as file:
    for line in file:
        line = line.rstrip()
        line = line.replace(")", "")
        chunks = line.split(" (contains ")

        curr_set = {ingredient for ingredient in chunks[0].split()}
        sets_of_chunks.append(curr_set)

        for ingredient in chunks[0].split():
            if ingredient not in all_chunks:
                all_chunks.add(ingredient)   
        
        for allergen in chunks[1].split(", "):
            if allergen in allergens:
                allergens[allergen] = allergens[allergen].intersection(curr_set)
            else:
                allergens[allergen] = curr_set

            if len(allergens[allergen]) == 1:
                val = allergens[allergen].pop()
                seen.add(val)
                mapping[allergen] = val 
            elif len(seen.intersection(allergens[allergen])) == len(allergens[allergen]) - 1:
                diff = allergens[allergen] - seen.intersection(allergens[allergen])
                val = diff.pop()
                seen.add(val)
                mapping[allergen] = val 

for allergen, ingredients in allergens.items():
    if len(ingredients) > 0:
        if len(seen.intersection(allergens[allergen])) == len(allergens[allergen]) - 1:
            diff = allergens[allergen] - seen.intersection(allergens[allergen])
            val = diff.pop()
            seen.add(val)
            mapping[allergen] = val 
            
count = 0
for unseen in (all_chunks - seen):
    for chunk in sets_of_chunks:
        if unseen in chunk:
            count += 1

print(f"q1 ans = {count}")

# q2 

allergens_list = [allergen for allergen in allergens.keys()]

allergens_list.sort()

res = []

for allergen in allergens_list:
    res.append(mapping[allergen])

res = ",".join(res)

print(f"q2 ans = {res}")
