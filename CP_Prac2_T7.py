# Computing Practical 2 - Task 7

print("Miles\tKilometers\tKilometers\tMiles")

for miles in range(10):
    print("{0}\t{1:.3f}\t\t{2}\t\t{3:.3f}".format(miles + 1, (miles + 1) * 1.609, miles * 5 + 20, miles * 5 + 20 / 1.609))
