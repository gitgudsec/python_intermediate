# a collection type that is: unordered, mutable, does NOT allow duplicates (disting. charac.)
# same curly braces as dict, but does not contain key:values just single entries

myset = {1, 6, 9, 13, 26, 69, 420, 666}
print(myset)

# if we have copies of an item in a list, only one will be interpreted as beign in set
myset = {1, 6, 9, 13, 26, 69, 420, 666, 6, 9, 13, 26, 69}
print(myset)

# we can use function to turn a word into a set, each UNIQUE letter will be processed as a single entry in set, and reorders ARBITRARILY
newset1 = set("rexkwondo")
print(newset1)
# output: {'d', 'o', 'n', 'w', 'k', 'r', 'e', 'x'}
# how many entries?
print(len(newset1))

# check to see if something is present or not
if 'x' in newset1: print("Present")
else: print("Not present")

if 'p' in newset1: print("Present")
else: print("Not present")

# add elements
import string
for letter in string.ascii_lowercase:
    newset1.add(letter)
 
print(newset1)

# remove elements
import string

for letter in string.ascii_lowercase:
    if letter == 'm':
        break
    newset1.remove(letter)

print(newset1)

# clear() will empty the set, pop() removes last one which is arbitrary

# iterate over the list:
for i in newset1:
    print(str(i)+" has the ASCII code "+str(ord(i)))

# union combines
newset2 = set("chimmychangas")
newset3 = set("tatertots")
comb_set = newset3.union(newset2)
print(comb_set)

# intersection only keeps those that are common across both sets
newset2 = set("chimmychangas")
newset3 = set("tatertots")
int_set = newset3.intersection(newset2)
print(int_set)

# difference of two sets - will return all elements from 2 that are not in 3 
newset2 = set("cagefighter")
newset3 = set("starla")
diff = newset2.difference(newset3)
print(diff)

# everything in 3 that are not in 2
diff2 = newset3.difference(newset2)
print(diff2)

# everything that is present in both will not be shown
diff3 = newset3.symmetric_difference(newset2)
print(diff3)

# update will add everything that is not already present - no duplicattion
newset2.update(newset3)
print(newset2)

# subsets and supersetps
print(newset2.issubset(newset3))
newset4 = set("rex")
newset5 = set("rexkwondo")
print(newset4.issubset(newset5))

print(newset3.issuperset(newset2))
print(newset5.issuperset(newset4))

# disjoint returns true if there are NO characters in common
newset6 = set("rex")
newset7 = set("napoleon") # 6 and 7 share e
newset8 = set("kip") # 6 and 8 have nothing in common

print(newset6.isdisjoint(newset7))
print(newset6.isdisjoint(newset8))

# a FROZEN SET is a set that is IMMUTABLE
freezeme = frozenset([1, 2, 3, 6, 9])
print(freezeme)
