#################################################
##
##  Basic R code examples
 
   
    
###### data types #########################################
 
### integer and double
 
# this is by default a double
x = 9
typeof(x)
 
x <- 9L
typeof(x)
 
x = 9
typeof(x)

# default operations work between integers and doubles
9 + 9.
7/3
7/3.
x/y

12 %% 7
12 %/%  7
 
#### character
 
x = "longhow"
typeof(x)
 
paste0("longhow", "lam")
 
library(stringr)
str_sub(x, 3, 6)
str_toupper(x)
 
#### factor
s = c("F", "F", "F", "M", "M") %>% as.factor()
 
##### data structures ############################
 
#### vectors
x = c(1, 2, 3, 4, 5)
x

# indices in R beginnen bij 1
x[1] 
 
# elementsgewijs operaties
x + 2*x
sin(x)


#### matrix
A = rbind(c(1,2,3), c(4,5,6), c(7,8,9))
A

## tweede rij tweede kolom
A[2,2]
## tweede rij
A[2,]
## kolommen 2 en 3
A[,2:3]

## matrix vermenigvuldigen: twee mogelijkheden 
A * A
A %*% A
 
#### list
a = list(1,2,3,4, "P")
 
b = list(1,2,3,4, list("a","b"))
 
released = list(
  "iphone" = 2007,
  "iphone 3G" = 2008,
  "iphone 3GS" = 2009,
  "iphone 4" = 2010,
  "iphone 4S" = 2011,
  "iphone 5" = 2012
)
 
## nested lists
test = list(
  "iphone" = 2007,
  "iphone 3G" = 2008,
  "iphone 3GS" = 2009,
  B = list(1,2,3,4),
  released
)
 
#### data frames
df = data.frame(
  id = c(1,2,3),
  col = c('red', 'blue', 'red'),
  leeftijd = c(56, 34, 78)
)
df

## kolommen in df
names(df)

df$id
df$col[2]
df[c("col", "leeftijd")]

df$temp = df$leeftijd * 12


### overview van kolomen met wat statistieken
summary(df)