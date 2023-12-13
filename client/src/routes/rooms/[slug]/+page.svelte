<script lang="ts">
import '../[slug]/room.css'
import Gallery from '../../../components/Gallery/Gallery.svelte';
import DataActivities from '../../../components/DataActivites/DataActivities.svelte';
import SocialData from '../../../components/SocialData/SocialData.svelte'
import LocationCard from '../../../components/LocationCard/LocationCard.svelte';

export let data;
</script>

<main class="container m-auto ">
    <div class="flex justify-between mt-6 items-center mb-2">
        <h1 class="text-4xl font-brand ">{data.title}</h1>
        <h3 class="underline text-base">Architecture</h3>
    </div>
    <hr>
    <Gallery picture='https://cdn.paris.fr/qfapv4/2023/07/26/huge-7a54e7be61474eacf645a10190fd5e10.jpg' name="Arc de Triomphe"/>
    <section class="grid grid-cols-3 gap-4">
        <section class='flex flex-col mt-6 col-span-2'>
            <h2 class="text-2xl mb-3 font-brand">A propos</h2>
            <p class="text-base font-light">{data.content}</p>
            
    <DataActivities price="Gratuit" access="Tout le monde" date="12 Décembre 2023"/>
    <hr>
    <SocialData phone="00000000" mail="test@test.gmail" facebook="Fabien" twitter="Fabien"/>
        </section>
        <div class="shadow-md h-40 mt-6 rounded-lg ">
    <LocationCard />
        </div>
    </section>
</main>