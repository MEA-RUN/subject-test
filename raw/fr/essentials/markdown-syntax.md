# Markdown Syntax

> Text, title, and styling in standard markdown.

## Titles

Use titles to introduce main sections. They structure your documentation and help users navigate content.

<code-preview className="[&>div]:*:my-0">

## Titles

<template v-slot:code="">

```mdc
## Titles
```

</template>
</code-preview>

### Subtitles

Use subtitles to divide sections further. They create a more detailed content hierarchy for better readability.

<code-preview className="[&>div]:*:my-0">

### Subtitles

<template v-slot:code="">

```mdc
### Subtitles
```

</template>
</code-preview>

<tip>

Each title and subtitle creates an anchor and shows up automatically in the table of contents.

</tip>

## Text Formatting

Docus supports most Markdown formatting options.

<table>
<thead>
  <tr>
    <th>
      Style
    </th>
    
    <th>
      How to use
    </th>
    
    <th>
      Result
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Bold
    </td>
    
    <td>
      <code>
        **bold**
      </code>
    </td>
    
    <td>
      <strong>
        Bold
      </strong>
    </td>
  </tr>
  
  <tr>
    <td>
      Italic
    </td>
    
    <td>
      <code>
        *italic*
      </code>
    </td>
    
    <td>
      <em>
        Italic
      </em>
    </td>
  </tr>
  
  <tr>
    <td>
      Strike
    </td>
    
    <td>
      <code>
        ~~strike~~
      </code>
    </td>
    
    <td>
      <del>
        Strike
      </del>
    </td>
  </tr>
</tbody>
</table>

Combine formatting for richer text styles and visual emphasis.

<table>
<thead>
  <tr>
    <th>
      Style
    </th>
    
    <th>
      How to use
    </th>
    
    <th>
      Result
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Bold Italic
    </td>
    
    <td>
      <code>
        **_bold italic_**
      </code>
    </td>
    
    <td>
      <em>
        <strong>
          Bold Italic
        </strong>
      </em>
    </td>
  </tr>
  
  <tr>
    <td>
      Bold Strike
    </td>
    
    <td>
      <code>
        ~~**bold**~~
      </code>
    </td>
    
    <td>
      <del>
        <strong>
          Bold
        </strong>
      </del>
    </td>
  </tr>
  
  <tr>
    <td>
      Italic Strike
    </td>
    
    <td>
      <code>
        ~~*italic*~~
      </code>
    </td>
    
    <td>
      <del>
        <em>
          Italic
        </em>
      </del>
    </td>
  </tr>
</tbody>
</table>

## Links

Links connect different parts of your documentation and external resources, essential for user navigation and providing references.
To create a link, wrap the link text in brackets `[]()`.

<code-preview className="[&>div]:*:my-0">

[Nuxt UI](https://ui.nuxt.com/getting-started/installation/nuxt)<template v-slot:code="">

```mdc
[Nuxt UI](https://ui.nuxt.com/getting-started/installation/nuxt)
```

</template>
</code-preview>

### Internal links

For linking within your documentation, use root-relative paths like `/getting-started/installation`.

<code-preview className="[&>div]:*:my-0">

[Installation](/getting-started/installation)<template v-slot:code="">

```mdc
[Installation](/getting-started/installation)
```

</template>
</code-preview>

## Lists

Organize related items in a structured, readable format. Markdown supports unordered, ordered, and nested lists for various content needs.

### Unordered

Use unordered lists for items without a specific sequence. Start each item with a `-` symbol.

<code-preview className="[&>div]:*:my-0">

- I'm a list item.
- I'm another list item.
- I'm the last list item.

<template v-slot:code="">

```mdc
- I'm a list item.
- I'm another list item.
- I'm the last list item.
```

</template>
</code-preview>

### Ordered

Use ordered lists when item order matters, like steps in a process. Start each item with a number.

<code-preview className="[&>div]:*:my-0">

1. I'm a list item.
2. I'm another list item.
3. I'm the last list item.

<template v-slot:code="">

```mdc
1. I'm a list item.
2. I'm another list item.
3. I'm the last list item.
```

</template>
</code-preview>

### Nested

Create hierarchical lists with sub-items for complex structures. Indent sub-items by four spaces for nesting.

<code-preview className="[&>div]:*:my-0">

- I'm a list item.

  - I'm a nested list item.
  - I'm another nested list item.
- I'm another list item.

<template v-slot:code="">

```mdc
- I'm a list item.
  - I'm a nested list item.
  - I'm another nested list item.
- I'm another list item.
```

</template>
</code-preview>

## Tables

Present structured data in rows and columns clearly. Tables are ideal for comparing data or listing properties.

<code-preview className="[&>div]:*:my-0,[&>div]:*:w-full">
<table>
<thead>
  <tr>
    <th>
      Prop
    </th>
    
    <th>
      Default
    </th>
    
    <th>
      Type
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        size
      </code>
    </td>
    
    <td>
      <code>
        md
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        color
      </code>
    </td>
    
    <td>
      <code>
        neutral
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
  </tr>
</tbody>
</table>

<template v-slot:code="">

```mdc
| Prop    | Default   | Type                     |
|---------|-----------|--------------------------|
| `name`  |           | `string`{lang="ts-type"} |
| `size`  | `md`      | `string`{lang="ts-type"} |
| `color` | `neutral` | `string`{lang="ts-type"} |
```

</template>
</code-preview>

## Blockquotes

Highlight important quotations, citations, or emphasized text. Blockquotes visually distinguish quoted content.

### Singleline

Single-line blockquotes are best for short, impactful quotes or citations that fit within a single line. To create a single-line blockquote, add a `>` in front of a paragraph. Ideal for short and impactful quotes.

<code-preview className="[&>div]:*:my-0">

> Nuxt UI is a collection of Vue components, composables and utils built on top of Reka UI, oriented on structure and layout and designed to be used as building blocks for your app.

<template v-slot:code="">

```mdc
> Nuxt UI is a collection of Vue components, composables and utils built on top of Reka UI, oriented on structure and layout and designed to be used as building blocks for your app.
```

</template>
</code-preview>

### Multiline

Multi-line blockquotes are suitable for longer quotes or when you need to include multiple paragraphs within a single quotation.

<code-preview className="[&>div]:*:my-0">

> Nuxt UI is a collection of Vue components, composables and utils built on top of Reka UI, oriented on structure and layout and designed to be used as building blocks for your app.
> 
> Create beautiful, responsive, and accessible Vue applications with Nuxt UI.

<template v-slot:code="">

```mdc
> Nuxt UI is a collection of Vue components, composables and utils built on top of Reka UI, oriented on structure and layout and designed to be used as building blocks for your app.
>
> Create beautiful, responsive, and accessible Vue applications with Nuxt UI.
```

</template>
</code-preview>
