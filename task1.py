
slices = party_pizza_mini + large + medium
print(f"Total Number of Slices: {slices}")

people += 1
share = slices // people
leftover = slices % people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")

people += 2 #Eric and Brandon are coming too.
share = slices // people
leftovers = slices % people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftovers}") 


slices += party_pizza_mini
share = slices // people
leftovers = slices % people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftovers}")
print("...for Mr. Hollow Leg")
