import itertools as it
from operator import itemgetter

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
            for i in list(perm):
                if i[0] == 2 and i[1] == 3:
                    self.delis = {'Comb': i, 'Total pax': str(tot_pax), 'Total pzs': tot_pizza, 'del_by2': by2, 'del_by3': by3,
                                  'del_by4': by4}
                elif i[0] == 2 and i[1] == 4:
                    self.delis = {'Comb': i, 'Total pax': str(tot_pax), 'Total pzs': tot_pizza, 'del_by2': by2, 'del_by4': by4,
                                  'del_by3': by3}
                elif i[0] == 3 and i[1] == 2:
                    self.delis = {'Comb': i, 'Total pax': str(tot_pax), 'Total pzs': tot_pizza, 'del_by3': by3, 'del_by2': by2,
                                  'del_by4': by4}
                elif i[0] == 3 and i[1] == 4:
                    self.delis = {'Comb': i, 'Total pax': str(tot_pax), 'Total pzs': tot_pizza, 'del_by3': by3, 'del_by4': by4,
                                  'del_by2': by2}
                elif i[0] == 4 and i[1] == 2:
                    self.delis = {'Comb': i, 'Total pax': str(tot_pax), 'Total pzs': tot_pizza, 'del_by4': by4, 'del_by2': by2,
                                  'del_by3': by3}
                else:
                    self.delis = {'Comb': i, 'Total pax': str(tot_pax), 'Total pzs': tot_pizza, 'del_by4': by4, 'del_by3': by3,
                                  'del_by2': by2}

                self.all_delis.append(self.delis)
        else:
            for i in list(perm):
                [a, tot_pzs2] = self.delis_pzs(tot_pizza, i[0], by2, by3, by4)
                [b, tot_pzs3] = self.delis_pzs((int(tot_pizza)-tot_pzs2), i[1], by2, by3, by4)
                [c, tot_pzs4] = self.delis_pzs(((int(tot_pizza)-tot_pzs2)-tot_pzs3), i[2], by2, by3, by4)
                self.delis = {'Comb': i, 'Total pax': str(tot_pax), 'Total pzs': (tot_pzs2+tot_pzs3+tot_pzs4), 'del_by'+str(i[0]): a, 'del_by'+str(i[1]): b, 'del_by'+str(i[2]): c}
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
        self.delis = {}
        return

class Combinations:
    def get_combis(self, permut, ings, num):

        self.uni_ing2.clear()
        self.uni_ing3.clear()
        self.uni_ing4.clear()
        self.uni_comb.clear()

        if num == 2:
            self.uni_ing2 = [[comb[0], comb[1], len(set(ings[int(comb[0])] + ings[int(comb[1])]))] for comb in permut]
            #self.uni_ing2.append({'Pizzas': comb, 'unique': unique})
            self.uni_ing = self.uni_ing2
        elif num == 3:
            self.uni_ing3 = [[comb[0], comb[1], comb[2], len(set(ings[int(comb[0])] + ings[int(comb[1])] + ings[int(comb[2])]))] for comb in permut]
            self.uni_ing = self.uni_ing3
        elif num == 4:
            self.uni_ing4 = [
                [comb[0], comb[1], comb[2], comb[3], len(set(ings[int(comb[0])] + ings[int(comb[1])] + ings[int(comb[2])] + ings[int(comb[3])]))] for
                comb in permut]
            self.uni_ing = self.uni_ing4

        return self.uni_ing

    def get_remaining(self, combinations, indx, num, tope2, tope3, tope4):

        maxtomin = sorted(combinations, key=itemgetter(num), reverse=True)

        if num == 2:
            final = maxtomin[0:int(tope2)]
        elif num == 3:
            final = maxtomin[0:int(tope3)]
        elif num == 4:
            final = maxtomin[0:int(tope4)]

        pizzas = [l[:num] for l in final]
        c = list(it.chain.from_iterable(pizzas))
        indx = list(set(indx) ^ set(c))

        return final, indx

    def get_permut(self, indx, num):
        permut_orig = it.permutations(indx, num)
        permut = {self.to_sorted(i) for i in permut_orig}

        return permut

    def to_sorted(self, t):
        return tuple(sorted(t))


    def __init__(self):
        self.uni_comb = []
        self.uni_ing = []
        self.uni_ing2 = []
        self.uni_ing3 = []
        self.uni_ing4 = []
        return


