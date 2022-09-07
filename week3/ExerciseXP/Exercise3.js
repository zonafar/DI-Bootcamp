// change the value of the id attribute from navBar to socialNetworkNavigation
document.querySelector("div").setAttribute("id","socialNetworkNavigation");
console.log(document.querySelector("div").id)
// We are going to add a new <li> to the <ul>
let newli = document.createElement('li');
let textNewli = document.createTextNode('logout');
newli.appendChild(textNewli);
document.querySelector("ul").appendChild(newli); 
// Bonus
let first = document.querySelector("ul").firstElementChild;
let last = document.querySelector("ul").lastElementChild;
console.log("first element: "+first.textContent);
console.log("last element: "+last.textContent);