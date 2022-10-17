from itertools import accumulate
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import groupby
from itertools import count, cycle, repeat
from calendar import c
from logging import exception
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from calendar import month
from ctypes import pointer
import string
from timeit import default_timer as timer
import sys
from math import*

"""
mylist = ["Apple", "Banana", "Guava"]
print(mylist)

mylist2 = list()
print(mylist2)

if "Banana" in mylist:
    print("yes")
else:
    print("No")

mylist.insert(2, "Orange")
print(mylist)
numbers = [1, 2, 3, 4, 5, -3, 90, -9]
sorted_list = sorted(numbers)
print(sorted_list)
new_list = mylist = sorted_list

print(new_list)
# reverse: print(: : -1)
list_org = ["banana", "apple", "orange"]
list_copy = list_org.copy()
# list_copy=list(list.org)
# list_copy=list_org[:]
list_copy.append("lemon")
print(list_org)
print(list_copy)

'''list comprehension'''
A = [1, 2, 3, 4, 5, 6]
B = [i*i for i in A]

print(A)
print(B)

# TUPLES: ORDERED,IMMUTABLE,ALLOWS DUPLICATE ELEMENTS
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

item = mytuple[-1]
for i in mytuple:
    print(i)

if 'Max' in mytuple:
    print("yes")
else:
    print("no")

print(len(mytuple))

a = [1, 2, 3, 4, 5,  6, 7, 8, 9, 10]
b = a[len(a)-1::-2]
print(b)

my_tuple = [0, 1, 2, 3, 4]
*i1, i2, i3 = my_tuple

print(i1)
print(i3)
print(i2)

print(sys.getsizeof(my_tuple), "bytes")
# timeit.time(stmt="[0,1,2,3,4,5",number=1000)
# working with tuples can be more efficient than lists

# tuples can be used in dictionary as key but lists cannot

# SETS:
myset = set("Hellopython")
my_set = {1, 2, 3, 4}
# unordered,mutable,no duplicates
print(myset)
my_set.add(6)
my_set.remove(2)
myset.discard(8)
my_set.add(5)
print(my_set)
odds = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8}
a = odds.union(even)
# a=odds.intersection(even) will be empty
print(a)
seta = {1, 2, 3, 5, 6, 8}
setb = {1, 2, 3, 9, 11, 13}
diff = seta.difference(setb)
print(diff)

# symmetric_difference will remove common elements of both sets and return te rest of the elements, update,intersection_update,diff_update,symmetric_difference_update

print(seta.issubset(setb))
print(seta.issuperset(setb))
seta.update(setb)
print(seta.issuperset(setb))
# if we do assignment like seta=setb both will change simultaneously..instead setb=seta.copy()

# frozenset is immutable version of normal set
x = frozenset([1, 2, 3, 4, 5])
# x.remove(1)-error

# STRINGS
my_string = "I'm a programmer"
print(my_string)

# strings are immutable..
substring = my_string[0:9:2]
print(my_string[::-1])
print(substring)

mystr = '  HELLO WORLD  '
mystr = mystr.strip()  # removes white space
print(mystr)

# find,replace,count,startswith,endswith
x = my_string.split()
print(x)

newstring = '  '.join(x)
print(newstring)

my_list = ['a'] * 1000000


# bad method to join
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()

print(stop-start)

# good method to join:
start = timer()
my_string = ''.join(my_list)
stop = timer()

print(stop-start)

# %,.format(),f-strings

var = "Amogh"
my_str = "The variable is %s" % var
# if number then %d, if float then %f
# by default 6 digits..can do %.2f for 2 digits

print(my_str)

mystring = "the variable is {:.3s}".format(var)
print(mystring)
my = f"the variable is {var}"
print(my)
"""
# COLLECTIONS-counter,,namedtuple,ordereddict,defaultdict,deque

from collections import Counter
a = "abcdeee"
my_counter = Counter(a)
print(my_counter)
print(max(my_counter.values()))

keys = my_counter.keys()
for i in keys:
    print(i)

print(my_counter)
print(my_counter.most_common(2))


Point = namedtuple('Point', 'x,y')
pt = Point(1, -2)
print(pt.x, pt.y)


ordered_dict = OrderedDict()

ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1

print(ordered_dict)


d = defaultdict(float)
d['a'] = 1.54
d['b'] = 2
print(d['a'])


de = deque()
de.append(1)
de.append(2)
print(de)
de.appendleft(3)
print(de)


de.pop()
for i in de:
    print(i)

de.extend([4, 5, 6])
print(de)
de.rotate(1)
# de.rotate(-1)--rotate all elements to the left

print(de)


d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
# extend,extendleft,popleft,pop,rotate

# EXCEPTIONS::

"""
a = 5
print(a)
# syntax error like print(a))

a = 5+'10'  # type error

#import error

a = 5
b = c
# name error..c not defined

f = open('somefile.txt')
# filenotfound error

a = [1, 2, 3]
a.remove(1)
a.remove(4)
# value error
# index error:accessing wrong index
diction = {'name': 'max'}
diction['age']  # key error

x = -5
if x < 0:
    raise exception('x should be positive')

assert(x>=0) #assertion error

try:
    a=5/0
except exception as e:
    print(e)
"""


class valuetoohigherror(Exception):
    pass


def test_value(x):
    if x > 100:
        raise valuetoohigherror('Value is too high')


try:
    test_value(101)
except valuetoohigherror as e:
    print(e)

# iterators:products,permutations,combinations,accumulations,groupby and infinite iterators


a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

"""
a = [1, 3, 4]

perm = permutations(a, 2)
print(list(perm))

a = [1, 2, 3, 3, 5]
comb = combinations(a, 5)
print(list(comb))
perm_2 = permutations(a)
print(list(perm_2))

"""
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# accumulate gives sum of each element with previous sum
# if acc=accumulate(a, func=operator.mul)

a = [1, 2, 3, 4]


n = int(input("Enter the previous sum sequence length:"))
a = [int(i) for i in range(n)]
print(list(accumulate(a)))


def smaller_three(x):
    return x < 3


persons = [{'name': 'tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'lisa', 'age': 27}, {'name': 'claire', 'age': 28}]
group_ob = groupby(persons, key=lambda x: x['age'])

for key, value in group_ob:
    print(key, list(value))

"""


for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3, 4]
for i in cycle(a):
    print(i)

"""
for i in repeat(1, 4):
    print(i)
