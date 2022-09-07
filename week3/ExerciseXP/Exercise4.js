let allBooks = [
    Book1={
        title:"48 low of power",
        author:"Robert",
        image:"https://pictures.abebooks.com/isbn/9780670881468-fr.jpg",
        alreadyRead : false
    },
    Book2={
        title:"Secrets from the new science of expertise",
        author:"Anders Ericsson,Robert Pool",
        image:"https://i1.sndcdn.com/artworks-V7vNGLqaDT53tuE2-wTzPHw-t500x500.jpg",
        alreadyRead : true
    }
]
console.log(allBooks);

// Create node
let table = document.createElement('table');
table.setAttribute("class","tab");
table.style.border = "2px solid";
table.style.borderCollapse = "collapse";
table.style.fontSize="20px";

allBooks.forEach(MyFunction)
function MyFunction(elem) {
    // Create node
    let tr = document.createElement('tr');
    let td1 = document.createElement('td');
    let td2 = document.createElement('td');
    let img = document.createElement('img');
    // Nested elements
    let text = document.createTextNode(elem.title+ " written by "+ elem.author);
    td1.appendChild(text);
    td2.appendChild(img);
    tr.appendChild(td1);
    tr.appendChild(td2);
    table.appendChild(tr);
    // Add attribute and content
    img.setAttribute("src",elem.image);
    img.style.width = "100px";
    img.style.height = "100px";
    img.style.borderRadius="50%";
    tr.setAttribute("class","tab");
    td1.setAttribute("class","tab");
    td2.setAttribute("class","tab");
    td1.style.border = "2px solid";
    td1.style.borderCollapse = "collapse";
    td2.style.border = "2px solid";
    td2.style.borderCollapse = "collapse";
    if (elem.alreadyRead) {
        td1.style.color="red";
    }
}

document.body.appendChild(table);

console.log(table);