<script lang="ts">
    export let picture: string
    export let name: string
</script>

<div class="w-1/3 bg-white rounded shadow-md">
<figure>
    <img src="{picture}" alt="{name}">
    <figcaption class="py-4 px-2"><div class="flex justify-between items-center"> {name || 'Bonjour toi'} <button class="bg-primary w-20 text-white rounded p-2 text-xs ">Voir</button></div></figcaption>
</figure>
</div>