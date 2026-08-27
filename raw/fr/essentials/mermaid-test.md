# Mermaid Diagrams Test

This page demonstrates how to use Mermaid diagrams in your markdown content.

## Simple Flowchart

```mermaid
graph TD
    A[Start] --> B{Is it working?}
    B -->|Yes| C[Great!]
    B -->|No| D[Debug]
    D --> B
    C --> E[End]
```

## Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant Server
    User->>Browser: Click button
    Browser->>Server: Send request
    Server-->>Browser: Return data
    Browser-->>User: Display result
```

## Class Diagram

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +eat()
        +sleep()
    }
    class Dog {
        +String breed
        +bark()
    }
    class Cat {
        +String color
        +meow()
    }
    Animal <|-- Dog
    Animal <|-- Cat
```

## Regular Code Block (for comparison)

```javascript
// This is regular JavaScript code
function hello() {
  console.log('Hello, world!')
}
```
