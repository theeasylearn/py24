'''
    write a program to calculate & display gross annual income, tax and net income from monthly given income as per below income tax rule 
    annual income                           Tax Rate
    Above Rs. 24,00,001	                    30%
    From Rs. 20,00,001 to Rs. 24,00,000	    25%
    From Rs. 16,00,001 to Rs. 20,00,000	    20%
    From Rs. 12,00,001 to Rs. 16,00,000	    15%
    below 12,00,000                          0%
    
    steps 
    1)  create variable monthly_income, tax, yearly_income,net_income
    2)  accept monthly income from user 
    3)  calculate annual income
        annual_income = monthly_income * 12
    4)  calculate tax 
        if annual_income above 24,00,001 then 
            tax = annual_income * 0.30
        else if annual_income above  20,00,001 then 
            tax = annual_income * 0.25
        else if annual_income above  16,00,001 then 
            tax = annual_income * 0.20
        else if annual_income above  12,00,001 then 
            tax = annual_income * 0.15
        else 
            tax = 0 
    5) calculate net income 
       net_income = annual_income - tax 
    6) display annual income, net income tax      
'''
#chain assignment technique
monthly_income = annual_income = tax = net_come = 0

monthly_income = int(input("Enter monthly income"))
annual_income = monthly_income * 12
if annual_income>2400001:
    tax = annual_income * 0.30
elif annual_income>2000001:
    tax = annual_income * 0.25
elif annual_income>1600001:
    tax = annual_income * 0.20
elif annual_income>1200001:
    tax = annual_income * 0.15
else: 
    tax = 0
net_income = annual_income - tax 
print(f"annual income = {annual_income} tax = {tax} net income = {net_income}")

