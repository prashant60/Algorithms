import sys
def merge_sort(n):
    split(n,0,len(n)-1)
    return n

def split(n,first,last):
    if first<last:
        middle=(first+last)//2
        split(n,first,middle)
        split(n,middle+1,last)
        merge(n,first,middle,last)

def merge(n,first,middle,last):
    l=n[first:middle+1]
    r=n[middle+1:last+1]
    l.append(sys.maxsize)
    r.append(sys.maxsize)
    i=j=0

    for k in range(first,last+1):
        if l[i]<=r[j]:
            n[k]=l[i]
            i+=1
        else:
            n[k]=r[j]
            j+=1


n=[5,9,1,2,4,8,6,3,7]
print(merge_sort(n))

