<script lang="ts">
  import LitlleCard from "../LitlleCard/LitlleCard.svelte";
  import { onMount } from 'svelte';
  import { afterUpdate } from 'svelte';
  import { ChevronLeft, ChevronRight } from 'lucide-svelte';

  let datas: any[] = [];
  let page: number = 1;
  let filteredActivities: any[] = [];
  const pageSize: number = 91;
  let totalResults: number = 0;
  const api = (pageNum: number) => `https://shuhado.alwaysdata.net/django/api/v1/event/?page=${pageNum}`;

  async function fetchData() {
    try {
      const resp = await fetch(api(page));
      const data = await resp.json();
      datas = data.results;
      totalResults = data.count;
      return datas;
    } catch (error) {
      console.log(error);
    }
  }

  onMount(async () => {
    await fetchData();
  });

  afterUpdate(() => {
    fetchData();
    filteredActivities = filterActivitiesByEndDate();
  });

  function filterActivitiesByEndDate() {
    const currentDate = new Date();
    return datas
      .filter((activity) => new Date(activity.date_end) > currentDate)
      .sort((a, b) => Number(new Date(a.date_end)) - Number(new Date(b.date_end)))
      .slice(0, 12);
  }

  function nextPage() {
    if ((page - 1) * pageSize + datas.length < totalResults) {
      page++;
    }
  }

  function prevPage() {
    if (page > 1) {
      page--;
    }
  }
</script>

<section class="grid grid-cols-2 sm:grid-cols-3">
  {#each filteredActivities as data}
    <LitlleCard picture="{data.cover_url}" name="{data.title}" description="{data.lead_text}" price="{data.price_id}" id="{data.id}" />
  {/each }
</section>
<div class="pagination flex w-full items-center justify-center">
  <button on:click="{prevPage}" disabled="{page === 1}" class="text-center bg-primary-300 p-2 rounded-md"><ChevronLeft /></button>
  <span class="mx-2 text-lg text-primary-500">{page}</span>
  <button on:click="{nextPage}" disabled="{(page - 1) * pageSize + datas.length >= totalResults}" class="text-center bg-primary-300 p-2 rounded-md"><ChevronRight /></button>
</div>
