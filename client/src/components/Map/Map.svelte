<script lang="ts">
    import { MapLibre,Marker } from 'svelte-maplibre';
    import { MapPin } from 'lucide-svelte';
    </script>

<div id="map">
    <MapLibre
    
    center={[2.36093301435977, 48.8540040044365]}
    zoom={15}
    style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
    class=" w-full aspect-[9/16] h-40 sm:max-h-full sm:aspect-video my-6"
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