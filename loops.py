def combis_of_two(unique, combis, tot_pzs_2, final2=[]):

    j = len(unique) - 1
    i = len(unique) - 1
    # Get best combinations of 2:
    while j >= 0:
        while i >= 0:
            u = len(set(unique[i]) ^ set(unique[j]))
            common = len(set(unique[i]) | set(unique[j])) - u
            if common == 0:
                combis[str(i)] = {}
                combis[str(i)]['Pzs_id'] = sorted([i, j])
                combis[str(i)]['Uni'] = u

                if sorted([i, j]) not in [d['Pzs_id'] for d in final2]:
                    if len(final2) < int(tot_pzs_2):
                        final2.append(combis[str(i)])
                    else:
                        break
            i = i-1

        i = len(unique) - 1
        j = j-1

    return final2

def combis_of_three(unique, combis, tot_pzs_3, final3=[]):

    j = len(unique) - 1
    i = len(unique) - 1
    k = len(unique) - 1
    # Get best combinations of 2:
    while j >= 0:
        while k >= 0:
            while i >= 0:
                u = len(set(unique[i]) ^ (set(unique[j]) ^ set(unique[k])))
                common = len(set(unique[i]) | (set(unique[j]) | set(unique[k]))) - u
                print(j,k,i)
                print("common = ", common)
                print("unique = ", u)
                if common == 0:
                    combis[str(i)] = {}
                    combis[str(i)]['Pzs_id'] = sorted([i, j, k])
                    combis[str(i)]['Uni'] = u

                    if sorted([i, j, k]) not in [d['Pzs_id'] for d in final3]:
                        if len(final3) < int(tot_pzs_3):
                            final3.append(combis[str(i)])
                        else:
                            break
                i = i-1

            i = len(unique) - 1
            k = k-1

        i = len(unique) - 1
        k = len(unique) - 1
        j = j-1

    return final3