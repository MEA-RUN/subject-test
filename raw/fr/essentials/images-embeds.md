# Images and Embeds

> Add image, video, and other HTML elements

## Markdown

Display images or videos using standard Markdown syntax.

### Images

<code-preview>

![Nuxt Social Image](https://nuxt.com/new-social.jpg)<template v-slot:code="">

```mdc
![Nuxt Social Image](https://nuxt.com/new-social.jpg)
```

</template>
</code-preview>

Or with your local images

<code-preview>

![Snow-capped mountains in a sea of clouds at sunset](/mountains.webp)<template v-slot:code="">

```mdc
![Snow-capped mountains in a sea of clouds at sunset](/mountains.webp)
```

</template>
</code-preview>

<note to="https://image.nuxt.com/">

Docus will use `<NuxtImg>` component under the hood instead of the native `img` tag.

</note>

### Videos

<prose-code-preview>
<video :autoplay="true" :controls="true" :loop="true" src="https://res.cloudinary.com/dcrl8q2g3/video/upload/v1745404403/landing_od8epr.mp4">



</video>

<template v-slot:code="">

```mdc
:video{autoplay controls loop src="https://res.cloudinary.com/dcrl8q2g3/video/upload/v1745404403/landing_od8epr.mp4"}
```

</template>
</prose-code-preview>

###
