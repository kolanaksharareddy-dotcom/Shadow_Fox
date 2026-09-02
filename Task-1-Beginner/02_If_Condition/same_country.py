city1 = input("Enter first city: ")
country1 = input("Enter first country: ")

city2 = input("Enter second city: ")
country2 = input("Enter second country: ")

if country1.lower() == country2.lower():
    print("Both cities are in the same country")
else:
    print("Both cities are in different countries")