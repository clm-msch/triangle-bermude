<script lang="ts">
    import { UsersRound,Calendar,Euro } from 'lucide-svelte';
    export let price:string
    export let access:string
    export let date:string
</script>

<ul class="w-80 md:mr-10">
    <li class="flex  mt-4"><Euro  class="mr-3 "/> : {price}</li>
    <li class="flex mt-4"><UsersRound class="mr-3"/> : {access}</li>
    <li class="flex mt-4"><Calendar  class="mr-3 "/> : {date}</li>

</ul>