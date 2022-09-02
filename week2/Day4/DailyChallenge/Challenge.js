// /////////////////////////////////////
// This section permit to ask user for word one by one
// ////////////////////////////////////
// let words = [];let word;
// do {
//     word = prompt("Propose a word! -- Type (Enter) to stop");
//     if (word && !Number(word)) {
//         words.push(word)
//     }
// } while (word);
// console.log(words);

// /////////////////////////////////////
// This section permit to ask user for words separate by comma
// ////////////////////////////////////
// Hello,word,in,a,frame
let sentence = prompt("Put several words (separated by commas)");
let words = sentence.split(",")
console.log(words);
let longWord=0;
for (let i of words){
    if (i.length > longWord) {
        longWord = i.length;
    }
}
console.log(longWord);
let margin;
console.log("*".repeat(longWord+4));
for (const t of words) {
    margin = longWord - t.length;
    console.log("* "+t+" ".repeat(margin)+" *");
}
console.log("*".repeat(longWord+5));
