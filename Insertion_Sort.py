
def insertion_sort1(a):
    for i in range(1,len(a)):
        for j in range(i-1,-1,-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            else:
                break
    return a

def insertion_sort2(a):
    for i in range(1,len(a)):
        j=i-1
        while a[j]>a[j+1] and j>=0:
            a[j],a[j+1] = a[j+1],a[j]
            j-=1
    return a

def insertion_sort3(a):
    for i in range(1,len(a)):
        curr=a[i]
        for j in range(i-1,-2,-1):
            if a[j]>curr:
                a[j+1]=a[j]
            else:
                break
        a[j+1]=curr
    return a




a=[10,9,8,5,3,7,92,185,78,1,0,65]
print(insertion_sort1(a))
print(insertion_sort2(a))
print(insertion_sort3(a))
