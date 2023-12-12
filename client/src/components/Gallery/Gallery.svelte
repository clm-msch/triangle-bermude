<script lang="ts">
  
  export let picture: string;
  export let name: string;

 
</script>

<div class="grid grid-cols-3 mt-6 gap-4 h-96">
  <div class="col-span-2 mr-2 row-span-2">
    <img src={picture} alt={name} class="rounded-l-xl" />
  </div>
  <div id="map" class="row-span-2" style="height: 100%;"></div>
</div>
