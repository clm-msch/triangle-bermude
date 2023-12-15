<script lang="ts">
  import { MapLibre, Marker } from "svelte-maplibre";
  import { MapPin } from "lucide-svelte";
  import { onMount } from "svelte";
  export let lng: number;
  export let lat: number;
  export let adresse_id: number;
  let adresseData: any = [];
  const API_BASE_URL: string = "https://shuhado.alwaysdata.net/django/api/v1/";

  async function fetchAdress(adress_id: number) {
    try {
      const resp = await fetch(API_BASE_URL + "adresse/" + adress_id + "/");
      const data: any = await resp.json();
      
      lat = data.latitude
      lng = data.longitude
      
      return data;
    } catch (error) {
      console.log(error);
    }
  }
  onMount(async() => {
    adresseData = await fetchAdress(adresse_id);
    console.log(adresseData)
  });
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
      <MapPin color="#155FC4" />
    </Marker>
  </MapLibre>
  <p class="mb-2">Adresse : {adresseData.address_name}</p>
</div>
