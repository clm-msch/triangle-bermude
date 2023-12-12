<script lang="ts">
import '../rooms/room.css'
import Gallery from '../../components/Gallery/Gallery.svelte';
</script>

<main class="container m-auto ">
    <div class="flex justify-between mt-6 items-center mb-2">
        <h1 class="text-4xl">Arc de Triomphe</h1>
        <h3 class="underline text-base">Architecture</h3>
    </div>
    <hr>
    <Gallery picture='https://cdn.paris.fr/qfapv4/2023/07/26/huge-7a54e7be61474eacf645a10190fd5e10.jpg' name="Arc de Triomphe"/>
    <section class='flex flex-col'>
        <h2>A propos</h2>
    </section>

</main>