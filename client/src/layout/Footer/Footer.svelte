<script>
import { Github } from 'lucide-svelte';
</script>
<div class="bg-primary-75 rounded-lg p-4 flex flex-col lg:flex-row items-center justify-between">
    <div class="flex gap-2 items-center">
        <img src="https://res.cloudinary.com/diurvm1bd/image/upload/v1702620188/logo-little_upxy1d.svg" class="w-32 sm:w-48" alt="">
        <div class="flex flex-col gap-2">
            <div class="flex gap-2 items-center"><Github class="text-secondary" /><a target="_blank" href="https://github.com/ShuHado" class="text-secondary font-basic font-semibold">@ShuHado</a></div>
            <div class="flex gap-2 items-center"><Github class="text-secondary" /><a target="_blank" href="https://github.com/scotty974" class="text-secondary font-basic font-semibold">@scotty974</a></div>
            <div class="flex gap-2 items-center"><Github class="text-secondary" /><a target="_blank" href="https://github.com/clm-msch" class="text-secondary font-basic font-semibold">@clm-msch</a></div>
        </div>
    </div>
    <div class="flex gap-4 items-center">
        <p class="font-basic font-medium text-right">Projet réalisé à l’ESD Paris <br>
            avec l’API Open Data Paris <br>
            <b class="text-xs">Fabien - Cyril - Clément</b> <br> 
            <i class="text-xs">2023</i></p>
        <div class="flex flex-col gap-2">
            <a target="_blank" href="https://opendata.paris.fr/explore/dataset/que-faire-a-paris-/information/?disjunctive.tags&disjunctive.address_name&disjunctive.address_zipcode&disjunctive.address_city&disjunctive.pmr&disjunctive.blind&disjunctive.deaf&disjunctive.transport&disjunctive.price_type&disjunctive.access_type&disjunctive.programs"><img src="https://res.cloudinary.com/diurvm1bd/image/upload/v1702620457/creditparis_nf5kwl.svg" alt=""></a>
            <a target="_blank" href="https://ecole-du-digital.com/"><img src="https://res.cloudinary.com/diurvm1bd/image/upload/v1702620457/creditesd_hotg8y.svg" alt=""></a>
        </div>
    </div>
</div>