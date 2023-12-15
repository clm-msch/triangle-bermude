<script lang="ts">
    import { onMount } from 'svelte';
    import '../app.css'
    import Header from '../layout/Header/Header.svelte'
    import BigCard from '../components/BigCard/BigCard.svelte'
    import CarouselBigCard from '../components/CarouselBigCard/CarouselBigCard.svelte';
    import Footer from '../layout/Footer/Footer.svelte'
    import LittleCard from '../components/LitlleCard/LitlleCard.svelte'
    import CardActivities from '../components/CardActivities/CardActivities.svelte';
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
    <div class="m-2 sm:m-6 flex flex-col gap-6 sm:gap-12">
        <!-- <div class="p-6">
            {#each datas as data}
            <LittleCard picture='{data.cover_url}' name='{data.title}' description='{data.cover_url}' price='{data.cover_url}' on:click={() => handleId(123)} />
            {/each}
        </div> -->
        <Header />
        <div class="flex flex-col gap-2 sm:gap-6">
            <h2 class="font-brand font-semibold text-2xl sm:text-3xl text-secondary">Les Nouveautés</h2>
            <CarouselBigCard />
            <div class="flex flex-col mt-6">
                <h2 class="font-brand font-semibold text-2xl sm:text-3xl text-secondary">Les Différentes facons de découvrir Paris</h2>
           <p class="my-2">Découvrir des lieux uniques sur Paris</p>
            </div>
            
            <CardActivities />
        </div>
        <!-- <BigCard picture="https://cdn.paris.fr/qfapv4/2023/10/23/huge-efc64f2a6bd0674e013a2a946ce6f8cd.jpg" name="Pétanque square Emile Chautemps" /> -->
        <!-- <CarouselCard /> -->
        <Footer />
    </div>
</main>
