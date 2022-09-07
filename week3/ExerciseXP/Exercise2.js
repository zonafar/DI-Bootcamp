// Add a “light blue” background color and some padding to the <div>.
let div = document.getElementsByTagName("div")[0];
let divcolor = div.style.backgroundColor="lightblue";
div.style.padding="10px";
// Do not display the <li> that contains the text node “John”.
let john = document.querySelectorAll("li")[0];
john.style.display = "none";
// Add a border to the <li> that contains the text node “Pete”.
let pete = document.querySelectorAll("li")[1];
console.log(pete);
pete.style.color="red";
pete.style.border = " 10px solid  black";
// Change the font size of the whole body.
let body = document.body;
body.style.fontSize = "24px";
// Bonus
if (divcolor == "lightblue") {
    alert("Hello "+pete.innerHTML+" and "+john.innerText);
}