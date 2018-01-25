// Arrays

// Declare a variable greeting and assign to it a phrase.
let greeting = 'hello';

// Split a string into an array of characters (see the .split() method)
let greetingChars = greeting.split("");

// Take an array of letters and merge them into a string (see the .join() method)
let greetingString = greetingChars.join("");

// Select a random item from an array (Read up on Math.random() to figure out how to choose a random item from your array. JavaScript doesn’t have Python’s random.choice() function at the ready, so we get to do it ourselves!)

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

let foodsArray = ['eggs', 'rice', 'brussel sprouts', 'curry'];

function getRandomFood(mArray) {
    let arrayLength = mArray.length;
    let randomNum = getRandomInt(arrayLength);
    let randomFood = foodsArray[randomNum];

    return randomFood;
}
 
// Select two random items from an array and swap them

function swapItems(mArray) {
    let swappedArray = mArray.slice();
    let randomNum1, randomNum2;

    randomNum1 = getRandomInt(mArray.length);
    randomNum2 = getRandomInt(mArray.length);

    while (randomNum2 === randomNum1) {
        randomNum2 = getRandomInt(mArray.length);
    }

    swappedArray[randomNum2] = mArray[randomNum1];
    swappedArray[randomNum1] = mArray[randomNum2];

    console.log(`Original array: ${mArray}`);
    console.log(`Swapped array: ${swappedArray}`);

    return swappedArray;
}

// Maps
// Create an empty map and assign it to the variable candy
let candy = new Map();

// Set five colors as keys in the map and flavors as the values, for instance “purple” could be “grape”.
candy.set('green', 'apple')
     .set('purple', 'grape')
     .set('orange', 'orange')
     .set('yellow', 'lemon')
     .set('blue', 'blueberry');

//Iterate over the candy flavors to print “The x flavor is colored y.” for each
for (let [color, flavor] of candy.entries()) {
    console.log(`“The ${flavor} flavor is colored ${color}.`);
}


// Get the value of a color from the map, and see what happens when you try getting a value of a color that doesn’t exist.
console.log("blue flavor: ", candy.get('blue'));
console.log("black flavor: ", candy.get('black'));

/*
Functions
Write a function that takes a color and the candy map. It should return the flavor or if it’s not in the map, console log “Sorry, that color doesn’t have a flavor” and return nothing.
*/
function getFlavor(color, candyMap) {
    if (candyMap.get(color)) {
        return candyMap.get(color); 
    } else {
        console.log("Sorry, that color doesn’t have a flavor");
    }
}

/*
Write a function that takes an array of colors and returns an array of the corresponding flavors. If the map doesn’t have the color, add null to the array.
*/

// Test array
let colorsArray = ['green', 'yellow', 'red'];

function getFlavors(colors, candyMap) {
    let flavors = [];
    // for let color of colors

    for (let color of colors) {
        if (candyMap.get(color)) {
            flavors.push(candyMap.get(color));
        } else {
            flavors.push(null);
        }
    }

    return flavors;
}

console.log(getFlavors(colorsArray, candy));