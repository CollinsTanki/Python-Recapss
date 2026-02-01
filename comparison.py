#if name is less than 3 characters long, then name must be at least 3 characters otherwise if it's more than 50 characters then name must be a maximum of 50 characters otherwise name looks good!
name = "john"
if len(name) < 3:
    print("Name must be more than 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")
