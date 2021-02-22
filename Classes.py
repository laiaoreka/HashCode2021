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
        self.pzs = {'Pizza': str(cnt-1), 'Total ingredients': line[0], 'Ingredients': sorted(line[1:len(line)])}
        self.pizzas.append(self.pzs)

    def __init__(self):
        self.pizzas = []
        return


class Deliveries:
    def set(self, tot_pizza, tot_pax, by2, by3, by4):
        if int(tot_pizza) > int(tot_pax):
            self.delis = {'Total pax': str(tot_pax), 'del_by2': by2, 'del_by3': by3, 'del_by4': by4}
        else:
            self.delis = 0

    def __init__(self):
        return

class Unique:
    def set(self, pizzas):
        self.uni_pzs = (list(map(list, set(map(lambda i: tuple(i), [d['Ingredients'] for d in pizzas])))))
