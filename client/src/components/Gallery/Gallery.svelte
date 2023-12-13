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
  <div id="map" class="row-span-2">
    <MapLibre
    
    center={[2.36093301435977, 48.8540040044365]}
    zoom={20}
    style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
    class="relative w-full aspect-[9/16] h-full sm:max-h-full sm:aspect-video rounded-xl"
    standardControls
  >
  <Marker
  lngLat={[2.36093301435977, 48.8540040044365]}
  class=" focus:outline-2 focus:outline-black w-20 h-8  text-black rounded-full grid place-items-center"
>
<MapPin color="#155FC4"/>
</Marker>
</MapLibre>
  </div>
</div>
