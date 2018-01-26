// Create a function that reverses a word
function reverseWord(word) {
    let reversedWord;
    
    reversedWord = word.split("").reverse().join("");
    return reversedWord;
}


// Create a function that takes an array of words and returns a new array of the
 // words with each word reversed.

function reverseWords(words) {
    let reversedWords = [];
    
    for (let word of words) {
        reversedWords.push(reverseWord(word));
    }

    return reversedWords;
}

// Generates a random integer, given a max number
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }

// Create a function that returns a random word from an array
function pickRandomWord(words) {
    let randomNum = getRandomInt(words.length);
    return words[randomNum];
}

// Random word from map keys
function pickRandomWordFromKeys(someMap) {
    let keysList = [];
    let keys = someMap.keys();
    for (let key of keys) {
        keysList.push(key);
    }
    return pickRandomWord(keysList);
}

// Create an array of words and save it to a variable. Using your functions create
// a second array of reversed words.

let myWords = ["copper", "explain", "ill-fated", "truck",
           "neat", "unite", "branch", "educated",
           "tenuous", "hum", "decisive", "notice"];

let reversedMyWords = reverseWords(myWords);

// We could use the two arrays we've created to select a random word to show the user
// and check their guess. How could we do that? Is there a better way?


// ////////////////////////////////////////////////////////////////////////////

// Create a function that takes an array of words and returns a map with the keys
// as the reversed word and the values as the original word.

function mapWordsToReversed(words) {
    let wordsMap = new Map();
    let reversedWords = reverseWords(words);

    for (let i = 0; i < words.length; i++) {
        wordsMap.set(reversedWords[i], words[i]);
    }
    return wordsMap;
}

// Checks to see if user guess was correct. Return true/false.
function checksGuess(guess, word) {
    if (guess === word) {
        return true;
    }
    return false;
}

// FOR TESTING
// let m = mapWordsToReversed(myWords);
// let rv = checksGuess('copper', 'copper', m)
// console.log(rv);

// ////////////////////////////////////////////////////////////////////////////
// FURTHER STUDY

// Create a function that scrambles a word. Use whatever method you like to
// rearrange the letters.

function shuffleWord (word) {
    let wordChars = word.split("");
    let n = wordChars.length;
    // Implement Fisher-Yates shuffling algorithm
    for (let i = n-1; i > 0; i--) {
        let j = getRandomInt(n);
        let temp = wordChars[i];
        wordChars[i] = wordChars[j];
        wordChars[j] = temp;
    }
    return wordChars.join("");
}

// Given an array of words, returns an array of shuffled words.
function shuffleWords (words) {
    let shuffledWords = [];
    for (let word of words) {
        shuffledWords.push(shuffleWord(word));
    }
    return shuffledWords;
}

// Create a function that takes an array of words and returns a map with the
// scrambled words as the keys and the original word as the values.

function generateShuffledWordsMap (words) {
    let shuffledWordsMap = new Map();
    let shuffledWords = shuffleWords(words);

    for (let i = 0; i < words.length; i++) {
        shuffledWordsMap.set(shuffledWords[i], words[i]);
    }
    return shuffledWordsMap;
}