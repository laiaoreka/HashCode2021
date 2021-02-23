# Libraries:
import os
import Classes as c
from itertools import permutations

##NOTE: Relative path <-- Without problems to get files beetwen differents OS
p = os.path.dirname(__file__)  # path as p
fn = os.path.join(p, 'Data_Files/d_many_pizzas.in')  # File Name as fn
obj = {}  # empty global variable for containing objects in order to get all properties by line


##VARIABLES
list_ing = {}  # List containing Objects from Pizza class
T = c.Teams()  # Init teams class as global variable
P = c.Pizzas()
D = c.Deliveries()
U = c.Unique()


# TODO: Getting exceptions??
with open(fn) as f:
    try:
        line = f.readline()
        cnt = 0
        while line:
            ##NOTE: Show Line information
            line = line.strip('\n').split(' ')
            # print('Line {}: {}'.format(cnt, line))

            ##NOTE: Getting Line information
            if cnt == 0:
                ##NOTE: Get header information and set to Teams
                T.set(line)
            else:
                P.set(cnt, line)
                ##NOTE: Create Pizza Objects
                #P = Pizza(cnt, line[0], line[1:len(line)])
                #list_ing[cnt] = P.get_ingredients()

            line = f.readline()
            cnt += 1

    except Exception as e:
        print('Some exception happened!')
        print(e)
    finally:
        f.close()

# 0 - Get teams information:
#print('All teams: %s' % T.tms)

# 1 - Get number of deliveries:
perm = permutations([2, 3, 4])
D.set(perm, T.tot_pizza, T.total_pax, T.tms.get('by2').get('teams'), T.tms.get('by3').get('teams'), T.tms.get('by4').get('teams'))

for i in D.all_delis:
    print(i)

# 2 - Get list of unique pizzas based on ingredients:
U.set(P.pizzas)
unique = sorted(U.uni_pzs)
unique.sort(key=len)

j = len(unique)-1
i = len(unique)-1
k = 0
combis = {}
final2 = []
print('Total unique pizzas: ', len(unique))
#print('Total de 2: ', D.delis['del_by2'])
tot_pzs_2 = str(1)#D.delis['del_by2']





