<script lang="ts">
import '../[slug]/room.css'
import Map from '../../../components/Map/Map.svelte';
import DataActivities from '../../../components/DataActivites/DataActivities.svelte';
import SocialData from '../../../components/SocialData/SocialData.svelte'
import LocationCard from '../../../components/LocationCard/LocationCard.svelte';


</script>

<main class="container m-auto ">
    
    <div class="flex justify-between mt-6 items-center mb-2">
        <a href="/" class="bg-newprimary p-2 rounded-lg">Revenir à l'accueil</a>
    </div>
   

    <section class="mt-28">
        <div class="flex flex-col md:w-2/3 mobile:w-full">
            <h1 class="md:text-8xl mobile:text-4xl  z-40">L'Arc de Triomphe </h1>
            <span class=" w-full h-4 bg-newprimary relative bottom-6 mobile:bottom-4"></span>
        </div>
       
        <section class="flex md:flex-row mobile:flex-col-reverse md:items-start mobile:justify-start  z-40">
            <div class="flex md:flex-row mobile:flex-col-reverse md:justify-between md:items-start mt-8 ">
                <div class="flex flex-col justify-between">
                    <DataActivities price="Gratuit" access="Tout le monde" date="14 Décembre 2023"/>
                    <Map />
                    <SocialData phone="0000000"  mail="test@test.com" facebook="Fabien" twitter="Fabien"/>
                </div>
               
                <p class="md:w-96 mobile:w-full">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Autem, saepe natus aliquam ex consequatur laboriosam ipsum expedita corrupti tempore eius sapiente voluptas maxime doloribus, vel et provident incidunt nam cum!</p>
            </div>
            <div class="md:ml-10"><img src="https://cdn.paris.fr/qfapv4/2023/10/25/huge-54b666d11f1633e18341957c6015d8c6.jpg" alt="Tennis" class=" md:w-zoomPicture md:rounded-full md:h-zoomPicture object-cover md:relative md:bottom-40 -z-10 mobile:w-full"></div>
        </section>
       
    </section>
</main>