<script lang="ts">
    export let picture: string
    export let name: string
</script>

<div class="w-1/2 bg-white rounded-md shadow-md  mx-2">
<figure >
    <img src="{picture}" alt="{name}" class="rounded-t-md">
    <figcaption class="py-4 px-2"><div class="flex justify-between items-center"><h3 class="text-base">{name} </h3><button class="bg-primary w-20 text-white rounded-md p-2 text-xs ">Découvrir</button></div></figcaption>
</figure>
</div>