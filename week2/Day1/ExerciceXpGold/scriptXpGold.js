
// /////////////////////////////////////
// Exercise 1 : Favorite color
// ////////////////////////////////////
let sentence = ["my","favorite","color","is","blue"];
let join = sentence.join();
console.log(join)


// /////////////////////////////////////
// Exercise 2 : Mixup
// ////////////////////////////////////
let str1 = "Hello";
let str2 = "World";

let start1 = str1.substring(0,2);
let end1 = str1.substring(2);
let start2 = str2.substring(0,2);
let end2 = str2.substring(2);

let newstr1 = start1.concat(end2)
let newstr2 = start2.concat(end1)
console.log("newWord should be equal to : "+newstr2 +" "+newstr1)

// /////////////////////////////////////
// Exercise 3 : Calculator
// ////////////////////////////////////
/**Addition*/ 
let num1 = Number(prompt("Enter your first number"));
let num2 = Number(prompt("Enter your second number"));
console.log("result : "+(num1+num2))
/**Multiplication*/ 
let mult1 = Number(prompt("Enter your first number"));
let mult2 = Number(prompt("Enter your second number"));
console.log("result : "+(mult1+mult2))
