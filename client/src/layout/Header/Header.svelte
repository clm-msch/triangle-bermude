<script>
    import Logo from '../../assets/logo.svg'
    import SearchBar from '../../components/SearchBar/SearchBar.svelte'
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher()
    let word = ''

function handleSearch(event) {
    word = event.detail;
    
    handleWord()
  // Perform any other actions based on the search term if needed
}

function handleWord(){
    dispatch('word', word)
}
</script>
<div class="bg-header h-90% rounded-lg bg-cover bg-center shadow-md">
    <div class="px-6 md:px-32 py-32 flex flex-col items-center gap-8 ">
        <div class="flex flex-col gap-2">
            <img src={Logo} class="sm:w-full w-80 m-auto" alt="logo">
            <p class="font-basic font-medium text-primary-50 text-md sm:text-lg  text-center">Trouvez votre prochaine aventure unique à Paris.</p>
        </div>
      
        <SearchBar on:search="{handleSearch}" />
    </div>
</div>
