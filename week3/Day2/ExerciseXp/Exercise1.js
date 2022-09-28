// Using a DOM property, retrieve the h1 and console.log it.
let h1 = document.querySelector("h1")
console.log(h1);

// Using DOM methods, remove the last paragraph in the <article> tag.
let allP = document.querySelectorAll("p");
allP[3].remove();
// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
let h2 = document.querySelector("h2");
// 1st way
let f = function bgr_red(){
    h2.style.backgroundColor = "red";
}
h2.onclick = f;
// 2st way
h2.addEventListener("click",bg_red)
function bg_red(){
    h2.style.backgroundColor = "blue";
}
// Add an event listener which will hide the h3 when it’s clicked on 
let h3 = document.querySelector("h3");
let hide = function (){
    h3.style.display = "none";
}
h3.onclick = hide;
// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold

let btText = document.createTextNode("Bold");
let bt = document.createElement("button");
bt.appendChild(btText);
document.querySelector("article").appendChild(bt);
bt.addEventListener("click",bold)
function bold() {
    let all_p = document.querySelectorAll("p");
    for (const e of all_p) {
        e.style.fontWeight = "bold";
    }
}

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.

h1.addEventListener("mouseover",setFont);
function setFont(params) {
    h1.style.fontSize = Math.random()*100 + "px";
}


allP[1].addEventListener("mouseover",fadeP);
function fadeP(params) {
    allP[1].style.opacity = "20%";
    allP[1].style.transition = "opacity 1s";
}
