
// /////////////////////////////////////
// Mini project : Play the game
// ////////////////////////////////////
function playTheGame() {
    let choice = confirm("Do you want to play the game?");
    let number;
    if (!choice) {
        alert("No problem, Goodbye")
    } else{
        number = prompt("Enter a number between 0 to 10")
        if (!number) {
            alert("Sorry Not a number, Goodbye")
        } else if(number<0 && number>10){
            alert("Sorry it’s not a good number, Goodbye")
        } else {
            let computerNumber = Math.floor(Math.random() * 11);
            console.log(computerNumber);
            compareNumbers(number,computerNumber);
        }
    }
}

function compareNumbers(userNumber,computerNumber) {
    let out=0; let i=0;
    do {
        if (userNumber == computerNumber) {
            alert("WINNER") ;
            out = 1;
            break;
        } else if(userNumber > computerNumber){
            if (i<2) {
                userNumber = prompt("Your number is bigger then the computer’s, guess again");
            }
        } else {
            if (i<2) {
                userNumber = prompt("Your number is smaller then the computer’s, guess again");
            }
        }
        i++;
    } while (i < 3);
    if (out == 0) {
        alert("out of chances");
    }
  }
