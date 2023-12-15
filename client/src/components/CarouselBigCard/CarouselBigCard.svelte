<script lang="ts">
  import { onMount } from 'svelte';
  import BigCard from '../BigCard/BigCard.svelte';

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

</script>

<div class="grid grid-cols-2 sm:grid-cols-3 gap-4">
  {#each datas.slice(0, 6) as data (data.id)}
    <BigCard picture="{data.cover_url}" name="{data.title}" id="{data.id}" />
  {/each}
</div>
