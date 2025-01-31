/** @type {import('tailwindcss').Config} */
const { addDynamicIconSelectors } = require("@iconify/tailwind")
module.exports = {
  content: [
     "./templates/**/*.{html,js}",
    "home.html",
    "./src/**/*.{html,js}",
    "./static/node_modules/flyonui/dist/js/*.js"
  
  ],
    
  theme: {
    extend: {},
  
  },
  flyonui: {
    themes: [
      {
        mytheme: {
          "primary": "oklch(21% 0.034 264.665)",
          "primary-content": "oklch(98% 0 0)",
          "secondary": "oklch(44% 0.011 73.639)",
          "secondary-content": "oklch(98% 0.018 155.826)",
          "accent": "oklch(26.861% 0 0)",
          "accent-content": "oklch(100% 0 0)",
          "neutral": "oklch(55% 0.046 257.417)",
          "neutral-content": "oklch(100% 0 0)",
          "base-100": "oklch(100% 0 0)",
          "base-200": "oklch(97% 0 0)",
          "base-300": "oklch(94% 0 0)",
          "base-content": "oklch(0% 0 0)",
          "info": "oklch(44% 0.011 73.639)",
          "info-content": "oklch(97% 0.014 308.299)",
          "success": "oklch(90.13% 0.153 164.14)",
          "success-content": "oklch(12% 0.042 264.695)",
          "warning": "oklch(88.37% 0.135 79.94)",
          "warning-content": "oklch(17.674% 0.027 79.94)",
          "error": "oklch(78.66% 0.15 28.47)",
          "error-content": "oklch(39% 0.141 25.723)"
        }
      }
    ]
  },
  plugins: [
    require('flyonui'),
    addDynamicIconSelectors()
  ]
}

