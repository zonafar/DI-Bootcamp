// /////////////////////////////////////
// Exercise 1: Simple If/Else Statement
// ////////////////////////////////////
let x=46,y=230;
if (x>y) {
    console.log("x is the biggest number")
}else{
    console.log("y is the biggest number")
}

// /////////////////////////////////////
// Exercise 2: Chihuahua
// ////////////////////////////////////
let newDog = "Chihuahua";
console.log(newDog.length)
// display in uppercase and then in lowercase
console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())
// check
if (newDog == "Chihuahua") {
    console.log("I love Chihuahuas, it’s my favorite dog breed")
} else {
    console.log("I dont care, I prefer cats")  
}

// /////////////////////////////////////
//  Exercise 3: Even Or Odd
// ////////////////////////////////////
let number = Number(prompt("please enter any number!"))
if(number % 2 == 0){
    console.log(number+" is an even number");
}else{
    console.log(number+" is an odd number");
}
// /////////////////////////////////////
//  Exercise 4: Group Chat
// ////////////////////////////////////
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000","remi689"];
if (users.length == 0) {
    console.log("no one is online")
} else if(users.length == 1) {
    console.log(users[0]+" is online")
} else if(users.length == 2) {
    console.log(users[0] + " and "+users[1] + " are online.")
} else if(users.length > 2) {
    let others = (users.length - 2);
    console.log(users[0] + " "+ users[1] +" and "+ others + " and are online.")
}