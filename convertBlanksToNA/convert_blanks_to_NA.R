# Run this lesson in the console using `source("convert_blanks_to_NA.R")`
# Suppose you have a data frame
print("Suppose you have a data frame")

df <- as.data.frame( c("Cheese", "", "Apple", "Barnacle", 
                       "Apple", "Barnacle", "Apple", "Apple") )

print(summary(df))

# We passed in a single character vector, which R data frames coerce into factors
print("The class of df[[1]] should be factor. It should print below:")
print(class(df[[1]]))

print("Notice that the levels include the empty character vector, \"\"")
print(levels(df[[1]]))

print("We can turn those into NA by using the following replacement syntax:")
print("`levels(df[[1]])[1] <- NA`")
print("Let's do that.")

levels(df[[1]])[1] <- NA

print("Now we see the levels again:")
print(levels(df[[1]]))

print("And finally the summary:")
print(summary(df))
