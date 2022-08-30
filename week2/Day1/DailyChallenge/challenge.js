// /////////////////////////////////////
// Exercise 2 
// ////////////////////////////////////
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// 1 Remove Banana
fruits.shift();
console.log(fruits)
// 2 Sort the array
fruits.sort()
console.log(fruits)
// 3 Add “Kiwi” to the end
fruits.push("Kiwi")
console.log(fruits)
// Remove “Apples”
fruits.splice(0,1);
console.log(fruits);
// Sort the array in reverse order
fruits.reverse();
console.log(fruits);

// /////////////////////////////////////
// Exercise 2 
// ////////////////////////////////////
// 1  console.log “Oranges”
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0])