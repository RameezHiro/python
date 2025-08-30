d = {}  # Empty dictionary
print(type(d))


marks = {
   "Rameez": 100,
   "Aniket": 90,
   "Ash": 80,
    0:"Rameez"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Rameez": 99, "Greninja": 100})
# print(marks)

# print(marks.get("Rameez2")) # Prints None
# print(marks["Rameez2"])  #Returns an Error

# print(marks.pop("Ash"))

print(marks.popitem())
