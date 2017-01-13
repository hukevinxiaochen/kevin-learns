# Handle missing values

# [tutorial](http://www.ats.ucla.edu/stat/r/faq/missing.htm)

# How are missing values handled by default in R?
getOption("na.action")

#------------------------------------------------------------
# Let's see all the different ways R can handle missing values.

# Start with a suitable data frame for demonstration purposes.
( g <- as.data.frame( matrix( c( 1:5, NA ), ncol=2 ) ) )

##   V1 V2
## 1  1  4
## 2  2  5
## 3  3 NA

#------------------------------
# See what happens when you
# pass the data frame to various 
# missing value handling functions.
na.omit(g) # removes observations if they contain missing values

##   V1 V2
## 1  1  4
## 2  2  5

na.exclude(g) # removes observations if they contain missing values

##   V1 V2
## 1  1  4
## 2  2  5

na.fail(g) # returns only if data frame contains no missing values

## Error: missing values in object

na.pass(g) # returns data frame unchanged

##   V1 V2
## 1  1  4
## 2  2  5
## 3  3 NA

