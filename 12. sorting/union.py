def solve(lst_a, lst_b):
    a_union_b = []

    i = j = 0

    while i < len(lst_a) and j < len(lst_b):
        if lst_a[i] == lst_b[j]:
            a_union_b.append(lst_a[i])
            i += 1
            j += 1
        else:
            if lst_a[i] < lst_b[j]:
                a_union_b.append(lst_a[i])
                i +=1
            else:
                a_union_b.append(lst_b[j])
                j +=1
    
    if i != len(lst_a):
        a_union_b.extend(lst_a[i:])
    if j != len(lst_b):
        a_union_b.extend(lst_a[j:])
    
    return a_union_b


lst_a = [1, 2, 3, 4, 5, 6] 
lst_b = [3, 5, 7, 8, 9]

print(solve(lst_a, lst_b))