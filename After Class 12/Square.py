import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.left(90)     # Turn left by 90 degrees

# Keep the window open
turtle.done()