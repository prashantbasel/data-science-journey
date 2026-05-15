studnet = {
    "name": "Prashant",
    "age": 21,
    "course":"Data Science",
    "gpa": 3.5
}


print(studnet)
print(studnet["name"])
print(studnet["gpa"])

# Add a new key 
studnet["university"] = "Whitecliffe" 
print(studnet)


# Update existing key
studnet["gpa"]= 3.8
print(studnet)

# delete a key

del studnet["age"]
print(studnet)