# Interactive Tools Demo

This page demonstrates how to use the `:::tools` component to embed interactive tool buttons directly in your content.

## What are Tool Buttons?

Tool buttons allow you to create clickable buttons in your markdown that open specific interactive tools in the side panel. This is perfect for:

- Providing direct access to exercises
- Creating interactive learning experiences
- Offering hands-on practice opportunities
- Enhancing engagement with your content

## Basic Example

Here's a simple button that opens the Match the Shape game:

<tools id="match">

🎮 Open Match the Shape Game

</tools>

Click the button above to see it in action!

## How It Works

When you click a tool button:

1. The side panel opens automatically (if not already open)
2. The specified tool loads in the panel
3. You can interact with the tool while reading the content
4. The tool stays open as you navigate (until you close it)

## Use Cases

### 1. Practice Sections

After explaining a concept, provide immediate practice:

**Example: Python Variables**

Variables in Python are like labeled boxes that store values:

```python
# Create a variable
name = "Alice"
age = 25
```

Now try it yourself:

<tools id="match">

Try Creating Variables

</tools>

### 2. Multiple Tools

You can include multiple tool buttons for different exercises:

<tools id="match">

🐍 Python Exercise

</tools>

<tools id="code-editor">

💻 Code Editor

</tools>

<tools id="quiz">

📝 Take Quiz

</tools>

### 3. Inline with Content

Tool buttons work great inline with your explanations:

**Step 1**: Read the instructions
**Step 2**: Click the button → :::tools{id="match"}
Start Exercise
:::
**Step 3**: Complete the challenge

## Advanced Usage

### Custom Button Text

You can customize the button text to match your content:

:::tools match
🚀 Launch Interactive Tutorial
:::

:::tools match
Begin Shape Challenge
:::

:::tools match
Practice Now
:::

### With Callouts

Combine with other MDC components:

<prose-note>

Before starting, make sure you understand the basics of Python syntax.

:::tools match
Open Practice Environment
:::

</prose-note>

<prose-tip>

**Pro Tip**: Try to solve the puzzle with the minimum number of moves!

:::tools match
Start Challenge
:::

</prose-tip>

### In Lists

You can even use them in lists:

1. Read the lesson content
2. <tools id="match">

Open the interactive tool

</tools>
3. Complete the exercises
4. Move to the next lesson

## Best Practices

### ✅ Do:

- Use descriptive button text
- Place buttons near relevant content
- Include emojis for visual appeal
- Test that tool IDs are correct

### ❌ Don't:

- Use too many buttons on one page
- Use vague text like "Click here"
- Reference non-existent tools
- Place buttons in headings

## Styling Examples

### Primary Action

:::tools match
🎯 Start Main Exercise
:::

### Secondary Action

:::tools quiz
📊 Optional Quiz
:::

### With Icons

:::tools match
🎮 Game Mode
:::

:::tools code-editor
⌨️ Editor Mode
:::

:::tools quiz
✏️ Test Mode
:::

## Error Handling

If you specify a tool ID that doesn't exist, the button will show an error:

:::tools non-existent-tool
This Won't Work
:::

The error message helps you identify invalid tool IDs during development.

## Comparison with Frontmatter

There are two ways to use tools:

### Frontmatter (Page-Level)

```markdown
---
tool: match
---
```

- Opens automatically when page loads
- One tool per page
- Suited for dedicated tutorial pages

### Tool Buttons (Inline)

```markdown
:::tools match
Open Tool
:::
```

- Opens on button click
- Multiple tools per page
- Suited for reference pages with multiple examples

You can use both together!

## Complete Example

Here's a complete lesson using tool buttons:

---

### Lesson: Python Movement Commands

In this lesson, you'll learn how to move objects using Python code.

**Concept**: The `forward()` method moves an object in its current direction.

```python
shape.forward(3)  # Move 3 spaces
```

:::tools match
🎮 Try Forward Movement
:::

**Concept**: The `right()` method rotates an object 90° clockwise.

```python
shape.right()  # Rotate right
```

:::tools match
🎮 Try Rotation
:::

**Challenge**: Combine both to navigate a path!

:::tools match
🚀 Complete Challenge
:::

---

## Summary

The `:::tools` component is a powerful way to create interactive, engaging documentation. Use it to:

- ✅ Provide hands-on practice
- ✅ Create interactive tutorials
- ✅ Offer multiple learning tools
- ✅ Enhance user engagement

Happy teaching! 🎓
