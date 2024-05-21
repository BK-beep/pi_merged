/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./blogs/**/*.html"],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'SerenePink': '#985D69',
        'SerenePink1' : '#E1ACAC',
        'SereneGreen': '#13472E',
        'SereneBeige': '#EAE5DF',

      },
    },
  },
  plugins: [],
}
