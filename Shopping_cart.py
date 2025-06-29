foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy or q to quit: ")
    if food.lower()== 'q':
        break   
    else:
        price = float(input(f"Enter price of food: {food} : R"))
        foods.append(food)
        prices.append(price)
        
    print("-YOUR CART")
    
    for food in foods: 
        print(food, end= ",")
        
    for price in prices:
        total += price
        
    print("\n")  
    print(f"Total is: R{total:}")
    
        