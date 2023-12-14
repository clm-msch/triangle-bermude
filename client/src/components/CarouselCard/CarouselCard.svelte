<!-- <script>
import { Carousel } from 'flowbite-svelte';
import BigCard from '../BigCard/BigCard.svelte';

</script>

<div class="flex justify-center">
  <div class="w-1/2">
    <Carousel {BigCard}>
      <BigCard picture="https://cdn.paris.fr/qfapv4/2023/10/23/huge-efc64f2a6bd0674e013a2a946ce6f8cd.jpg" name="Pétanque square Emile Chautemps" />
      <BigCard picture="https://cdn.paris.fr/qfapv4/2023/10/26/huge-70ffa87b1b966dff747b16caa0434b56.jpg" name="Basket au TEP Paris Stadium Charlemagne" />
      <BigCard picture="https://cdn.paris.fr/qfapv4/2023/11/17/huge-3c1318c1e7803f05a788caeae16a9527.jpg" name="Multisports au gymnase Archereau" />
  </div>
  </div> -->

  <script>
    import { Carousel } from "flowbite-svelte";
    
    const data = [
      {
        component: "MyComponent1",
        props: {
          title: "Composant 1",
        },
      },
      {
        component: "MyComponent2",
        props: {
          title: "Composant 2",
        },
      },
      {
        component: "MyComponent3",
        props: {
          title: "Composant 3",
        },
      },
    ];
    </script>
    
    <Carousel {data}/>
