/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/**/*.{php,html,js,py}"],
    theme: {
      extend: {
        backgroundImage: {
          'bg-01': "url('../templates/img/header.png')",
          'bg-02': "url('../templates/img/image_bg.jpg')",
        },
      },
    },
    plugins: [],
  }