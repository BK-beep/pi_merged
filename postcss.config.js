module.exports = {
    plugins: [
      require('tailwindcss'),
      require('autoprefixer'),
    ],
  };

// npx postcss static/css/main.css -o static/css/output.css --watch