/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors : {
        primary : '#155FC4',
        titleCard : '#2B2B2B'
      },
      fontFamily: {
        brand: ['fields'],
        basic: ['Inter'],
      },
      backgroundImage: {
        'header': "url('./src/assets/bg-home-paris.jpg')",
      }
    }
  },
  plugins: []
};