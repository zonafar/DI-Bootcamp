// /////////////////
let div = document.getElementById("container");
console.log(div);
//  Changer pete en richard
document.getElementsByTagName("li")[1].innerHTML ="Richard";
// ////////////////Remplacer 
// let ul = document.querySelectorAll(".list > li");
// // console.log(ul)
// for (let i of ul){
//     i.innerHTML = "ZONA";
// }
// ////////////////Supprimmer Sarah
let parent = document.getElementsByClassName("list")[1];
console.log(parent)
parent.removeChild(document.getElementsByTagName("li")[3]);

// //////////////// Add a class called student_list
let uls = document.querySelectorAll(".list");
for (let i of uls){
    i.classList.add("student_list");
}
console.log(document.getElementsByTagName("ul")[0].className);
