# Description: QAP 5 - Project 1A - A program for The One Stop Insurance Company to process a
# data file and create a detailed report - a policy listing.
# Author: Ellen Dalton
# Date: July 29, 2023

# Import required libraries:
import datetime
curr_date = datetime.datetime.now()

# Open the defaults file and read the values into variables
f = open('OSICDef.dat', 'r')

NEXT_POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_RATE = float(f.readline())
GLASS_COVERAGE_RATE = float(f.readline())
LOANER_COVERAGE_RATE = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())

f.close()

# Before the loop:

# Print headings
print()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTING AS OF {curr_date.strftime('%d-%b-%y')}")
print()
print(f"POLICY CUSTOMER", " "*15, "POLICY     INSURANCE     EXTRA      TOTAL")
print(f"NUMBER NAME", " "*20, "DATE       PREMIUM      COSTS     PREMIUM")
print("="*74)

# Initialize summary data
total_policies_ctr = 0
insurance_premium_acc = 0
extra_costs_acc = 0
total_premium_acc = 0

# Open the file
f = open("Policies.dat", "r")

for cust_data_line in f:
    # Inside the loop, read the record.
    cust_line = cust_data_line.split(",")

    policy_num = cust_line[0].strip()
    cust_first_name = cust_line[2].strip()
    cust_last_name = cust_line[3].strip()
    policy_date = cust_line[1].strip()
    insurance_premium = float(cust_line[14].strip())
    extra_liability = cust_line[10].strip()
    glass_coverage = cust_line[11].strip()
    loaner_car = cust_line[12].strip()
    num_cars_insured = int(cust_line[9].strip())

    # Do calculations.
    if extra_liability == "Y":
        extra_liability_cost = EXTRA_LIABILITY_RATE * num_cars_insured
    else:
        extra_liability_cost = 0.00

    if glass_coverage == "Y":
        glass_coverage_cost = GLASS_COVERAGE_RATE * num_cars_insured
    else:
        glass_coverage_cost = 0.00

    if loaner_car == "Y":
        loaner_car_cost = LOANER_COVERAGE_RATE * num_cars_insured
    else:
        loaner_car_cost = 0.00

    extra_costs = extra_liability_cost + glass_coverage_cost + loaner_car_cost

    total_premium = insurance_premium + extra_costs

    # Print the detail line.
    print(f"{policy_num}  {cust_first_name + ' ' + cust_last_name:<20s}    {policy_date}   ${insurance_premium:>8,.2f}"
          f"  ${extra_costs:>8,.2f}  ${total_premium:>8,.2f}")

    # Increment counters and accumulators
    total_policies_ctr += 1
    insurance_premium_acc += insurance_premium
    extra_costs_acc += extra_costs
    total_premium_acc += total_premium

# After the loop:
# Close the file
f.close()

# Print any summary data
print("="*74)
print(f"Total Policies: {total_policies_ctr:>3d}", " "*21, f"${insurance_premium_acc:>9,.2f} ${extra_costs_acc:>9,.2f} ${total_premium_acc:>9,.2f}")
print()





