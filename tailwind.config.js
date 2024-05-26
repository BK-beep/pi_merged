/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./blogs/**/*.html",
    "./CLIENT/**/*.html",
    './**/templates/**/*.html',
    './static/**/*.js',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'SerenePink': '#985D69',
        'SerenePink-200': '#be959f',
        'SerenePink1' : '#be959f',
        'SereneGreen': '#13472E',
        'SereneBeige': '#EAE5DF',

      },
    },
  },
  plugins: [],
}
