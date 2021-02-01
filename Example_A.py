# Libraries:
import os

#############NOTE
#Codiii
# Pas 0 - ordenar les pizzes
##### objecte/array de pizzes que tinguin els mateixos ingredients
##### hash objectes
##### classe pizza per saber si té un ingredient en concret
##### crear objecte pizza
##### paquets de pizzes i distribuir
# Pas 1 - calcular el número d'entregues que podem fer (combinacions possibles d'equips)
# Pas 2 - combinacions de pizza segons les entregues
##### Tenir en compte que hi ha pizzes iguals

#############EONOTE

# Read data from first file:
#file = '/Users/laiagvernet/Documents/HashCode_practice/HashCode2021/Data_Files/a_example.in'
#data_file = open(file, "r")

# Get first line from file:
#first_line = data_file.readline()

# Get info from first line:
#n_pizza = first_line[0]
#n_t2 = first_line[2]
#n_t3 = first_line[4]
#n_t4 = first_line[6]

# Close data file:
#data_file.close()

##NOTE: Alternative code by ASL
##NOTE: realtive path <-- Without problems to get files beetwen differents OS
p = os.path.dirname(__file__) #path as p
fn = os.path.join(p,'Data_Files/a_example.in') #File Name as fn
obj = {} #empty global variable to contains objects to get all properties by line

#TODO: Getting excetions??
with open(fn) as f:
    try:
        line = f.readline()
        cnt = 0
        while line:
            ##NOTE: Show information
            #print('Line {}: {}'.format(cnt, line.strip()))

            ##NOTE: adding line information into array by counter
            ##f.e.: obj[0] contains array with [5,1,2,1]
            obj[cnt]=line.split(' ')
                        
            line = f.readline()
            cnt += 1
    except:
        print('Some exception happened!')

    finally:
        f.close()

print(obj)
