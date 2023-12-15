import { error } from '@sveltejs/kit';
const API_URL:string = "https://shuhado.alwaysdata.net/django/api/v1/event/"

export async function load({params}){
   try{
	const resp = await fetch(API_URL+params.slug+'/')
	const data = await resp.json()
	console.log(data)
	return data
   }catch(error){
	console.log(error)
	throw error(404, 'Not found');
   }
	

	
}