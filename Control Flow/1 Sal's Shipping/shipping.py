weight = float(input('Enter the weight of your product: '))


# Ground Shipping
flat_charge_weight_ground = 20.00
ground_cost = 0
if weight < 0:
      print("Sorry! Weight can't be a negative number.")
elif weight <= 2 and weight >= 0:
      ground_cost += weight * 1.50 + flat_charge_weight_ground
elif weight >= 2 and weight <= 6:
      ground_cost += weight * 3.00 + flat_charge_weight_ground
elif weight >= 6 and weight <= 10:
      ground_cost += weight * 4.00 + flat_charge_weight_ground
elif weight >= 10:
      ground_cost += weight * 4.75 + flat_charge_weight_ground
else:
      print('Error. Try again.')

print("Ground Shipping Cost: $" + str(ground_cost))


# Premium Ground Shipping
ground_cost_premium = 125.00

print("Ground Shipping Premium Cost: $" + str( ground_cost_premium))


# Drone Shipping
flat_charge_weight_drone = 0.00
drone_cost = 0
if weight < 0:
      print("Sorry! Weight can't be a negative number.")
elif weight <= 2 and weight >= 0:
      drone_cost += weight * 5.50 + flat_charge_weight_drone
elif weight >= 2 and weight <= 6:
      drone_cost += weight * 9.00 + flat_charge_weight_drone
elif weight >= 6 and weight <= 10:
      drone_cost += weight * 12.00 + flat_charge_weight_drone
elif weight >= 10:
      drone_cost += weight * 14.75 + flat_charge_weight_drone
else:
      print('Error. Try again.')

print("Drone Shipping Cost: $" + str(drone_cost))