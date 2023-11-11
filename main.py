print()

mass = float(input("Enter the mass in grams: "))
volume = float(input("Enter the volume in cubic centimeters: "))

density = mass / volume
print(f"\nThe density is {density} grams per cubic centimeter.")

density_water = 1
print(f"\nWater has a density of {density_water} gram per cubic centimeter.")

if density < density_water:
  print("It will float in water.")
else:
  print("It will sink in water.")
