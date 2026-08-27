# Markdown Components

> Use Markdown components to help you structure your content, with the help of Nuxt UI.

Prose components are replacements for HTML typography tags. They provide a simple way to customize your UI when using Markdown.

**Docus and Nuxt UI** provides a set of styled and beautiful prose components to help you write your documentation using the [MDC syntax](https://content.nuxt.com/docs/files/markdown#mdc-syntax).

<prose-note to="https://ui.nuxt.com/getting-started">

This page highlights only the prose components best suited for writing documentation. However, you can use **any Nuxt UI component** in your Markdown. For the full list of available components, visit the Nuxt UI documentation.

</prose-note>

### `Accordion`

Use the `accordion` and `accordion-item` components to display an [Accordion](https://ui.nuxt.com/components/accordion) in your content.

<tabs>
<tabs-item icon="i-lucide-eye" label="Preview">
<accordion>
<accordion-item icon="i-lucide-circle-help" label="What is Docus and what are its key features??">

Docus is a fully integrated documentation solution built with Nuxt UI. It's a theme based on the UI documentation template that provides a ready-to-use visual. User can focus on content using Markdown and MDC syntax.

</accordion-item>

<accordion-item icon="i-lucide-circle-help" label="How do I get started with Docus?">

The only thing you need to start a Docus project is a `content/` folder. You can have a check at the starter for a quick start.

</accordion-item>

<accordion-item icon="i-lucide-circle-help" label="What is Nuxt UI?">

[Nuxt UI](https://ui.nuxt.com/) is a collection of premium Vue components, composables and utils.

</accordion-item>
</accordion>
</tabs-item>

<tabs-item icon="i-lucide-code" label="Code">

```mdc
::accordion

  :::accordion-item{label="What is Docus and what are its key features??" icon="i-lucide-circle-help"}
  Docus is a fully integrated documentation solution built with Nuxt UI. It's a theme based on the UI documentation template that provides a ready-to-use visual. User can focus on content using Markdown and MDC syntax.
  :::

  :::accordion-item{label="How do I get started with Docus?" icon="i-lucide-circle-help"}
  The only thing you need to start a Docus project is a `content/` folder. You can have a check at the starter for a quick start.
  :::

  :::accordion-item{label="What is Nuxt UI ?" icon="i-lucide-circle-help"}
  [Nuxt UI](https://ui.nuxt.com/) is a collection of premium Vue components, composables and utils.
  :::
::
```

</tabs-item>
</tabs>

### `Badge`

Use markdown in the default slot of the `badge` component to display a [Badge](https://ui.nuxt.com/components/badge) in your content.

<tabs>
<tabs-item icon="i-lucide-eye" label="Preview" className="my-5">
<badge>

**v3.0.0**

</badge>
</tabs-item>

<tabs-item icon="i-lucide-code" label="Code">

```mdc
::badge
**v3.0.0**
::
```

</tabs-item>
</tabs>

### `Callout`

Use markdown in the default slot of the `callout` component to add eye-catching context to your content.

Use the `icon` and `color` props to customize it. You can also pass any property from the [`<NuxtLink>`](https://nuxt.com/docs/api/components/nuxt-link) component.

You can also use the `note`, `tip`, `warning` and `caution` shortcuts with pre-defined icons and colors.

<tabs>
<tabs-item icon="i-lucide-eye" label="Preview" className="my-5">
<div className="flex,flex-col,gap-4,w-full">
<note className="w-full,my-0">

Here's some additional information for you.

</note>

<tip className="w-full,my-0">

Here's a helpful suggestion.

</tip>

<warning className="w-full,my-0">

Be careful with this action as it might have unexpected results.

</warning>

<caution className="w-full,my-0">

This action cannot be undone.

</caution>
</div>
</tabs-item>

<tabs-item icon="i-lucide-code" label="Code">

```mdc
::note
Here's some additional information.
::

::tip
Here's a helpful suggestion.
::

::warning
Be careful with this action as it might have unexpected results.
::

::caution
This action cannot be undone.
::
```

</tabs-item>
</tabs>

### `Card` and `CardGroup`

Use markdown in the default slot of the `card` component to highlight your content.

Use the `title`, `icon` and `color` props to customize it. You can also pass any property from the [`<NuxtLink>`](https://nuxt.com/docs/api/components/nuxt-link).

Wrap your `card` components with the `card-group` component to group them together in a grid layout.

<tabs>
<tabs-item icon="i-lucide-eye" label="Preview" className="my-5">
<card-group className="w-full,my-0">
<card icon="i-simple-icons-github" target="_blank" title="Dashboard" to="https://github.com/nuxt-ui-templates/dashboard">

A dashboard with multi-column layout.

</card>

<card icon="i-simple-icons-github" target="_blank" title="SaaS" to="https://github.com/nuxt-ui-templates/saas">

A template with landing, pricing, docs and blog.

</card>

<card icon="i-simple-icons-github" target="_blank" title="Docs" to="https://github.com/nuxt-ui-templates/docs">

A documentation with `@nuxt/content`.

</card>

<card icon="i-simple-icons-github" target="_blank" title="Landing" to="https://github.com/nuxt-ui-templates/landing">

A landing page you can use as starting point.

</card>
</card-group>
</tabs-item>

<tabs-item icon="i-lucide-eye" label="Preview" className="my-5">

```mdc
:::card-group

  ::card
  ---
  title: Dashboard
  icon: i-simple-icons-github
  to: https://github.com/nuxt-ui-templates/dashboard
  target: _blank
  ---
  A dashboard with multi-column layout.
  ::

  ::card
  ---
  title: SaaS
  icon: i-simple-icons-github
  to: https://github.com/nuxt-ui-templates/saas
  target: _blank
  ---
  A template with landing, pricing, docs and blog.
  ::

  ::card
  ---
  title: Docs
  icon: i-simple-icons-github
  to: https://github.com/nuxt-ui-templates/docs
  target: _blank
  ---
  A documentation with `@nuxt/content`.
  ::

  ::card
  ---
  title: Landing
  icon: i-simple-icons-github
  to: https://github.com/nuxt-ui-templates/landing
  target: _blank
  ---
  A landing page you can use as starting point.
  ::

:::
```

</tabs-item>
</tabs>

### `Collapsible`

Wrap your content with the `collapsible` component to display a [Collapsible](https://ui.nuxt.com/components/collapsible) in your content.

<tabs>
<tabs-item icon="i-lucide-eye" label="Preview" className="my-5">
<collapsible>
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
</collapsible>
</tabs-item>

<tabs-item icon="i-lucide-code" label="Code">

```mdc
::collapsible

| Prop    | Default   | Type                     |
|---------|-----------|--------------------------|
| `name`  |           | `string`{lang="ts-type"} |
| `size`  | `md`      | `string`{lang="ts-type"} |
| `color` | `neutral` | `string`{lang="ts-type"} |

::
```

</tabs-item>
</tabs>

### `Field` and `FieldGroup`

A `field`is a prop or parameter to display in your content. You can group them by `field-group` in a list.

<tabs>
<tabs-item icon="i-lucide-eye" label="Preview" className="my-5">
<field-group className="my-0">
<field name="analytics" type="boolean">

Default to `false` - Enables analytics for your project (coming soon).

</field>

<field name="blob" type="boolean">

Default to `false` - Enables blob storage to store static assets, such as images, videos and more.

</field>

<field name="cache" type="boolean">

Default to `false` - Enables cache storage to cache your server route responses or functions using Nitro's `cachedEventHandler` and `cachedFunction`

</field>

<field name="database" type="boolean">

Default to `false` - Enables SQL database to store your application's data.

</field>
</field-group>
</tabs-item>

<tabs-item icon="i-lucide-code" label="Code">

```mdc
::field-group
  ::field{name="analytics" type="boolean"}
    Default to `false` - Enables analytics for your project (coming soon).
  ::

  ::field{name="blob" type="boolean"}
    Default to `false` - Enables blob storage to store static assets, such as images, videos and more.
  ::

  ::field{name="cache" type="boolean"}
    Default to `false` - Enables cache storage to cache your server route responses or functions using Nitro's `cachedEventHandler` and `cachedFunction`
  ::

  ::field{name="database" type="boolean"}
    Default to `false` - Enables SQL database to store your application's data.
  ::
::
```

</tabs-item>
</tabs>

### `Icon`

Use the `icon` component to display an [Icon](https://ui.nuxt.com/components/icon) in your content.

<code-preview>
<icon name="i-simple-icons-nuxtdotjs">



</icon>

<template v-slot:code="">

```mdc
:icon{name="i-simple-icons-nuxtdotjs"}
```

</template>
</code-preview>

### `Kbd`

Use the `kbd` component to display a [Kbd](https://ui.nuxt.com/components/kbd) in your content.

<code-preview>
<template v-slot:code="">

```mdc
:kbd{value="meta"} :kbd{value="K"}
```

</template>
</code-preview>

### `Tabs`

Use the `tabs` and `tabs-item` components to display [Tabs](https://ui.nuxt.com/components/tabs) in your content.

<code-preview>
<tabs className="w-full">
<tabs-item icon="i-lucide-code" label="Code">

```mdc
::callout
Lorem velit voluptate ex reprehenderit ullamco et culpa.
::
```

</tabs-item>

<tabs-item icon="i-lucide-eye" label="Preview">
<callout>

Lorem velit voluptate ex reprehenderit ullamco et culpa.

</callout>
</tabs-item>
</tabs>

<template v-slot:code="">

```mdc
::tabs{.w-full}
  :::tabs-item{icon="i-lucide-code" label="Code"}
    ```mdc
    ::::callout
    Lorem velit voluptate ex reprehenderit ullamco et culpa.
    ::::
    ```
  ::::

  :::tabs-item{icon="i-lucide-eye" label="Preview"}
    :::::callout
    Lorem velit voluptate ex reprehenderit ullamco et culpa.
    :::::
  :::
::
```

</template>
</code-preview>

### `Steps`

Wrap your headings with the Steps component to display a list of steps.

Use the `level` prop to define which heading will be used for the steps.

<tabs>
<tabs-item icon="i-lucide-eye" label="Preview" className="my-5">
<steps level="4">

#### Start a fresh new project

```bash [Terminal]
npm create nuxt@latest -- -t github:nuxt-content/docus
```

#### Run docus CLI to run your dev server

```bash [Terminal]
docus dev
```

</steps>
</tabs-item>

<tabs-item icon="i-lucide-code" label="Code">

```mdc
::steps{level="4"}
  #### Start a fresh new project
  
  ```bash [Terminal]
  npm create nuxt@latest -- -t github:nuxt-content/docus
  ```
  
  #### Run docus CLI to run your dev server
  
  ```bash [Terminal]
  docus dev
  ```
::
```

</tabs-item>
</tabs>
