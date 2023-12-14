<script lang="ts">
  import { MapLibre,Marker } from 'svelte-maplibre';
  import { MapPin } from 'lucide-svelte';
  export let picture: string;
  export let name: string;

 
</script>

<div class="grid grid-cols-3 mt-6 gap-4 ">
  <div class="col-span-2 mr-2 row-span-2">
    <img src={picture} alt={name} class="rounded-xl" />
  </div>
 
</div>
