slices = int(input("How many slices?"))
students = int(input("How many students?"))
slicesPerPerson = slices//students
extra = slices%students
print("Each student gets " + str(slicesPerPerson) + " slices, and there will be " + str(extra) + " extra slice(s).")
