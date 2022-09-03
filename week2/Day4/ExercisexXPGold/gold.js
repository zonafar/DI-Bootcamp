// /////////////////////////////////////
// Exercise 1 : Is_Blank
// ////////////////////////////////////
function isBlank(para) {
    if (!para) {
        return true;
    }
    return false;
}
console.log(isBlank(''));
console.log(isBlank('abc'));

// /////////////////////////////////////
// Exercise 2 : Abbrev_name
// ////////////////////////////////////
function abbrevName(para) {
    let arr = para.split(" ");
    let result = arr[0];
    for (let i = 1; i < arr.length; i++) {
        result = result + " " + arr[i].slice(0,1)+".";
    }
    return result;
}
// let x="Robin Singh";

console.log(abbrevName("Robin Singh"));

// /////////////////////////////////////
// Exercise 3 : SwapCase
// ////////////////////////////////////
function swapCase(params) {
    let str = "";
    for (c in params){
        if (params[c] === params[c].toLowerCase()) {
            str = str + params[c].toUpperCase();
        }else if(params[c] === params[c].toUpperCase()){
            str = str + params[c].toLowerCase();
        } else{
            str = str + params[c];
        }
    }
    return str;
}

console.log(swapCase("The Quick Brown Fox"))

// /////////////////////////////////////
// Exercise 4 : Omnipresent Value
// ////////////////////////////////////
// function isOmnipresent(v) {
    // let v= [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]];
//     let res = true;
//     for (let i in v){
//         for (let j in v[i]) {
//             for (const key in v) {
//                 const found = v[key].find(element => element == j);
//                 if (!found) {
//                     res = false; 
//                 }
//             }
//             if (res == true) {
//                 return true;
//             }
//         }
//     }
//     return false;
// }

// console.log(isOmnipresent([[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]));
// console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6));
// console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1))

// let omni = [[1, 1], [1, 3], [5, 1], [6]];
// let omni = [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]];
function isOmnipresent(omni){
    let found,res = 0;
    for (let i = 0; i < omni.length; i++) {
        for (let j = 0; j < omni[i].length; j++) {
            for (let k = 0; k < omni.length; k++){
                found = omni.find(elem => elem == k );
                // console.log(found)
                if (found == k) {
                    res += 1;
                }
                // console.log(omni[i][j]); 
            }
            if (res == omni.length) {
                return true;
            }
        }
        // console.log("++++++++");
    }
    return false;
}
// console.log(isOmnipresent([[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]));
// console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6));
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6,1]]))


