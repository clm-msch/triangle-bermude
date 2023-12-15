<script lang="ts">
import { Phone, Mail, Facebook, Twitter} from 'lucide-svelte';
export let phone:string
export let mail:string
export let facebook:string
export let twitter:string
</script>

<ul class=" flex justify-between">
    
    <li class="flex py-2"> <a href="mailto:{mail}" ><Mail class="mr-3 text-titleCard"/> </a> </li>
    <li class="flex py-2">  <a target="_blank" href="{facebook}" > <Facebook class="mr-3 text-titleCard"/></a></li>
    <li class="flex py-2"> <a target="_blank" href="{twitter}" ><Twitter class="mr-3 text-titleCard"/>  </a></li>
    <li class="flex py-2"> <a target="_blank" href="{phone}" ><Phone class="mr-3 text-titleCard"/>  </a></li>
   
</ul>