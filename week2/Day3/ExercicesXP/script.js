// /////////////////////////////////////
//   Exercise 1 : List Of People
// ////////////////////////////////////
// let people = ["Greg", "Mary", "Devon", "James"];
// // remove “Greg”
// people.shift();
// //  replace “James” to “Jason”
// people[2] = "Jason";console.log(people);
// // add your name to the end
// people.push('gafar')
// // console.logs Mary’s index
// let mary = people.indexOf("Mary")
// console.log(mary);
// // make a copy of the people array using the slice method
// let copy = people.slice((mary + 1),(people.length - 1))
// console.log(copy);
// // gives the index of “Foo”
// console.log(people.indexOf("foo")) // expected result : -1, cause "foo" not in people 
// // Create a variable called last which value is the last element of the array
// let last = people[people.length-1];
// console.log(last);
// console.log("//////////////////////////");
// // iterate each person
// for (const k of people) {
//     console.log(k);
// }
// console.log("//////////////////////////");
// // iterate and exit the loop after you console.log “Jason”
// for (const k of people) {
//     if (k == "Jason") {
//         break;
//     }
//     console.log(k);
// }
// /////////////////////////////////////
//    Exercise 2 : Your Favorite Colors
// ////////////////////////////////////
// let color = ["Red", "Purple", "Blue", "Green"];
// let suffixe = ["st","nd","rd","th"]
// for (let i in color){
//     let j = Number(i)+1;
//     console.log(`My ${j}${suffixe[i]} choice is ${color[i]} `)
// }

// /////////////////////////////////////
//    Exercise 3 : Repeat The Question
// ////////////////////////////////////
// let number;
// do {
//     number = Number(prompt("Enter a number"));
//     while (!number) {
//         console.log("not a number")
//         number = Number(prompt("Enter a true number please"));
//     }
// }while (number < 10)

// /////////////////////////////////////
//    Exercise 4 : Building Management
// ////////////////////////////////////
// let building = {
//     numberOfFloors : 4,
//     numberOfAptByFloor : {
//         firstFloor : 3,
//         secondFloor : 4,
//         thirdFloor : 9,
//         fourthFloor : 2,
//     },
//     nameOfTenants : ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan :  [4, 1000],
//         david : [1, 500],
//     },
// }

// // the number of floors
// console.log(building.numberOfFloors);
// // how many apartments are on the floors 1 and 3
// console.log("apartments on the floor 1: "+building.numberOfAptByFloor.firstFloor)
// console.log("apartments on the floor 1: "+building.numberOfAptByFloor.thirdFloor)
// // name of the second tenant and the number of rooms he has in his apartment
// console.log("name of the second tenant: "+building.nameOfTenants[1]);
// console.log("his appartement: "+building.numberOfRoomsAndRent.dan[0]);
// // Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent
// let davSarah = building.numberOfRoomsAndRent.david[1] + building.numberOfRoomsAndRent.sarah[1];
// let dan = building.numberOfRoomsAndRent.dan[1];
// if (davSarah > dan) {
//     building.numberOfRoomsAndRent.dan[1] = 1200;
//     console.log("After the increase: "+building.numberOfRoomsAndRent.dan[1]);
// }

// /////////////////////////////////////
//   Exercise 5 : Family
// ////////////////////////////////////
// let family={grandfather : "Bwa",grandmother:"mami",father:"fa",mother:"Na",son:"dentchiè"};
// for (let property in family){
//     console.log(property);
// }
// console.log("//////////////////////")
// for (let property in family){
//     console.log(family[property]);
// }

// /////////////////////////////////////
//   Exercise 6
// ////////////////////////////////////
// let details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
//   }
// for (let k in details) {
//     console.log(`${k} ${details[k]}`)
// }

// /////////////////////////////////////
//   Exercise 7 : Secret Group
// ////////////////////////////////////
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"].sort();
let secret="";
for (let letter in names){
    secret = secret + names[letter].slice(0,1)
}
console.log("Secret society name: "+secret)