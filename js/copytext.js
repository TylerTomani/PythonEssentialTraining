const cpyText = document.querySelectorAll(".cpyText")
let map = [];
let copy = false
let toggle = false
let text = ""


copyTxt()

cpyText.forEach(c => {
    c.addEventListener("focusin",(e) => {
        let code = c.querySelector("code")
        toggle = true
        console.log("focus toggle:",toggle)
        console.log("copy", copy )
        if(copy = true){
            text = code.innerText

        }

    })
    c.addEventListener("focusout",(e) => {
        let code = c.querySelector("code")
        toggle = false
        console.log(toggle)
        console.log("copy", copy )
    })
})

function copyTxt(){
    addEventListener("keydown",e => {
        // 91 67
        if(e.keyCode == 91){
            map[0] = 1;
        } 
        if(e.keyCode == 67){
            map[1] = 1
        }
    
        if(map[0] == 1 && map[1] == 1){
            copy = true
        } else {
            copy = false
        }
    
    })
}
