<script>
import { Splide, SplideSlide } from '@splidejs/svelte-splide';
import BigCard from '../BigCard/BigCard.svelte';


</script>
<div class="">
  <Splide   options={ {
    type  : 'loop',
    width : 400,
    height : 250,
    gap   : '1rem',
  } }
  aria-label="My Favorite Images" class="bg-slate-300 px-6 py-4">
    <SplideSlide>
      <BigCard picture="https://cdn.paris.fr/qfapv4/2023/10/23/huge-efc64f2a6bd0674e013a2a946ce6f8cd.jpg" name="Pétanque square Emile Chautemps" />
    </SplideSlide>
    <SplideSlide>
      <BigCard picture="https://cdn.paris.fr/qfapv4/2023/10/26/huge-70ffa87b1b966dff747b16caa0434b56.jpg" name="Basket au TEP Paris Stadium Charlemagne" />
    </SplideSlide>
    <SplideSlide>
      <BigCard picture="https://cdn.paris.fr/qfapv4/2023/11/17/huge-3c1318c1e7803f05a788caeae16a9527.jpg" name="Multisports au gymnase Archereau" />
    </SplideSlide>
  </Splide>
</div>