# 1. Define the angle in degrees
import math


angle_degrees = 45

# 2. Convert the angle to radians (math functions require radians)
angle_radians = math.radians(angle_degrees)

# 3. Calculate trigonometric values
sine_value = math.sin(angle_radians)
cosine_value = math.cos(angle_radians)
tangent_value = math.tan(angle_radians)

# 4. Display the results
print(f"Angle: {angle_degrees}°")
print(f"Sin: {sine_value:.4f}")
print(f"Cos: {cosine_value:.4f}")
print(f"Tan: {tangent_value:.4f}")