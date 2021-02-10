from typing import Dict, Any, Union


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
