// /////////////////////////////////////
// nested loops
// ////////////////////////////////////
// Starts the timer
console.time("MyTimer");
let string = "";
let k = 1;
for (let i = 1; i < 8; i++) {
    while (k<i) {
        string  = string  + " *";
        k++;
    }
    console.log(`${string }`)
    
}
// Ends the timer and outputs the time in milliseconds
console.timeEnd("MyTimer");

// /////////////////////////////////////
// one loop
// ////////////////////////////////////
// Starts the timer
console.time("MyTimer");
let s = " *";
let j = 1;
for (let i = 1; i < 7; i++) {
    console.log(`${s.repeat(i)}`)
}
// Ends the timer and outputs the time in milliseconds
console.timeEnd("MyTimer");