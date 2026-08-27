# Match the Shape Tutorial

Welcome to the interactive Python tutorial! This lesson uses the **Match the Shape** game to teach you fundamental programming concepts.

<prose-note>

The interactive tool will open automatically in the right panel. Use it to practice the concepts as you learn!

</prose-note>

## What You'll Learn

In this tutorial, you'll master:

- **Variables** - Storing and naming objects
- **Objects** - Understanding object-oriented programming
- **Methods** - Calling functions on objects
- **Sequences** - Understanding execution order
- **Method Chaining** - Combining multiple operations

## Getting Started

The Match the Shape game is an interactive Python environment where you control shapes on a grid using Python code.

### Creating Your First Shape

Let's create a simple square:

```python
s = shape.Square("red")
```

This creates a red square and stores it in the variable `s`.

### Positioning the Shape

Now let's place it on the grid:

```python
s.set_position(2, 3)
```

This puts the square at coordinates (2, 3) on the grid.

### Moving the Shape

You can move shapes using directional commands:

```python
s.forward(2)  # Move 2 spaces forward
s.right()     # Rotate 90° to the right
s.forward(1)  # Move 1 space forward
```

## Your First Challenge

Try this complete example in the tool on the right:

```python
# Create a blue circle
c = shape.Circle("blue")

# Position it at the starting point
c.set_position(1, 1)

# Move it to the destination
c.forward(3)
c.right()
c.forward(2)
```

<prose-tip>

Watch how the shape moves on the grid as you execute your code!

</prose-tip>

:::tools match
🎮 Open Interactive Game
:::

## Advanced Techniques

### Method Chaining

You can chain multiple methods together:

```python
s = shape.Square("green")
s.set_position(0, 0).forward(2).right().forward(1)
```

### Working with Multiple Shapes

Create and control multiple shapes:

```python
s1 = shape.Square("red")
s2 = shape.Circle("blue")
s3 = shape.Triangle("green")

s1.set_position(0, 0)
s2.set_position(1, 0)
s3.set_position(2, 0)
```

## Practice Exercises

Use the tool to complete these challenges:

1. **Beginner**: Create one shape and move it to its destination
2. **Intermediate**: Control 2 shapes simultaneously
3. **Advanced**: Master all 4 shapes and reach all destinations!

<prose-warning>

Remember: Each shape must have a unique combination of type and color!

</prose-warning>

## Tips for Success

- Plan your path before writing code
- Use the grid coordinates to calculate moves
- Rotate before moving in a new direction
- Test your code one shape at a time

## Next Steps

Once you've mastered the basics, try:

- Creating complex paths with multiple turns
- Optimizing your code to use fewer commands
- Using method chaining for cleaner code
- Exploring different shape and color combinations

Happy coding! 🎮🐍
