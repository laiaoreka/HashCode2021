# Libraries:

# Read data from first file:
file = '/Users/laiagvernet/Documents/HashCode_practice/HashCode2021/Data_Files/a_example.in'
data_file = open(file, "r")

# Get first line from file:
first_line = data_file.readline()

# Get info from first line:
n_pizza = first_line[0]
n_t2 = first_line[2]
n_t3 = first_line[4]
n_t4 = first_line[6]


# Create the class pizza:
class Pizza:
    def __init__(self, index, total_ing, ing):
        self.index = index
        self.total_ing = total_ing
        self.ing = ing


# Get list of pizzas:
lines = data_file.readlines()[0:]
f = [i.strip('\n').split(' ') for i in lines]
ind = 0
pizzas = []
for pizza in f:
    P = Pizza(ind, pizza[0], pizza[1:len(pizza)])
    pizzas.append(P)
#print(pizzas[0].ing)

# Get ingredients of unique pizzas:
unique = set()
for i in range(len(pizzas)):
    unique.add(tuple(sorted(pizzas[i].ing)))
print(unique)







# Codiii
# Pas 0 - ordenar les pizzes
##### objecte/array de pizzes que tinguin els mateixos ingredients
##### hash objectes
##### classe pizza per saber si té un ingredient en concret
##### crear objecte pizza
##### paquets de pizzes i distribuir
# Pas 1 - calcular el número d'entregues que podem fer (combinacions possibles d'equips)
# Pas 2 - combinacions de pizza segons les entregues
##### Tenir en compte que hi ha pizzes iguals


# Close data file:
data_file.close()
