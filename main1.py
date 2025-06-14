import turtle

# Create turtle object
t = turtle.Turtle()

# Set speed (1 = slow, 10 = fast, 0 = instant)
t.speed(2)

# Draw a square
for _ in range(4):
    t.forward(100)   # Move forward by 100 units
    t.right(90)      # Turn right by 90 degrees

# Close window on click
turtle.done()
