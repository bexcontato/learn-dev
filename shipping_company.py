"""
Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

. Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
. Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
. Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

(price values from codecademy.com are written into the program and available at their website on the Python3 learning course)
"""
weight = 41.5
# Ground Shipping
flat_charge = 20
premium_charge = 125

if weight <= 2:
  price = weight * 1.50
elif weight > 2 and weight <= 6:
  price = weight * 3.00
elif weight > 6 and weight <= 10:
  price = weight * 4.00
elif weight > 10:
  price = weight * 4.75 

print("Ground Shipping:", weight, "lb(s), costs: $", price + flat_charge, "for regular shipping and $", price + premium_charge, "for premium shipping.")



 #Drone Shipping
if weight <= 2:
  price = weight * 4.50
elif weight > 2 and weight <= 6:
  price = weight * 9.00
elif weight > 6 and weight <= 10:
  price = weight * 12.00
elif weight > 10:
  price = weight * 14.25

print("Drone Shipping:", weight, "lb(s), costs: $", price, ".")
