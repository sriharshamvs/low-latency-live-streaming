// For smooth transition between light and dark theme

const themeButton = document.querySelector(".theme-toggle")

let currentTheme = localStorage.getItem("data-theme")
if (!currentTheme) {
  localStorage.setItem("data-theme", "light")
  applyTheme("light")
}

themeButton.addEventListener("click", (e) => {
  if (document.documentElement.getAttribute("data-theme") === "light") {
    applyTheme("dark")
    localStorage.setItem("data-theme", "dark")
  } else {
    localStorage.setItem("data-theme", "light")
    applyTheme("light")
  }
  transition()
})

function applyTheme(theme) {
  if (theme === "light") {
    document.documentElement.setAttribute("data-theme", "light")
  } else {
    document.documentElement.setAttribute("data-theme", "dark")
  }
}

function transition() {
  document.documentElement.classList.add("smooth")
  window.setTimeout(() => {
    document.documentElement.classList.remove("smooth")
  }, 1000)
}
