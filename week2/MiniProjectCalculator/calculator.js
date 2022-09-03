// //////////////////////
// Declarations
// //////////////////////

let log = "";
const screen = document.getElementById("screen");
// 2. Create a new <p></p> element programmatically
const sp = document.createElement("span");

// //////////////////////
//
// //////////////////////
function show(para){
    // 3. Add the text content
    sp.textContent = para;
    // 4. Append the span element to the div element
    screen?.appendChild(sp);
}

function number(n) {
    log = log + n;
    show(log);
    console.log(log);
}

function operator(o) {
    log = log + o;
    show(log);
    console.log(log);
}

function equal() {
    show(eval(log));
    log = "";
}

function cleared() {
    let length = log.length;
    log = log.substring(0,length-1);
    show(log);
    console.log(log);
}

function reset() {
    log = "";
    show(" ");
}

