
// /////////////////////////////////////
// Exercise 1 : Evaluation
// ////////////////////////////////////
5 >= 1
// Prediction : true
// output : 
0 === 1
// Prediction : false
// output :
4 <= 1
// Prediction : true
// output : false
1 != 1
// Prediction : false
// output : false
"A" > "B"
// Prediction : false
// output : false
"B" < "C"
// Prediction : true
// output : true
"a" > "A"
// Prediction : true
// output :
"b" < "A"
// Prediction : false
// output : false
true === false
// Prediction : true
// output : false
true != true
// Prediction : false
// output : false

// /////////////////////////////////////
// Exercise 2 : Ask for Numbers
// ////////////////////////////////////
let virgule = prompt("Type a number separate by commas. Exemple(2,3)");
let  number = virgule.split(",");
let somme = Number(number[0])+ Number(number[1])
console.log(virgule +" ---> " + somme)

// /////////////////////////////////////
// Exercise 3 : Find Nemo
// ////////////////////////////////////
let sentence = prompt("give a sentence containing the word 'Nemo'"); 
let place = sentence.split(" ")
console.log(place)
if (sentence.search('Nemo') != -1) {
    console.log("I found Nemo at "+sentence.search('Nemo') +" position")
}
if(sentence.search('Nemo') == -1){
    console.log("I can’t find Nemo")
}