<script lang="ts">
    import { MapLibre,Marker } from 'svelte-maplibre';
    import { MapPin } from 'lucide-svelte';


    export let lng:number
    export let lat:number
    </script>

<div id="map">
    <MapLibre
    
    center={[lng, lat]}
    zoom={15}
    style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
    class=" w-full aspect-[9/16] h-40 sm:max-h-full sm:aspect-video my-6"
    standardControls
  >
  <Marker
  lngLat={[lng, lat]}
  class=" focus:outline-2 focus:outline-black w-20 h-8  text-black rounded-full grid place-items-center"
>
<MapPin color="#155FC4"/>
</Marker>
</MapLibre>
  </div>