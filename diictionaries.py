#We use them when we want to store information that comes as key value pairs

phone = input("Phone: ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"

}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)