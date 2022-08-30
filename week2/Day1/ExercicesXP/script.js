
// /////////////////////////////////////
// Exercise 1 : Favorite food
// ////////////////////////////////////
let food = "avocado"
let meal = "dinner"
console.log("I eat " + food + " at every " + meal)


// /////////////////////////////////////
// Exercise 2: Serie
// ////////////////////////////////////
let myWatchedSeries = ["black list", "Game of thrones", "Cameron black","Hunter x hunter","the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;
let myWatchedSeriesSentence = myWatchedSeries.toString();
console.log("I watched " + myWatchedSeriesLength + " series : " +myWatchedSeriesSentence);
/** Part 2*/
myWatchedSeries.splice(4,1)
console.log(myWatchedSeries)
/** another series*/
myWatchedSeries.push("The Outpost")
/** add my favorite series*/
myWatchedSeries.unshift("Naruto")
console.log(myWatchedSeries)
/** Delete the series "black list"*/
myWatchedSeries.splice(1,1)
console.log(myWatchedSeries)
/** the third letter of the series "Hunter x hunter".*/
third = myWatchedSeries[3].substring(2,3)
console.log("The third letter of the serie 'Hunter x hunter' is : "+third)
/** See all the modifications we made*/
myWatchedSeriesSentence = myWatchedSeries.toString() 
console.log(myWatchedSeriesSentence)


// /////////////////////////////////////
// Exercice 3 : Temperature converter
// ////////////////////////////////////
let cels = 10;
let fahr = (cels * 9/5)+32;
console.log(cels + "°C is " + fahr+ "°F")


// /////////////////////////////////////
// Exercice 4: Guess the answers #1
// ////////////////////////////////////
let c;
let a = 34;
let b = 21;
console.log(a+b) //first expression
// Prediction: The output will be 55, cause we done additions of numbers
// Actual: 55
a = 2;
console.log(a+b) //second expression
// Prediction: The output is 23 because the variable a get new value 2
// Actual: 23
// The value of c is undefined


// /////////////////////////////////////
// Exercice 5: Guess the answer #2
// ////////////////////////////////////
typeof(15)
// Prediction: number
// Actual:

typeof(5.5)
// Prediction: float
// Actual: number

typeof(NaN)
// Prediction: null
// Actual: number

typeof("hello")
// Prediction: string
// Actual: string

typeof(true)
// Prediction: boolean
// Actual: boolean

typeof(1 != 2)
// Prediction: boolean
// Actual: boolean

"hamburger" + "s"
// Prediction: hamburgers
// Actual: hamburgers

"hamburgers" - "s"
// Prediction: hamburger
// Actual: NaN

"1" + "3"
// Prediction: "13"
// Actual:

"1" - "3"
// Prediction: "13"
// Actual: "13"

"johnny" + 5
// Prediction: "johnny5"
// Actual:  "johnny5"

"johnny" - 5
// Prediction: 
// Actual: NaN

99 * "hello"
// Prediction: 
// Actual: NaN

1 != 1
// Prediction: false
// Actual: false

1 == "1"
// Prediction: false
// Actual: true

1 === "1"
// Prediction: false
// Actual: false

// /////////////////////////////////////
// Exercise 6 : Guess The Answers #3
// ////////////////////////////////////
5 + "34"
// Prediction: "534"
// Actual:

5 - "4"
// Prediction: NaN
// Actual: -1

10 % 5
// Prediction: 0
// Actual: 0

5 % 10
// Prediction: 5
// Actual: 5

"Java" + "Script"
// Prediction: "JavaScript"
// Actual: "JavaScript"

" " + " "
// Prediction:"  "
// Actual: "  "

" " + 0
// Prediction: " 0"
// Actual: " 0"

true + true
// Prediction: true
// Actual: 2

true + false
// Prediction: false
// Actual: 1

false + true
// Prediction: false
// Actual: 1

false - true
// Prediction: NaN
// Actual: -1

!true
// Prediction: false
// Actual: false

3 - 4
// Prediction: -1
// Actual: -1

"Bob" - "bill"
// Prediction: NaN
// Actual: NaN
