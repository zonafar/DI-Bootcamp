// /////////////////////////////////////
//  Daily challenge
// ////////////////////////////////////
let sentence = prompt("Enter a sentence which contains the words “not” and “bad”");
let WordBad = sentence.indexOf("bad");
let WordNot = sentence.indexOf("not");
console.log(WordBad,WordNot);
if (WordNot < WordBad && WordNot>0) {
    let ToReplace = sentence.slice(WordNot,(WordBad + 4));
    let result =sentence.replace(ToReplace,"good");
    console.log(result);
} else{
    console.log(sentence);
}