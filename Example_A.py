# Libraries:
import os
import Classes
import loops
import itertools

##NOTE: Relative path <-- Without problems to get files beetwen differents OS
p = os.path.dirname(__file__)  # path as p
fn = os.path.join(p, 'Data_Files/a_example.in')  # File Name as fn
obj = {}  # empty global variable for containing objects in order to get all properties by line


##VARIABLES
combis = {}
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

unique2 = P.get_unique()

print(unique)
print([d['Pizza'] for d in unique2])




