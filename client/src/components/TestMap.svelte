<script>
// @ts-nocheck

  import { onMount, onDestroy } from 'svelte'
  import {Map, MapStyle, config} from '@maptiler/sdk';
  import "@maptiler/sdk/dist/maptiler-sdk.css";

  let map;
  let mapContainer;

  config.apiKey = 'iRznsVPWcekup3LE99ON';

  onMount(() => {
    const initialState = { lng: 139.753, lat: 35.6844, zoom: 14 };

    map = new Map({
      container: mapContainer,
      style: MapStyle.STREETS,
      center: [initialState.lng, initialState.lat],
      zoom: initialState.zoom
    });

  });

  onDestroy(() => {
    map.remove();
  });
</script>

<div class="map-wrap">
  <div class="map rounded-lg" bind:this={mapContainer}></div>
</div>

<style>
  .map-wrap {
    position: relative;
    width: 100%;
    height: calc(100vh - 77px); /* calculate height of the screen minus the heading */
  }

  .map {
    position: absolute;
    width: 100%;
    height: 100%;
  }
</style>