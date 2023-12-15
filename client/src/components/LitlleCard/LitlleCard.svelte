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

onMount(()=>{
    calculateLenght()
})
</script>

<div class="w-1/4 mx-2" >
<figure >
    <img src="{picture}" alt="{name}" class="h-96 object-cover rounded-lg my-3.5">
    <figcaption>
        <h3 class="text-lg text-titleCard font-semibold ">{name}</h3>
        <p class="font-light">{@html description}</p>
        <span class="text-titleCard"><strong>{price}</strong></span>
    </figcaption>
</figure>
</div>