// /////////////////////////////////////
// Exercise 1: Random Number
// ////////////////////////////////////
let random = Math.floor(Math.random()*100);
for (let i = 0; i < random; i++) {
    if (i%2 == 0) {
        console.log(i);
    }
    
}

// /////////////////////////////////////
// Exercise 2: Capitalized Letters
// //////////////////////////////////// 
function capitalize(param) {
    let lower = param.toLowerCase();
    let even = "",odd = "";
    let arr = [];
    for (const i in lower) {
        if (i%2 == 0) {
            even = even + lower[i].toUpperCase();
            odd = odd + lower[i];
        } else{
            even = even + lower[i];
            odd = odd + lower[i].toUpperCase();
        }
    }
    arr.push(even);
    arr.push(odd);
    return arr;
}
console.log(capitalize("param"));



// /////////////////////////////////////
// Exercise 3 : Is Palindrome?
// //////////////////////////////////// 

function checker(params) {
    let center = (params.length/2);
    let check = true;
    let middleR = center;
    let middleL = center;
    for (let i = 0; i < center; i++) {
        check = compare(params[middleL-1],params[middleR+1]);
        if (check == false) {
            return false;
        }
        middleR++;middleL--;

    }
    return true;
}

function compare(a,b) {
    if (a == b) {
        return true;
    } else{
        return false;
    }
}

function palindrome(params) {
    if (checker(params)) {
        console.log("The entry is a palindrome")
    } else{
        console.log("The entry is not a palindrome")
    }
}

palindrome("madam");


// /////////////////////////////////////
//Exercise 4 : Biggest Number
// //////////////////////////////////// 
function biggestNumberInArray(arrayNumber) {
    let big = 0;
    if (arrayNumber.length > 0) {
        for (let i = 0; i < arrayNumber.length; i++) {
            if (big < Number(arrayNumber[i]) && Number(arrayNumber[i])) {
                big = arrayNumber[i];
            }
            
        }         
    }else {
        return big;
    }
    return big;
}
// 
const array = ['a', 3, 4, 2]
console.log(biggestNumberInArray(array))

// /////////////////////////////////////
// Exercise 5: Unique Elements
// //////////////////////////////////// 

function unique(arr) {
    let newArr = [];
    let indice = 0;
    for (let i in arr) {
        for (let j in newArr) {
            if (arr[i] == newArr[j]) {
                indice++;
            }
        }
        if (indice == 0) {
            newArr.push(arr[i]);
        } else{
            indice = 0;
        }
    } 
    return newArr;  
}
console.log(unique([1,2,3,3,3,3,4,5,5,10,10,10]));
