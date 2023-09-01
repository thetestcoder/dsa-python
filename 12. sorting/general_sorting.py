def gnome_sort(Arr):
    i = 0
    while i < len(Arr):
        if i == 0 or Arr[i-1] <= Arr[i]:
            i += 1
        else:
            Arr[i], Arr[i-1] = Arr[i-1], Arr[i]
            i -= 1
        
    return Arr

Arr = [6, 3, 2, 6, 4, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]

print(gnome_sort(Arr))