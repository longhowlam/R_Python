######################################## 
##
## introductie code python

#### data stypes and structures

## integer and doubles 

x = 9

x = 9.
type(x)

x = 7
y = 2
x/y

12 % 7
12 // 7

## strings 
x = "longhow"
type(x)

"longhow" + "lam"

x.upper()
x[3:6]

## categorische data

import pandas as pd

s = pd.Series(["F","F","F","M", "M"], dtype="category")
s

#### data structures

## arrays (vectoren)
import numpy as np
x = np.array([1, 2, 3, 4, 5])
x
type(x)
x.mean()
x.max()

x[0]



x= (1,2,3,4,5)
x[2] = 9

## matrices

import numpy as np

A = np.array([ [1., 2, 3,6], [3, 4, 5,8]] )
A[1,1]

A = np.array([
  [1., 2, 3],
  [4., 5, 6],
  [7., 8, 9]
])
    
A
A[:,1]
A[1,:]
A[ [1,2],:]


## lists

l1 = [1,2,3,4, "p", ["a", "b"]]
l1

## dictionaries

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
	


## pandas data frames
import numpy as np
import pandas as pd
data = np.array([[ 5.8,2.8], [ "a", "b"]])
print(data)

#Creating pandas dataframe from numpy array
dataset = pd.DataFrame({'Column1':data[:,0],'Column2':data[:,1]})
print(dataset)



arr1 = np.array([2, 4, 6, 8])
arr2 = np.array(["a3", "a6", "qqq9", "qqq12"])
df_from_arr = pd.DataFrame(data=[arr1, arr2])
df =   df_from_arr.T

df.dtypes

######################

d = {'id': [1, 2,3], 'col': ['red', 'blue', 'red']}
df = pd.DataFrame(data=d)
df



