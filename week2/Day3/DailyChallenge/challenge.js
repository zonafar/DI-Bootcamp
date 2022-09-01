// nested loops
let string = "";
let k = 1;
for (let i = 1; i < 8; i++) {
    while (k<i) {
        string  = string  + " *";
        k++;
    }
    console.log(`${string }`)
    
}
// one loop
let s = " *";
let j = 1;
for (let i = 1; i < 7; i++) {
    console.log(`${s.repeat(i)}`)
}
