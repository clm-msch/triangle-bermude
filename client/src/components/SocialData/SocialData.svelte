<script lang="ts">
import { Phone, Mail, Facebook, Twitter} from 'lucide-svelte';
export let phone:string
export let mail:string
export let facebook:string
export let twitter:string
</script>

<ul class="mt-6">
    <li class="flex py-2"><Phone class="mr-3 text-titleCard"/> : <span  class=" pl-2">{phone}</span></li>
    <li class="flex py-2"><Mail class="mr-3 text-titleCard"/> : <a href="mailto:{mail}" class="text-primary underline pl-2">{mail}</a> </li>
    <li class="flex py-2"><Facebook class="mr-3 text-titleCard"/> : <a href="{facebook}" class="text-primary underline pl-2"> {facebook}</a></li>
    <li class="flex py-2"><Twitter class="mr-3 text-titleCard"/> : <a href="{twitter}" class="text-primary underline pl-2"> {twitter}</a></li>
   
</ul>