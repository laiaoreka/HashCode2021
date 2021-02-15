from typing import Dict, Any, Union
import Functions

class Teams:
    def set(self, line):
        self.tot_pizza = line[0]
        self.tms = {
            'by2': {
                'teams': line[1],
                'pax': 2 * int(line[1])
            },
            'by3': {
                'teams': line[2],
                'pax': 3 * int(line[2])
            },
            'by4': {
                'teams': line[3],
                'pax': 4 * int(line[3])
            }
        }

        self.total_pax = sum(int(val['pax']) for key, val in self.tms.items())

    def __init__(self):
        return


##TODO and THINK, class pizzas as collection of pizza
class Pizzas:
    def set(self, cnt, line):
        self.pzs = {'Pizza': str(cnt-1), 'Total ingredients': line[0], 'Ingredients': line[1:len(line)]}
        self.pizzas.append(self.pzs)
        self.ing.append(self.pzs.get('Ingredients'))

    def __init__(self):
        self.pizzas = []
        self.ing = []
        return


##TODO and THINK, class ingredients as pizza's subclass
class Ingredients(Pizzas):
    def set(self, something):
        self.all_ings = something

    def __init__(self):
        return


class Deliveries:
    def set(self, tot_pizza, tot_pax, by2, by3, by4):
        if int(tot_pizza) > int(tot_pax):
            self.delis = {'Total pizzas': str(tot_pax), 'del_by2': by2, 'del_by3': by3, 'del_by4': by4}
        else:
            self.delis = 0

    def __init__(self):
        return


class Combis:
    def set(self, pizzas):
        self.pzs_ing = [d['Ingredients'] for d in pizzas]

        self.comb = Functions.combinaciones(self.pzs_ing, 2)
        for i in range(len(self.comb)):
            common = len(np.intersect1d(self.comb[i][0], self.comb[i][1]))
            unique = len(set(self.comb[i][0] + self.comb[i][1]))
            self.combis_2.append({'Comb_id': i, 'Common ing': common, 'Uni ing': unique, 'Combi': self.comb[i]})

        self.comb = Functions.combinaciones(self.pzs_ing, 3)
        for i in range(len(self.comb)):
            #common =
            unique = len(set(self.comb[i][0] + self.comb[i][1] + self.comb[i][2]))
            self.combis_3.append({'Comb_id': i, 'Common ing': common, 'Uni ing': unique, 'Combi': self.comb[i]})

        self.comb = Functions.combinaciones(self.pzs_ing, 4)
        for i in range(len(self.comb)):
            #common =
            unique = len(set(self.comb[i][0] + self.comb[i][1] + self.comb[i][2] + self.comb[i][3]))
            self.combis_4.append({'Comb_id': i, 'Common ing': common, 'Uni ing': unique, 'Combi': self.comb[i]})

    def __init__(self):
        self.combis_2 = []
        self.combis_3 = []
        self.combis_4 = []
        return