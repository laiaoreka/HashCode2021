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
C = Cl.Combinations()

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

# 2 - Explore all combinations:
max_combis = []

for i in D.all_delis:

    [indx, ings] = [[d['Pizza'] for d in P.pizzas], [d['Ingredients'] for d in P.pizzas]]

    a = list(i['Comb'])
    tope2 = i['del_by2']
    tope3 = i['del_by3']
    tope4 = i['del_by4']
    print(a[0], a[1], a[2])

    # 1st of combination:
    permut0 = C.get_permut(indx, a[0])
    combis0 = C.get_combis(list(permut0), ings, a[0])
    [final0, indx0] = C.get_remaining(combis0, indx, a[0], tope2, tope3, tope4)
    print('by'+str(a[0]), final0)

    # 2nd of combination:
    permut1 = C.get_permut(indx0, a[1])
    combis1 = C.get_combis(list(permut1), ings, a[1])
    [final1, indx1] = C.get_remaining(combis1, indx0, a[1], tope2, tope3, tope4)
    print('by'+str(a[1]), final1)

    # 3rd of combination:
    permut2 = C.get_permut(indx1, a[2])
    combis2 = C.get_combis(list(permut2), ings, a[2])
    [final2, indx2] = C.get_remaining(combis2, indx1, a[2], tope2, tope3, tope4)
    print('by' + str(a[2]), final2)









