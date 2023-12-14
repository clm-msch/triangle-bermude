/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors : {
        primary : {
          50: '#f5fcfb',
          75: '#d5f3ef',
          100: '#c4eee9',
          200: '#aae6df',
          300: '#99e1d9', //primary
          400: '#6b9e98',
          500: '#5d8984',
        },
        secondary : '#393424',
        // newprimary : '#99E1D9',
        titleCard : '#2B2B2B'
      },
      fontFamily: {
        brand: ['fields'],
        basic: ['Inter'],
      },
      backgroundImage: {
        'header': "url('https://res.cloudinary.com/diurvm1bd/image/upload/v1702559220/image_10_iwcucx.jpg')",
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