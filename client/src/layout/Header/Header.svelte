<script>
    import Logo from '../../assets/logo.svg'
    import SearchBar from '../../components/SearchBar/SearchBar.svelte'
</script>
<div class="bg-header mx-4 sm:mx-6 h-90% rounded-b-xl bg-cover bg-center shadow-md">
    <div class="px-12 md:px-32 py-32 flex flex-col items-center gap-8 ">
        <div class="flex flex-col gap-2">
            <img src={Logo} alt="">
            <p class="font-basic font-medium text-primary-50 text-lg text-center">Lorem ipsum dolor sit amet consectetur adipisicing.</p>
        </div>
        <SearchBar />
    </div>
</div>
