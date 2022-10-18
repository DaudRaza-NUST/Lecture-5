#%%
def quotient_and_remainder(x,y):
    q = x//y
    r = x%y
    return (q,r)
(quot, rem) = quotient_and_remainder(3,4)
# a = quotient_and_remainder(5, 3)
# print(a)
print((quot))
print((rem))
a = (quot, rem)
a = a + 1
print(a)
print(quot)
#%%
def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[1],)
        if t[0] not in words:
            words = words + (t[0],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

a = (('A', 9), ('B', 7), ('C', 4), ('C', 5), ('D', 1), ('E', 8), ('E', 7))
print(get_data(a))
#%%
a_list = []
L = [2, 'a', 4, [1,2]]
print(len(L))
print(L[0])
print(L[2]+1)
print(L[3])
#%%
def descending(alist):
    alist.sort()
    a = len(alist)
    for i in alist:
        print(alist[a-i])
    return
a = [9,5,6,10,8,1,7,4,3,2]
descending(a)
#%%
L = [1,2,3]
L.append(5)
print(L)
#%%
L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2
print(L3)
# print(L1.extend(0))
#%%
s = 'I<3 cs'
print(list(s))
print(s.split('<'))
L = ['a', 'b', 'c']
print(s.join(L))
#%%
a = 1
b = a
print(a)
print(b)
# append retroactively changes the equvilant variable as well
warm = ['red','yellow','orange']
hot = warm
hot.append('pink')
print(hot)
print(warm)
#%%
cool = ['blue', 'green', 'grey']
chill = cool[:]
chill.append('black')
print(chill)
print(cool)
