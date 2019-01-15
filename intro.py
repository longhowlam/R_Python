######################################## 
##
## introductie code python

#### data types ##############################

#### integer and doubles 

# this is by default a integer
x = 9

x = 9.
type(x)

x = 7
y = 2
x/y

12 % 7
12 // 7

#### strings 
x = "longhow"
type(x)

# strings can be added in python
"longhow" + "lam"

# string objects posses methods
x.upper()
x[3:6]

#### categorische data
import pandas as pd

s = pd.Series(["F","F","F","M", "M"], dtype="category")
s

#### data structures ######################################################

#### arrays (vectoren)
import numpy as np
x = np.array([1, 2, 3, 4, 5])
x
type(x)
x.mean()
x.max()

## indices in python beginnen bij 0
x[0]

# elementsgewijs operaties
x + 2*x
np.sin(x)

x[2] = 9

#### immutable tuples in python
x= (1,2,3,4,5)
x[2] = 9

#### matrices

import numpy as np
A = np.array([ [1., 2, 3,6], [3, 4, 5,8]] )

A = np.array([
  [1., 2, 3],
  [4., 5, 6],
  [7., 8, 9]
])
    
A
# rij 2 en kolom 2
A[1,1]
# kolom 2 
A[:,1]
# rij 2
A[1,:]

#rij 2 en 3
A[ [1,2],:]

## matrix vermenigvuldigen: twee mogelijkheden 
A*A
np.dot(A,A)

## lists
l1 = [1,2,3,4, "p", ["a", "b"]]
l1

#### dictionaries

released = {
	"iphone" : 2007,
	"iphone 3G" : 2008,
	"iphone 3GS" : 2009,
	"iphone 4" : 2010,
	"iphone 4S" : 2011,
	"iphone 5" : 2012
}

released["iphone 5"]
released["iphone 111"]

test = {
		"iphone" : 2007,
		"iphone 3G" : [1,2,3,4],
		"iphone 3GS" : released
}
	


#### pandas data frames
import numpy as np
import pandas as pd

## Creating pandas dataframe from numpy array
data = np.array([[ 5.8,2.8], [ "a", "b"]])
print(data)

dataset = pd.DataFrame({'Column1':data[0,:],'Column2':data[1,:]})
print(dataset)


##### data frame from dictionary

d = {
	'id': [1, 2,3], 
	'col': ['red', 'blue', 'red'],
	'leeftijd' : [56,34,78]
}
df = pd.DataFrame(data=d)
df

# kolommen in df
df.dtypes

df.id
df.col[2]

df[['col', 'leeftijd']]
