// console.log("successful import")
function dropinfo(currentId) {
    const sepEv = document.getElementById("mi_"+currentId);
    const posMatch = document.getElementById("im_"+currentId);
    sepEv.classList.toggle("active");
    posMatch.classList.toggle("active-pos");
}

function showopts() {
    const getw = document.querySelector(".advanced");
    getw.classList.toggle("optstrue");
}


function splitchars() {
    const tosplit = document.querySelectorAll(".split");
    
}