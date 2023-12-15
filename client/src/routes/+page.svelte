<script lang="ts">
    import { onMount, afterUpdate } from "svelte";
    import "../app.css";
    import Header from "../layout/Header/Header.svelte";
    import LitlleCard from "../components/LitlleCard/LitlleCard.svelte";
    import CarouselBigCard from "../components/CarouselBigCard/CarouselBigCard.svelte";
    import Footer from "../layout/Footer/Footer.svelte";
    import CardActivities from "../components/CardActivities/CardActivities.svelte";
  
    let datas = [];
    let wordData: string = "";
    let dataFound = true; // Nouvelle variable pour suivre si des données sont trouvées
    const api = "https://shuhado.alwaysdata.net/django/api/v1/event/";
  
    async function fetchData() {
      try {
        let apiUrl = api;
  
        if (wordData) {
          apiUrl += `?search=${wordData}`;
        }
  
        const resp = await fetch(apiUrl);
        const data = await resp.json();
  
        datas = data.results;
        
        // Mettez à jour la variable dataFound en fonction des résultats
        dataFound = datas.length > 0;
  
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
      fetchData();
    }
  
    $: fetchData();
  
    afterUpdate(() => {
      console.log("Data updated");
    });
  </script>
  
  <main>
    <div class="m-2 sm:m-6 flex flex-col gap-6 sm:gap-12">
      <Header on:word={handleSearch} />
      {#if !wordData}
        <div class="flex flex-col gap-2 sm:gap-6">
          <h2 class="font-brand font-semibold text-2xl sm:text-3xl text-secondary">
            Les Nouveautés
          </h2>
          <CarouselBigCard />
          <div class="flex flex-col mt-6">
            <h2 class="font-brand font-semibold text-2xl sm:text-3xl text-secondary">
              Dernière Chance
            </h2>
            <p class="font-basic font-light">
              Profitez de ces activités avant qu'elle ne s'arrête.
            </p>
          </div>
          <CardActivities />
        </div>
      {:else}
        {#if dataFound}
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
        {:else}
          <!-- Affichez un message si aucune correspondance n'est trouvée -->
          <p>Aucune correspondance trouvée.</p>
        {/if}
      {/if}
  
      <Footer />
    </div>
  </main>
  