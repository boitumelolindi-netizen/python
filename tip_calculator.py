
meal = input("How much was the meal? ")
percent = input("What percentage would you like to tip? ") 

meal = meal[1:]
meal = float(meal)

percent = percent[:-1]
percent = float(percent)
percent = percent/100

tip = meal * percent

print(f"leave ${tip:.2f}" )