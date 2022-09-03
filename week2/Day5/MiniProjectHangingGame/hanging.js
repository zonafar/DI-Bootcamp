console.log(`++++++++++++++++++`);
console.log(`++ Hanging Game ++`);
console.log(`++++++++++++++++++`);
let word;
do {
    word= prompt("Player1 must Enter a minimum of 8 letters");
} while (word.length<8);
let player1= word.split("");
let hiddenWord = "*".repeat(player1.length);
let hidden = hiddenWord.split("");
let apear;
let player2,limit=0;


function Initi() {
    for (const k in player1) {
        if (player2 == player1[k]) {
            hidden[k]=player1[k];
        }
    }
    console.log(Apearent());
    let ap = Apearent()
    if (ap.indexOf("*") < 0) {
        console.log("CONGRATS YOU WIN");
        limit=11;
    }
    if (limit == 9) {
        console.log("YOU LOSE");
    }
}

function Apearent() {
    apear = "";
    for (i in hidden){
        apear = apear + hidden[i];
    }
    return apear;
}

while (limit<10) {
    player2= prompt("Player1 : Guess a letter");
    Initi();
    limit++;
}

