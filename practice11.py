def calculate_tax(salary):
    if salary > 5_000_000:
        return salary * 0.2
    else:
        return salary * 0.13

def calculate_net_salary(salary):
    return salary - calculate_tax(salary)


salary = 4_000_000

tax = calculate_tax(salary)
net_salary = calculate_net_salary(salary)

print(f"soliq : {tax:,.2f} so'm")
print(f"oylik: {net_salary:,.2f} so'm")