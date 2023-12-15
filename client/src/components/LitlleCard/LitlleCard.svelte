<script lang="ts">
  import { onMount } from "svelte";


export let picture:string
export let name:string
export let description:string
export let price:string
let idActivity:number;
function calculateLenght(){
    const maxLength = 67;

    if(description.length >= maxLength) {
       description =  description.substring(0 ,maxLength - 10) + '...'
    }
}
const API_BASE_URL:string = "https://shuhado.alwaysdata.net/django/api/v1/"


async function fetchDataPrice(price_id:string){
    
    try{
        const resp = await fetch(API_BASE_URL+'price_type/'+price_id+'/')
        const data = await resp.json()
        
        price = data.name 
        return price
    }catch(error){
        console.log(error)
    }
}

onMount(async()=>{
    calculateLenght()
    await fetchDataPrice(price)
})
</script>

<div class="w-1/4 p-2 gap-1 hover:cursor-pointer transition ease-in-out delay-150 duration-300 hover:scale-75 ">
<figure >
    <img src="{picture}" alt="{name}" class="h-96 object-cover rounded-lg mb-3.5">
    <figcaption>
        <h3 class="text-lg text-titleCard font-semibold ">{name}</h3>
        <p class="font-light">{@html description}</p>
        <span class="text-titleCard"><strong>{price}</strong></span>
    </figcaption>
</figure>
</div>