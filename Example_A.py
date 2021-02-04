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
class Teams:
    def __init__(self, line):
        self.tot_pizza = line[0]
        self.by2 = {2: line[1]}
        self.by3 = {3: line[2]}
        self.by4 = {4: line[3]}

    def get_two_px(self):
        return self.by2.key*self.by2.value

    def get_three_px(self):
        return self.by3.key*self.by3.value

    def get_four_px(self):
        return self.by4.key*self.by4.value

    def get_tot_people(self):
        return self.by2.key*self.by2.value + self.by3.key*self.by3.value + self.by4.key*self.by4.value


class Pizza:
    def __init__(self, index, total_ing, ing):
        self.index = index
        self.total_ing = total_ing
        self.ing = ing

    def get_ingredients(self):
        return self.ing


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

            ret = index_pos_list
        except ValueError as e:
            print("Exception: {}".format(e))
            ret = False
            #break

    return ret


##VARIABLES
list_ing = {}  # List containing Objects from Pizza class


# TODO: Getting exceptions??
with open(fn) as f:
    try:
        line = f.readline()
        cnt = 0
        while line:
            ##NOTE: Show Line information
            line = line.strip('\n').split(' ')
            #print('Line {}: {}'.format(cnt, line))

            ##NOTE: Getting Line information
            if cnt == 0:
                ##NOTE: Get header information
                T = Teams(line)
            else:
                ##NOTE: Create Pizza Objects
                P = Pizza(cnt, line[0], line[1:len(line)])
                list_ing[cnt] = P.get_ingredients()

            line = f.readline()
            cnt += 1
            ##NOTE: adding line information into array by counter
            ##f.e.: obj[0] contains array with [5,1,2,1]
            # obj[cnt] = line.split(' ')

    except:
        print('Some exception happened!')

    finally:
        f.close()

print(T.get_two_px())

##NOTE: LGV --> aquests dos paràgrafs funcionen bé però s'han d'optimitzar que segur que hi ha una manera
## de fer-ho millor. La idea és cada fila de la llista uniq_list equival a una de les combinacions d'ingredients
## possibles. En el cas de l'exemple A, com que les pizzes 1 i 3 són iguals, hi ha una fila de la uniq_list
## que conté els valors [1,3].
##NOTE: Getting unique pizzas
# List of ingredients for each pizza:

# ##NOTE: How many deliveries?
# tot_pizzas = int(header[0])
# tot_persons = int(header[1])*2+int(header[2])*3+int(header[3])*4
#
# if tot_pizzas > tot_persons:
#     del_2 = int(header[1])
#     #print(del_2, 'de 2 pizzes')
#     del_3 = int(header[2])
#     #print(del_3, 'de 3 pizzes')
#     del_4 = int(header[3])
#     #print(del_4, 'de 4 pizzes')
# else:
#     print("Estic encallada aquí!!!")
