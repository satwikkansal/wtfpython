a=[11,22]
b=a
The ids of the two will be the same.
Now,
a[0]=1
The ids of the two will still be the same as both a and b are referring to the same location, changes made to a are made to b as well.
Hence,
a=[1,22]
b=[1,22]

Now if we do
import copy
c=copy.deepcopy(a)
id(a) will not be equal to id(c)
