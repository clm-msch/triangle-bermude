/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors : {
        primary : '#155FC4',
        newprimary : '#99E1D9',
        titleCard : '#2B2B2B'
      },
      fontFamily: {
        brand: ['fields'],
        basic: ['Inter'],
      },
      backgroundImage: {
        // 'header': "url('./src/assets/bg-home-paris.jpg')",
        'header': "url('./static/bg-home-paris.jpg')",
      },width:{
        zoomPicture : "500px"
      },
      height : {
        zoomPicture : "500px"
      },
      screens:{
        mobile : "300px"
      }
    }
  },
  plugins: []
};