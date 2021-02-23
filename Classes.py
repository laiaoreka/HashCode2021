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


class Pizzas:
    def set(self, cnt, line):
        self.pzs = {'Pizza': str(cnt-1), 'Total ingredients': line[0], 'Ingredients': sorted(line[1:len(line)])}
        self.pizzas.append(self.pzs)

    def __init__(self):
        self.pizzas = []
        return


class Deliveries:
    def set(self, perm, tot_pizza, tot_pax, by2, by3, by4):
        if int(tot_pizza) > int(tot_pax):
            self.delis = {'Total pax': str(tot_pax), 'Total pzs': tot_pizza, 'del_by2': by2, 'del_by3': by3, 'del_by4': by4}
        else:
            for i in list(perm):
                [a, tot_pzs2] = self.delis_pzs(tot_pizza, i[0], by2, by3, by4)
                [b, tot_pzs3] = self.delis_pzs((int(tot_pizza)-tot_pzs2), i[1], by2, by3, by4)
                [c, tot_pzs4] = self.delis_pzs(((int(tot_pizza)-tot_pzs2)-tot_pzs3), i[2], by2, by3, by4)
                self.delis = {'Total pax': str(tot_pax), 'Total pzs': (tot_pzs2+tot_pzs3+tot_pzs4), 'del_by'+str(i[0]): a, 'del_by'+str(i[1]): b, 'del_by'+str(i[2]): c}
                self.all_delis.append(self.delis)

    def delis_pzs(self, pzs, mod, by2, by3, by4):
        if mod == 2:
            by = by2
        elif mod == 3:
            by = by3
        else:
            by = by4

        tot_dls = int(pzs) // int(mod)
        if tot_dls > int(by):
            tot_dls = int(by)
            tot_pzs = int(tot_dls)*int(mod)
        else:
            tot_pzs = int(tot_dls) * int(mod)
        return tot_dls, tot_pzs

    def __init__(self):
        self.all_delis = []
        return


class Unique:
    def set(self, pizzas):
        self.uni_pzs = (list(map(list, set(map(lambda i: tuple(i), [d['Ingredients'] for d in pizzas])))))
