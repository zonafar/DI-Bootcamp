
console.log(`*****************************`);
console.log(`** 99 Bottles Of Beer Game **`);
console.log(`*****************************`);
let bottles = 99;
let decrease = Number(prompt("Enter for a number to begin counting down bottles"));

decrease--;
// for (let i = 0; i < 10; i++) {
do{
    console.log(`${bottles}  bottles of beer on the wall`);
    console.log(`${bottles}  bottles of beer`);
    decrease++;
    bottles = bottles - decrease; 
    if (bottles <= 0) {
        break;
    } else{
        if (decrease == 1) {
            console.log(`Take ${decrease} down, pass it around`);
        } else{
            console.log(`Take ${decrease} down, pass them around`);
        }
        console.log(`${bottles}  bottles of beer on the wall`);
    }
    console.log(`=============`);
}while(bottles > 0) ;