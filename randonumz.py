import random

# produces random float
a = random.uniform(1, 50)
print(a)

# produces integer
b = random.randint(10, 100)
print(b)

# variate using mu (mean) and sigma (std.deviation)
c = random.normalvariate(0, 1)
print(c)

#randomly draw from a list
mylist = list("ABCDEFGHIJKLMONPQRSTUVWXYZ")
print(mylist)

d = random.choice(mylist)
print(d)

# choose mulitple from list - unique
e = random.sample(mylist, 5)
print(e)

# choose mulitple from list - can reuse same element multiple times
f = random.choices(mylist, k=5)
print(f)

# shuffle list
random.shuffle(mylist)
print(mylist)

# all above was pseudo-randomness
# these will randomly choose first time but then value stays
# even if you rerun, value does not change after first run
# to rerun you have to reseed
# think of seed value as "set id"
# Obvs because these numbers stay the same don't use them for security purposes!

random.seed(1)
print(random.random())
print(random.randint(1, 69))

random.seed(2)
print(random.random())
print(random.randint(1, 69))

random.seed(3)
print(random.random())
print(random.randint(1, 69))

# let's explore the secrets module
import secrets

h = secrets.randbelow(100)
print(h)
 
# this is giving it a max capacity of 8 bits ie 11111111, ie 256 
i = secrets.randbits(8)
print(i)

# for arrays we use the numpy module
import numpy as np

k = np.random.rand(3) # 3 refers to dimensions
print(k)

j = np.random.randint(0, 10, 3, 3) # 3 x 3 array with ints between 0 and 10
print(j)