module.exports = {
  plugins: [
    require('postcss-simple-vars'),
    require('postcss-nested'),
    require('@tailwindcss/postcss'),
    require('autoprefixer'),
  ],
};