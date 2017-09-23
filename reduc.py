#Gets a fraction from the user
a = int(input("Choose a Numerator: "))
b = int(input("Choose a Denominator: "))

#Variable / Dependcy creation
if(a > b):
    max = a
    min = b
else:
    max = b
    min = a

#Finds the GCF
while(min != 0):
    reduc = (max % min)
    print(max)
    print(min + "\n")
    max = min
    min = reduc
GCF = max

print("\nThe GCF is " + str(GCF) + " for\n" + str(a) + "\n" + "-"*len(str(b)) + "\n" + str(b))

a = int(a/GCF)
b = int(b/GCF)

print("\nTherefore the reduced fraction is:\n" + str(a) + "\n" + "-"*len(str(b)) + "\n" + str(b))
