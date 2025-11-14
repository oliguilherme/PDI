def amount_salary(salary, increase) :
    return salary * (increase / 100)
        

salary = float(input("Salario: "))
before = salary
increase = 0

 
if (salary <= 2800) :
    increase = 20
elif (salary > 2800 and salary <= 7000) :
    increase = 15
elif (salary > 7000 and salary <= 15000) :
    increase = 10
else:
    increase = 5

amount = amount_salary(salary, increase)
after = before + amount

print(f"Antes: {before}\nTaxa de aumento: {increase}\nAumento: {amount}\nDepois: {after}")

