<script>
    import { Search } from 'lucide-svelte';
</script>
<div class="bg-red-500">
    <div class="flex justify-center w-fit bg-green-500 shadow-sm">
        <input type="text" class="w-1/2 focus:outline-none font-basic p-3" placeholder="Je veux faire du yoga dans le 8 ème" />
        <button class="font-basic font-regular bg-primary w-fit text-white rounded-md p-3 text-m flex items-center gap-2">Rechercher <Search size="18" /></button>
    </div>
</div>
