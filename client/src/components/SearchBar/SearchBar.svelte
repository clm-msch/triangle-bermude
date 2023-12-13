<script>
    import { Search } from 'lucide-svelte';
</script>
    <div class="flex justify-between sm:w-1/2 p-3 bg-white rounded-xl shadow-md">
        <input type="text" class="w-full focus:outline-none font-basic p-3" placeholder="Une expo, une activité" />
        <button class="font-basic font-regular bg-primary hover:bg-blue-800 w-fit text-white rounded-lg p-3 text-m flex items-center gap-2">
            <span class="hidden sm:block">Rechercher</span> 
            <Search size="18" />
        </button>
    </div>