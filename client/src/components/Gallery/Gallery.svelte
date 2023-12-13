<script lang="ts">
  import { MapLibre,Marker } from 'svelte-maplibre';

  export let picture: string;
  export let name: string;

 
</script>

<div class="grid grid-cols-3 mt-6 gap-4 ">
  <div class="col-span-2 mr-2 row-span-2">
    <img src={picture} alt={name} class="rounded-l-xl" />
  </div>
  <div id="map" class="row-span-2">
    <MapLibre
    
    center={[50, 50]}
    zoom={7}
    style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
    class="relative w-full aspect-[9/16] h-full sm:max-h-full sm:aspect-video"
    standardControls
  >
  <Marker
  lngLat={[2.36093301435977, 48.8540040044365]}
  class="border-gray-200 border shadow-2xl focus:outline-2 focus:outline-black w-20 h-8 bg-red-300 text-black rounded-full grid place-items-center"
>
  <span> Drag me ! </span>
</Marker>
</MapLibre>
  </div>
</div>
