def bubble_sort(n):
    for i in range(0,len(n)-1):
        for j in range(0,len(n)-1-i):
            max_val=n[j]
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n

n=[3,2,4,1,19,7,5,9,22,6]
print(bubble_sort(n))
