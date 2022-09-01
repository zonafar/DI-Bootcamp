// /////////////////////////////////////
//  Exercise 1 : Information
// ////////////////////////////////////
// // Part 1
// function infoAboutMe(){
//     console.log("My name: Gafar");
//     console.log("My age: 22");
//     console.log("My hobbies: films series and football");
// }
// infoAboutMe();
// // Part 2
// function infoAboutPerson(personName, personAge, personFavoriteColor) {
//     console.log(`You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`);
// }
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

// /////////////////////////////////////
//  Exercise 2 : Tips
// ////////////////////////////////////
// function calculateTip() {
//     let amount;
//     do {
//         amount = Number(prompt("What is the amount of the bill ?"));
//     } while (!amount || amount < 0);
//     if (amount < 50) {
//         console.log(`Tip amount: 20%`)
//         console.log(`Finall bill: ${amount + (amount*0.2)}`)
//     } else if(amount >= 50 && amount <= 200){
//         console.log(`Tip amount: 15%`)
//         console.log(`Finall bill: ${amount + (amount*0.15)}`)
//     } else{
//         console.log(`Tip amount: 10%`)
//         console.log(`Finall bill: ${amount + (amount*0.1)}`)
//     }
// }
// calculateTip()

// /////////////////////////////////////
//   Exercise 3 : Find The Numbers Divisible By 23
// ////////////////////////////////////
// function isDivisible(){
//     let sum=0;
//     for (let index = 0; index < 500; index++) {
//         if (index%23 == 0) {
//             sum = sum + index;
//             console.log(index)
//         }
//     }
//     console.log("Sum : "+sum)
// }
// isDivisible()
// // Bonus
// function isDivisible(divisor){
//     let sum=0;
//     for (let index = 0; index < 500; index++) {
//         if (index%divisor == 0) {
//             sum = sum + index;
//             console.log(index)
//         }
//     }
//     console.log("Sum : "+sum)
// }
// isDivisible(45)

// /////////////////////////////////////
//  Exercise 4 : Shopping List
// ////////////////////////////////////
// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// let shoppingList = ["banana","orange","apple"]
// function myBill() {
//     let bill,price = 0 ;
//     for (const k in shoppingList) {
//         let check = Number(stock[shoppingList[k]])
//         if (check > 0) {
//             price = price + Number(prices[shoppingList[k]])
//             stock[shoppingList[k]] = Number(stock[shoppingList[k]]) - 1 // Bonus
//         }
//     }
//     console.log("Total price: "+price)
// }
// myBill()
// console.log(stock)

// /////////////////////////////////////
//  Exercise 5 : What’s In My Wallet ? 
// ////////////////////////////////////
// function changeEnough(itemPrice, amountOfChange) {
//     let change = [0.25, 0.10, 0.05, 0.01];let amount = 0;
//     for (let index = 0; index < change.length; index++) {
//         amount = amount + (change[index] * amountOfChange[index])
//     }
//     if (amount < itemPrice) {
//         return false;
//     } else {
//         return true;
//     }
// }
// console.log(changeEnough(4.25, [25, 20, 5, 0]))
// console.log(changeEnough(14.11, [2,100,0,0]))
// console.log(changeEnough(0.75, [0,0,20,5]))

// /////////////////////////////////////
// Exercise 6 : Vacations Costs
// ////////////////////////////////////
// 1
function hotelCost() {
    let nights;const perNight=140;
    do {
        nights = Number(prompt("How many of nights would you like to stay in the hotel?"));
    } while (!nights || nights < 0);
    return nights * perNight
}
// console.log(hotelCost())

// 2
function planeRideCost() {
    let dest
    do {
        dest = prompt("What is your destination?");
    } while (!dest || Number(dest) );
    if (dest == "London") {
        return 183;
    } else if(dest == "Paris"){
        return 220;
    } else{
        return 300;
    }
}
// console.log(planeRideCost())

// 3
function rentalCarCost(){
    let days;const cost = 40;
    do {
        days = Number(prompt("How many of days would you like to rent the car.?"));
    } while (!days || days < 0);
    if (days>10) {
        return (days*cost)-(days*cost*0.05) 
    }
    return days*cost
}
// console.log(rentalCarCost());

// 4
function totalVacationCost() {
    return hotelCost() + planeRideCost() + rentalCarCost();
}
console.log(totalVacationCost())