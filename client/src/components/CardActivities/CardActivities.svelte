<script lang="ts">
import LitlleCard from "../LitlleCard/LitlleCard.svelte";
import { onMount } from 'svelte';
  
 

  let datas: any[] = [];
  let page:number
  const api = 'https://shuhado.alwaysdata.net/django/api/v1/event/?page=1';

  async function fetchData() {
    try {
      const resp = await fetch(api);
      const data = await resp.json();
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
</script>

<section class="flex">
    {#each datas as data}
        <LitlleCard picture="{data.cover_url}" name="{data.title}" description="{data.lead_text}" price="Gratuit"/>
    {/each}
   
  
</section>