
vol1 = float(input("Enter volume 1: "))
vol2 = float(input("Enter volume 2: "))
temp1 = float(input("Enter temperature 1: "))
temp2 = float(input("Enter temperature 2: "))

mixtemp = (vol1 * temp1 + vol2 * temp2) / (vol1 + vol2)
print("Mixture temperature is: ", mixtemp)
mixvol = vol1 + vol2
print("Mixture volume is: ", mixvol)



