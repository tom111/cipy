def removeDup (l1,l2):
    "Removes and returns duplicates from two lists"
    rej = []
    for l in l1:
        try:
            l2.remove(l)
            l1.remove(l)
            rej += [l]
        except ValueError:
            pass
    return rej;

def flatten(lst):
    "Flattens a list of lists 1 level"
    ret = []
    for elem in lst:
        if type(elem) in (tuple, list):
            for i in flatten(elem):
                ret.append(i)
        else:
            ret.append(elem)
    return ret
            
