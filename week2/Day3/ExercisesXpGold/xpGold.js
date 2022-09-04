// /////////////////////////////////////
//   Exercise 1 : Divisible By Three
// ////////////////////////////////////
let numbers = [123, 8409, 100053, 333333333, 7];

for (i of numbers){
    if (i%3 == 0) {
        console.log(true);
    } else{
        console.log(false);
    }
}

// /////////////////////////////////////
//   Exercise 2 : Attendance
// ////////////////////////////////////
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }

//   console.log(guestList["karl"]);

let student = prompt("What i your name?");
if (guestList[student]) {
    console.log(`Hi! I'm ${student}, and I'm from ${guestList[student]}.`)
} else{
    console.log("Hi! I'm a guest.")
}

// /////////////////////////////////////
//   Exercise 3 : Playing With Numbers
// ////////////////////////////////////
let age = [20,5,12,43,98,55];
let sum=0,hight = 0;
for (const i of age) {
    sum = sum + i;
    if (i>hight) {
        hight = i;
    }
}
console.log("Sum of age : "+sum);
console.log("Highest age : "+hight);