
# Define an array
values =[1111, 2, "Serdar", 21.5]
print(values[0])
print(values[-1]) # prints the last item
print(values[1:4]) # prints the items between these indexes

values.insert(2,"New value") # inserts an item into list
print(values[1:4]) # prints the items between these indexes

values.append("Last entry") # adds an item to the end
print(values)

values[0]="Updated value"  #updae value
print(values)

del values[1] # delete second item
print(values)

# Tuple is the same as lists, but immutable. You cannot update values. Instead of square brackets, normal brackets used
valuesTuple=(11,"value",44.5)
print(valuesTuple[0]) # prints the value
#valuesTuple[0]=22   # but you cannot reassign a value
#print(valuesTuple) # this throws error


#Dictionary
print("****************************")
dic={"ab":2, 4:"bcd","e":"Hello World"}
print(dic["ab"])
print(dic[4])
print(dic["e"])

# Creating dictionaries at runtime
# First create an empty dictionary
dict={}
dict["FirstName"]="Rahul"  # When we run the program, it writes the following values at runtime
dict["LastName"]="Shetty"
print(dict)
print("Runtime values "+dict["FirstName"])













