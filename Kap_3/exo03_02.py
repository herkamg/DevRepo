# This first line is provided for you

shrs = input("Enter Hours:")
srates = input("Enter Rates:")
try:
    hrs = float(shrs)
    rates = float(srates)
except:
    print("Error, please enter numeric input")
    quit()

if hrs > 40:
    over_hrs = hrs - 40.
    over_rates = rates * 1.5
    Amount = float(40) * float(rates) + over_hrs * over_rates
else:
    Amount = float(hrs) * float(rates)

print(Amount)
