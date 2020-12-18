// FOr smooth transition between light and dark theme

const themeButton = document.querySelector(".theme-toggle")

let currentTheme = localStorage.getItem("data-theme")
console.log(currentTheme)
if (!currentTheme) {
  localStorage.setItem("data-theme", "light")
}

applyTheme(currentTheme)

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

function commentSection(comments_room, comments_server, contact_name) {
  const roomName = comments_room
  const commentHost = comments_server
  const contactName = contact_name
  var d = document,
    s = d.createElement("script")
  s.src = "https://" + commentHost + "/static/comments.js"
  ;(d.head || d.body).appendChild(s)
}

function overPlayer(stream_url, stream_key) {
  OvenPlayer.debug(true)
  let webrtcSources = OvenPlayer.generateWebrtcUrls([
    {
      host: stream_url,
      //	host : 'ws://95.217.152.160:3333'.
      application: "app",
      stream: stream_key + "_o",
      width: "320",
      height: "160",
      label: "Stream 1"
    }
  ])

  let player = OvenPlayer.create("player", {
    autoStart: true,
    sources: webrtcSources
  })
  player.on("error", function (error) {
    console.log(error)
  })
  player.on("ready", function (data) {
    player.play()
  })
}
