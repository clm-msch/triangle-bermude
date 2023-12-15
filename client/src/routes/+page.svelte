<script lang="ts">
    import { onMount,afterUpdate  } from "svelte";
    import "../app.css";
    import Header from "../layout/Header/Header.svelte";
    import LitlleCard from "../components/LitlleCard/LitlleCard.svelte";
    import CarouselBigCard from "../components/CarouselBigCard/CarouselBigCard.svelte";
    import Footer from "../layout/Footer/Footer.svelte";
  
    import CardActivities from "../components/CardActivities/CardActivities.svelte";
    let datas = [];
    let wordData: string = "";
    const api = "https://shuhado.alwaysdata.net/django/api/v1/event/";
  
    async function fetchData() {
      try {
        let apiUrl = api;
  
        // Si un terme de recherche est défini, ajoutez-le à l'URL de l'API
        if (wordData) {
          apiUrl += `?search=${wordData}`;
        }
  
        const resp = await fetch(apiUrl);
        const data = await resp.json();
 
        // Assurez-vous de traiter correctement les résultats en fonction de la présence du terme de recherche
        datas = data.results;
  
       console.log(datas)
        return datas;
      } catch (error) {
        console.log(error);
      }
    }
    onMount(async () => {
      await fetchData();
    });
    function handleSearch(event: any) {
      wordData = event.detail;
      // Fetch data based on the search term
      fetchData();
    }
  
    $: fetchData();
  
  // Utilisez afterUpdate pour gérer les mises à jour après chaque rendu
  afterUpdate(() => {
    console.log('Data updated');
  });
  </script>
  
  <title>Unic Paris</title>
  
  <main>
    <div class="m-2 sm:m-6 flex flex-col gap-6 sm:gap-12">
      <!-- <div class="p-6">
              {#each datas as data}
              <LittleCard picture='{data.cover_url}' name='{data.title}' description='{data.cover_url}' price='{data.cover_url}' on:click={() => handleId(123)} />
              {/each}
          </div> -->
      <Header on:word={handleSearch} />
      {#if !wordData}
        <div class="flex flex-col gap-2 sm:gap-6">
          <h2
            class="font-brand font-semibold text-2xl sm:text-3xl text-secondary"
          >
            Les Nouveautés
          </h2>
          <CarouselBigCard />
          <div class="flex flex-col mt-6">
            <h2 class="font-brand font-semibold text-2xl sm:text-3xl text-secondary">Dernière Chance</h2>
            <p class="font-basic font-light">Profitez de ces activités avant qu'elle ne s'arrête.</p>
          </div>
          <CardActivities />
        </div>
      {:else}
      <div class="grid grid-cols-2 sm:grid-cols-3 gap-4">
        {#each datas as data}
        
          <LitlleCard
            picture={data.cover_url}
            name={data.title}
            description={data.lead_text}
            price={data.price_id}
            id={data.id}
          />
        {/each}
      </div>
        
      {/if}
  
      <!-- <BigCard picture="https://cdn.paris.fr/qfapv4/2023/10/23/huge-efc64f2a6bd0674e013a2a946ce6f8cd.jpg" name="Pétanque square Emile Chautemps" /> -->
      <!-- <CarouselCard /> -->
      <Footer />
    </div>
  </main>
  