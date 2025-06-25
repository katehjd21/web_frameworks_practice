
let favouriteColour;
const defaultColour = document.getElementById("favourite-colour").value;

document.addEventListener("DOMContentLoaded", startup)

function startup() {
    favouriteColour = document.getElementById("favourite-colour")
    favouriteColour.addEventListener("input", updateTextColour)
    
}

function updateTextColour(event) {
    // const h1 = document.getElementsByTagName("h1")
    // const p = document.getElementsByTagName("p")
    const allText = document.getElementsByClassName("colour-change")
    // if (h1 && p) {
    //     h1[0].style.color = event.target.value
    //     p[0].style.color = event.target.value
    // }
    for (let i = 0; i < allText.length; i++) {
        allText[i].style.color = event.target.value
    }
}


    


document.getElementById("favourite-colour").addEventListener("click", (event)=> {console.log(event.target.value)})