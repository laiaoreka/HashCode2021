# Libraries:
import os
import Classes

##NOTE: Relative path <-- Without problems to get files beetwen differents OS
p = os.path.dirname(__file__)  # path as p
fn = os.path.join(p, 'Data_Files/c_many_ingredients.in')  # File Name as fn
obj = {}  # empty global variable for containing objects in order to get all properties by line


##VARIABLES
list_ing = {}  # List containing Objects from Pizza class
T = Classes.Teams()  # Init teams class as global variable
P = Classes.Pizzas()
I = Classes.Ingredients()


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

#print('All teams: %s' % T.tms)
ingredients = set([item for sublist in P.ing for item in sublist])
print(ingredients)
# print('get team info: teams?? ->%s pax?? ->%s'%(T.tms['by3']['team'], T.tms['by3']['pax']))
