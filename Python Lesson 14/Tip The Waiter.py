def total_calc(bill_amount, tip_perc):
    #define function to calculate the tip on bill
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 6)
    print(f"The total amount to pay is: cedis {total}")

total_calc(500, 8)
