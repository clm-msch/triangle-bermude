<script>
import { Splide, SplideSlide } from '@splidejs/svelte-splide';
import BigCard from '../BigCard/BigCard.svelte';
</script>
<div class="container m-auto w-fit h-fit">
  <Splide aria-label="My Favorite Images">
    <SplideSlide>
      <BigCard picture="" name="" />
    </SplideSlide>
    <SplideSlide>
      <BigCard picture="" name="" />
    </SplideSlide>
  </Splide>
</div>