# Libraries:
import os
import Classes

##NOTE: Relative path <-- Without problems to get files beetwen differents OS
p = os.path.dirname(__file__)  # path as p
fn = os.path.join(p, 'Data_Files/d_many_pizzas.in')  # File Name as fn
obj = {}  # empty global variable for containing objects in order to get all properties by line


##VARIABLES
list_ing = {}  # List containing Objects from Pizza class
T = Classes.Teams()  # Init teams class as global variable
P = Classes.Pizzas()
D = Classes.Deliveries()
U = Classes.Unique()


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

# Get teams information:
#print('All teams: %s' % T.tms)
# print('get team info: teams?? ->%s pax?? ->%s'%(T.tms['by3']['team'], T.tms['by3']['pax']))

# Get number of deliveries:
D.set(T.tot_pizza, T.total_pax, T.tms.get('by2').get('teams'), T.tms.get('by3').get('teams'), T.tms.get('by4').get('teams'))
print('Total deliveries: ', D.delis)

# Get list of unique pizzas based on ingredients:
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

#print(set(unique[0]) ^ set(unique[1]))
#print(len(set(unique[60514]) ^ set(unique[60513])))

# Get best combinations of 2:
while j >= 0:
    while i >= 0:
        u = len(set(unique[i]) ^ set(unique[j]))
        common = len(set(unique[i]) | set(unique[j])) - u
        if common == 0:
            combis[str(i)] = {}
            combis[str(i)]['Pzs_id'] = sorted([i, j])
            combis[str(i)]['Uni'] = u
            #combis[str(i)]['Comb'] = [unique[len(unique)-i], unique[len(unique)-j]]
            if sorted([i, j]) not in [d['Pzs_id'] for d in final2]:
                if len(final2) < int(tot_pzs_2):
                    final2.append(combis[str(i)])
                else:
                    break
        i = i-1

    i = 0
    j = j-1