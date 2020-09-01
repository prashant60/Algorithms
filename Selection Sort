def selection_sort(n):
    for i in range(0,len(n)-1):
        min_value=n[i]
        for j in range(i+1,len(n)):
            if n[j]<min_value:
                min_value=n[j]
        min_index=n.index(min_value)
        if min_index==i:
            pass
        else:
            n[i],n[min_index]=n[min_index],n[i]
    return n

n=[5,1,7,3,6,2,9,4]
print(selection_sort(n))
