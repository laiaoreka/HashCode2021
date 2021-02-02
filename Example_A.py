# Libraries:
import os
from math import factorial

##NOTE: Alternative code by ASL
##NOTE: Relative path <-- Without problems to get files beetwen differents OS
p = os.path.dirname(__file__)  # path as p
fn = os.path.join(p, 'Data_Files/a_example.in')  # File Name as fn
obj = {}  # empty global variable for containing objects in order to get all properties by line


##CLASSES
## He fet aquesta classe que faig servir més endavant que potser no cal o hi ha una altra manera de fer (segur!!!)
class Pizza:
    def __init__(self, index, total_ing, ing):
        self.index = index
        self.total_ing = total_ing
        self.ing = ing


##FUNCTIONS
def get_index_pos(list_of_elems, element):
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list


##VARIABLES
header = ()
pizzas = []  # List containing Objects from Pizza class


# TODO: Getting exceptions??
with open(fn) as f:
    try:
        line = f.readline()
        cnt = 0
        while line:
            ##NOTE: Show Line information
            # print('Line {}: {}'.format(cnt, line.strip()))

            ##NOTE: Getting Line information
            if cnt == 0:
                ##NOTE: Get header information
                header = tuple(line.strip('\n').split(' '))
            else:
                ##NOTE: Create Pizza Objects
                P = Pizza(cnt, line.strip()[0], tuple(line.strip('\n').split(' ')[1:len(line.strip())]))
                pizzas.append(P)

            line = f.readline()
            cnt += 1
            ##NOTE: adding line information into array by counter
            ##f.e.: obj[0] contains array with [5,1,2,1]
            # obj[cnt] = line.split(' ')

    except:
        print('Some exception happened!')

    finally:
        f.close()

##NOTE: LGV --> aquests dos paràgrafs funcionen bé però s'han d'optimitzar que segur que hi ha una manera
## de fer-ho millor. La idea és cada fila de la llista uniq_list equival a una de les combinacions d'ingredients
## possibles. En el cas de l'exemple A, com que les pizzes 1 i 3 són iguals, hi ha una fila de la uniq_list
## que conté els valors [1,3].
##NOTE: Getting unique pizzas
# List of ingredients for each pizza:
list_ing = []
for i in range(len(pizzas)):
    list_ing.append(sorted(pizzas[i].ing))

# List indexes of unique pizzas:
uniq_list = []
for i in range(len(list_ing)):
    indexes = get_index_pos(list_ing, list_ing[i])
    if indexes not in uniq_list:
        uniq_list.append(indexes)
#print(uniq_list)

##NOTE: How many deliveries?
tot_pizzas = int(header[0])
tot_persons = int(header[1])*2+int(header[2])*3+int(header[3])*4

if tot_pizzas > tot_persons:
    del_2 = int(header[1])
    #print(del_2, 'de 2 pizzes')
    del_3 = int(header[2])
    #print(del_3, 'de 3 pizzes')
    del_4 = int(header[3])
    #print(del_4, 'de 4 pizzes')
else:
    print("Estic encallada aquí!!!")
