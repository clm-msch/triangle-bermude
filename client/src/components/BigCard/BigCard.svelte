<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    export let picture: string;
    export let name: string;
    export let id: any;
    let datas: any[] = [];
    const api = 'https://shuhado.alwaysdata.net/django/api/v1/event/';
  
    async function fetchData() {
      try {
        const resp = await fetch(api);
        const data: any = await resp.json();
        datas = data.results;
        return datas;
      } catch (error) {
        console.log(error);
      }
    }
  
    onMount(async () => {
      await fetchData();
    });
  
    function handleId() {
      goto(`/rooms/${id}`);
    }
  </script>
  
  <div on:click={handleId} class="bg-primary-50 rounded-lg shadow-md">
    <figure>
      <img loading="lazy" src="{picture}" alt="{name}" class="rounded-t-lg">
      <figcaption class="py-4 px-2">
        <div class="flex justify-between items-center">
          <h3 class="text-base">{name}</h3>
          <button class="bg-primary-300 hover:bg-primary-400 w-fit text-secondary rounded-lg p-3 text-sm font-semibold ">
            Découvrir
          </button>
        </div>
      </figcaption>
    </figure>
  </div>
  