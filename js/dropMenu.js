const dropLinks = document.querySelectorAll(".dropLink")
const uls = document.querySelectorAll(".chapter > ul")
const btn = document.getElementById("btn")
let toggle = false

function hideUls() {
    uls.forEach(ul => {
        ul.classList.add("hide")
    })
}
hideUls()

btn.addEventListener("click",() => {

    if(!toggle){
        uls.forEach(ul => {
            ul.classList.remove("hide")
        })
    } else {
        uls.forEach(ul => {
            ul.classList.add("hide")
        })
    }
    toggle = !toggle
    console.log(toggle)
})



dropLinks.forEach(link => {
    link.addEventListener("click",(e) => {
        let parent = e.target.parentElement
        let ul = parent.querySelector("ul")

        if(ul.classList.contains("hide")){
            ul.classList.remove("hide")
        } else {
            ul.classList.add("hide")
        }
        if(ul.classList.contains("show")){
            ul.classList.remove("show")
            ul.classList.add("hide")

        }
    })
})

