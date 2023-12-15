<script lang="ts">
    import { onMount } from 'svelte';
    export let picture: string
    export let name: string
    let datas = []
    const api = 'https://shuhado.alwaysdata.net/django/api/v1/event/'

    async function fetchData(){
    
    try{
        const resp = await fetch(api)
        const data:any = await resp.json()
        datas = data
        return data

    }catch(error){
        console.log(error)
    }
}
        onMount(async ()=>{
        fetchData()
    })

    function handleId(id:any){
    console.log("hey")
}
</script>

<div class="bg-primary-50 rounded-lg shadow-md">
<figure >
    <img loading="lazy" src="{picture}" alt="{name}" class="rounded-t-lg">
    <figcaption class="py-4 px-2"><div class="flex justify-between items-center"><h3 class="text-base">{name} </h3>
        <button class="bg-primary-300 hover:bg-primary-400 w-fit text-secondary rounded-lg p-3 text-sm font-semibold "on:click={() => handleId()}>Découvrir</button>
    </div></figcaption>
</figure>
</div>