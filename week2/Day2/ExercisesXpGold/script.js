// /////////////////////////////////////
//  Exercise 1 : The World Translator
// ////////////////////////////////////

let speak = prompt("Wich language do you speak?");

switch (speak.toLocaleLowerCase()) {
    case "english":
        console.log("Hello");
        break;
    case "french":
        console.log("Bonjour");
        break;
    case "hebrew":
        console.log("Shalom");
        break;
    case "bambara":
        console.log("Aw ni sogoma");
        break;

    default:
        console.log("01110011 01101111 01110010 01110010 01111001");
        break;
}

// /////////////////////////////////////
//  Exercise 2 : The Grade Assigner
// ////////////////////////////////////
let grade;
do {
    grade = Number(prompt("Wath is your grade?"));
} while (!grade);

if(grade>90){
    console.log("A");
} else if(grade>80 && grade<90){
    console.log("B");
}  else if(grade>70 && grade<80){
    console.log("C");
} else{
    console.log("D");
}


// /////////////////////////////////////
//  Exercise 3 : Verbing
// ////////////////////////////////////

let string = prompt("Enter a string ( It must be a verb)");

if (string.length > 3 && string.endsWith("ing")) {
    string = string + "ly"
} else if (string.length > 3 && !string.endsWith("ing")) {
    string = string + "ing"
}

console.log(string);