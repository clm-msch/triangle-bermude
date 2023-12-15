<script lang="ts">
  import { onMount } from "svelte";
  import { goto } from '$app/navigation';
export let id:number
export let picture:string
export let name:string
export let description:string
export let price:number
let price_name:string
let idActivity:number;
function calculateLenght(){
    const maxLength = 67;

    if(description.length >= maxLength) {
       description =  description.substring(0 ,maxLength - 10) + '...'
    }
}
const API_BASE_URL:string = "https://shuhado.alwaysdata.net/django/api/v1/"


async function fetchDataPrice(price_id:number){
    
    try{
        const resp = await fetch(API_BASE_URL+'price_type/'+price_id+'/')
        const data = await resp.json()
        
        price_name = data.name 
        return price_name
    }catch(error){
        console.log(error)
    }
}
function handleId() {
      goto(`/rooms/${id}`);
      console.log(id)
    }
    
onMount(async()=>{
    calculateLenght()
    await fetchDataPrice(price)
})
</script>

<div class="w-1/4 p-2 gap-1 hover:cursor-pointer transition ease-in-out delay-150 duration-300 hover:scale-90" on:click={handleId}>
<figure >
    <img src="{picture}" alt="{name}" class="h-96 object-cover rounded-lg mb-3.5">
    <figcaption>
        <h3 class="text-lg text-titleCard font-semibold ">{name}</h3>
        <p class="font-light">{@html description}</p>
        <span class="text-titleCard"><strong>{price_name}</strong></span>
    </figcaption>
</figure>
</div>