<!-- ChildComponent.svelte -->
<script lang="ts">
    import { Search } from 'lucide-svelte';
    import { createEventDispatcher } from 'svelte';
  
    let searchWord: string = '';
    const dispatch = createEventDispatcher();
  
    function handleSearch() {
      dispatch('search', searchWord);
    }
  </script>
  
  <div class="flex justify-between p-3 bg-white rounded-xl shadow-md">
    <input type="text" class="w-full focus:outline-none font-basic p-3" placeholder="Une expo, une activité" bind:value={searchWord} on:input={handleSearch}/>
    <button on:click="{handleSearch}" class="font-basic font-regular bg-primary-300 hover:bg-primary-400 w-fit text-white rounded-lg p-3 text-md flex items-center gap-2">
      <span class="hidden sm:block font-medium text-secondary">Rechercher</span>
      <Search size="18" class="text-secondary" />
    </button>
  </div>
  