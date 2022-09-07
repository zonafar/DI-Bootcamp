// /////////////////////////////////////
//   Daily Challenge GOLD: Bubble Sort
// ////////////////////////////////////
const numbers = [5,0,9,1,7,4,2,6,3,8];
let swapper;
let convertToString = numbers.toString();
console.log(convertToString);
let convertJoin = numbers.join("");
console.log(convertJoin);
console.log("Before sorting: "+numbers);

for (const i in numbers ) {
    for (const j in numbers) {
        if (numbers[i]>numbers[j]) {
            swapper=numbers[i];
            numbers[i]=numbers[j];
            numbers[j]=swapper;
        }
    }
}
console.log("After sorting: "+numbers);