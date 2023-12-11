<script lang="ts">

export let picture:string
export let name:string
export let description:string
export let price:string

</script>

<div class="w-1/4">
<figure>
    <img src="{picture}" alt="{name}">
    <figcaption>
        {@html description}
        <span>{price}</span>
    </figcaption>
</figure>
</div>