# Libraries:
import os
import Classes as Cl
import itertools as it

# Relative path <-- Without problems to get files beetwen differents OS
p = os.path.dirname(__file__)  # path as p
fn = os.path.join(p, 'Data_Files/a_example.in')  # File Name as fn
obj = {}  # empty global variable for containing objects in order to get all properties by line

# Class objects initializations
T = Cl.Teams()
P = Cl.Pizzas()
D = Cl.Deliveries()
U = Cl.Unique()

# 0 - Get file information:
with open(fn) as f:
    try:
        line = f.readline()
        cnt = 0
        while line:
            # Show Line information
            line = line.strip('\n').split(' ')
            # print('Line {}: {}'.format(cnt, line))

            # Getting Line information
            if cnt == 0:
                # Get header information and set to Teams
                T.set(line)
            else:
                P.set(cnt, line)

            line = f.readline()
            cnt += 1

    except Exception as e:
        print('Some exception happened!')
        print(e)
    finally:
        f.close()

# print('All teams: %s' % T.tms)

# 1 - Get number of deliveries:
perm = it.permutations([2, 3, 4])
D.set(perm, T.tot_pizza, T.total_pax, T.tms.get('by2').get('teams'), T.tms.get('by3').get('teams'), T.tms.get('by4').get('teams'))

# 2 - Get list of unique pizzas based on ingredients:
U.set(P.pizzas)
unique = sorted(U.uni_pzs)
unique.sort(key=len)

# initialize lists
uni_comb = []
uni_ing = []

[indx, ings] = [[d['Pizza'] for d in P.pizzas], [d['Ingredients'] for d in P.pizzas]]
permut = it.permutations(indx, 2)

for comb in permut:
    idx = sorted(list(comb))
    if idx not in uni_comb:
        uni_comb.append(idx)
        ing_a = ings[int(idx[0])]
        ing_b = ings[int(idx[1])]
        unique = len(set(ing_a) ^ set(ing_b))
        uni_ing.append({'Pizzas': idx, 'unique': unique})

from operator import itemgetter
newlist = sorted(uni_ing, key=itemgetter('unique'), reverse=True)
print(newlist)






