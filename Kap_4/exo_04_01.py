# Write a program to prompt the user for hours and
# rate per hour using input to compute gross pay.

def computepay(h,r):
    if h<= 40 :
        pay = h *r
    else:
        over_hrs = h - 40
        over_rates = r * 1.5
        pay = (40 * r) + (over_hrs * over_rates)
    return pay

shrs = input("Enter Hours:")
srates = input("Enter rates:")
try:
    hrs = float(shrs)
    rates = float(srates)
except:
    print("please, enter numeric input")
    quit()
p = computepay(hrs,rates)
print("Pay",p)
