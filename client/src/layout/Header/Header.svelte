<script>
    import Logo from '../../assets/logo.svg'
    import SearchBar from '../../components/SearchBar/SearchBar.svelte'
</script>
<div class="bg-header mx-4 sm:mx-6 h-90% rounded-b-lg bg-cover bg-center">
    <div class="px-2 py-32 flex flex-col items-center gap-8 ">
        <div class="flex flex-col gap-2">
            <img src={Logo} alt="">
            <p class="font-basic font-medium text-primary-50 text-lg">Lorem ipsum dolor sit amet consectetur adipisicing.</p>
        </div>
        <SearchBar />
    </div>
</div>
