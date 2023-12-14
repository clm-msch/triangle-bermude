<script lang="ts">
import '../[slug]/room.css'
import { onMount } from 'svelte';
import Map from '../../../components/Map/Map.svelte';
import DataActivities from '../../../components/DataActivites/DataActivities.svelte';
import SocialData from '../../../components/SocialData/SocialData.svelte'
export let data;
let price_id:number = data.price_id
let price:string
let access_id:number = data.access_id
let access:string

let date_start = data.date_start
const dateObjectStart = new Date(date_start)
const options:any = {
  day: 'numeric',
  month: 'long',
  year: 'numeric',
  hour: 'numeric',
  minute: 'numeric',
  timeZoneName: 'short'
};

const dateFormatter = new Intl.DateTimeFormat('fr-FR', options);
const formattedDate = dateFormatter.format(dateObjectStart);

let date_end = data.date_end
const dateObjectEnd = new Date(date_end)
const dateFormatterEnd = new Intl.DateTimeFormat('fr-FR', options);
const formattedDateEnd = dateFormatterEnd.format(dateObjectEnd);


const API_BASE_URL:string = "https://shuhado.alwaysdata.net/django/api/v1/"


async function fetchDataPrice(price_id:number){
    
    try{
        const resp = await fetch(API_BASE_URL+'price_type/'+price_id+'/')
        const data = await resp.json()
        
        price = data.name 
        return price
    }catch(error){
        console.log(error)
    }
}
async function fetchDataAccess(access_id:number){
    
    try{
        const resp = await fetch(API_BASE_URL+'audience/'+access_id+'/')
        const data = await resp.json()
        
        access = data.name 
        return access
    }catch(error){
        console.log(error)
    }
}


onMount(async ()=>{
fetchDataPrice(price_id)
fetchDataAccess(access_id)

})

</script>

<main class="container m-auto ">
    
    <div class="flex justify-between mt-6 items-center mb-2">
        <a href="/" class="bg-primary-300 p-2 rounded-lg">Revenir à l'accueil</a>
    </div>
   

    <section class="mt-28">
        <div class="flex flex-col md:w-2/3 mobile:w-full">
            <h1 class="md:text-8xl mobile:text-4xl  z-40">{data.title} </h1>
            <span class=" w-full h-4 bg-primary-300 relative bottom-6 mobile:bottom-4"></span>
        </div>
       
        <section class="flex md:flex-row mobile:flex-col-reverse md:items-start mobile:justify-start  z-40">
            <div class="flex md:flex-row mobile:flex-col-reverse md:justify-between md:items-start mt-8 ">
                <div class="flex flex-col justify-between ">
                    <DataActivities price="{price}" access="{access}" date="Début : {formattedDate} - Fin : {formattedDateEnd}"/>
                    <Map lng="{2.36093301435977}" lat="{48.8540040044365}"/>
                    <SocialData phone="{data.contact_phone}"  mail="{data.contact_mail}" facebook="{data.contact_url}" twitter="{data.contact_twitter}"/>
                </div>
               
                <p class="md:w-96 mobile:w-full">{data.lead_text}</p>
            </div>
            <div class="md:ml-10"><img src="{data.cover_url}" alt="{data.cover_alt}" class="md:w-zoomPicture md:rounded-full md:h-zoomPicture object-cover md:relative md:bottom-40 -z-10 mobile:w-full"></div>
        </section>
       
    </section>
</main>