const install = document.getElementById("install");
        addEventListener("DOMContentLoaded", e => {
            install.classList.add("big");
            console.log("working")
            setTimeout(function(){
            
                install.classList.add("small")
                install.classList.remove("big")
            },1000);
            
        })
