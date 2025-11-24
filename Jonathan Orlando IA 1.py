# Problem 1 - BMI

# Input (Ask the user to enter their weight/height in pounds/inches (imperial unit))
weight_pounds = float(input("Enter your weight in pounds: "))
height_inches = float(input("Enter your height in inches: "))

# Processing (Calculate BMI using the imperial formula: BMI = (weight / height^2) * 703)
# BMI using imperial units
bmi_imperial = weight_pounds / (height_inches ** 2) * 703

# Convert to metric
# Convert the weight from pounds to kilograms (1 pound = 0.453592 kg) and Convert height from inches to meters (1 inch = 0.0254 meters)
weight_kg = weight_pounds * 0.453592
height_meters = height_inches * 0.0254

# BMI using metric units (Calculate the BMI using the metric formula: BMI = weight / height^2)
bmi_metric = weight_kg / (height_meters ** 2)

# Output (Display the BMI calculated using imperial/metric units, rounded to 1 decimal place)
print("BMI (imperial):", round(bmi_imperial, 1))
print("BMI (metric):", round(bmi_metric, 1))


# Problem 2 - Vehicle Routing

# Local route (Calculate the distance for the Local route) Time = 1.00 hours, Speed = 30 mph
local_time = 1.00
local_speed = 30
local_distance = local_time * local_speed

# Parkway route (Calculate the distance for the Parkway route) Time = 0.88 hours, Speed = 40 mph
parkway_time = 0.88
parkway_speed = 40
parkway_distance = parkway_time * parkway_speed

# Highway route (Calculate the distance for the Highway route) Time = 0.87 hours, Speed = 55 mph
highway_time = 0.87
highway_speed = 55
highway_distance = highway_time * highway_speed

# Output (Display the distance for each route)
print("Local route distance:", local_distance, "miles")
print("Parkway route distance:", parkway_distance, "miles")
print("Highway route distance:", highway_distance, "miles")

# Determine the shortest route (Find the shortest distance among the three routes using the min() function)
shortest = min(local_distance, parkway_distance, highway_distance)

# Display the shortest route distance
print("Shortest route distance:", shortest, "miles")