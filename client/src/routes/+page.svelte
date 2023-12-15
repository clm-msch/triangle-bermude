<script lang="ts">
    import { onMount } from 'svelte';
    import '../app.css'
    import Header from '../layout/Header/Header.svelte'
    import BigCard from '../components/BigCard/BigCard.svelte'
    // import CarouselCard from '../components/CarouselCard/CarouselCard.svelte'
    import Footer from '../layout/Footer/Footer.svelte'
    import LittleCard from '../components/LitlleCard/LitlleCard.svelte'
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
<title>Unic Paris</title>

<main>
    <div class="m-2 sm:m-6">
        <!-- <div class="p-6">
            {#each datas as data}
            <LittleCard picture='{data.cover_url}' name='{data.cover_url}' description='{data.cover_url}' price='{data.cover_url}' on:click={() => handleId(123)} />
            {/each}
        </div> -->
        <Header />
        <!-- <BigCard picture="https://cdn.paris.fr/qfapv4/2023/10/23/huge-efc64f2a6bd0674e013a2a946ce6f8cd.jpg" name="Pétanque square Emile Chautemps" /> -->
        <!-- <CarouselCard /> -->
        <Footer />
    </div>
</main>
