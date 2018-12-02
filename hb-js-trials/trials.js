// ///////////////////////////////////////////////////////
// PART 1
// Account information:

let accountHolder = "Balloonicorn";
const accountNumber = "123456";
let businessName = "Balloonicorn's Cupcake Shop";

const addresses = ["123 Main Street", "683 Sutter Street", "1600 Pennsylvania Ave"];

const phoneNumbers = new Map();

// console.log('account holder');

// Add some phone numbers to our map

phoneNumbers.set("home", "510-867-5309")
.set("mobile", "415-555-1212")
.set("business", "415-123-4567");


// ///////////////////////////////////////////////////////
// Create User Info Display:

// Add function to print account information

function printAccountInformation(accountHolder, accountNumber, businessName) {
    console.log(`Account Holder: ${accountHolder}`);
    console.log(`Account Number: ${accountNumber}`);
    console.log(`Business Name: ${businessName}`);
}


// Add function to print all addresses, including a header

function showAddresses(addresses) {
    console.log("Addresses:");

    for (let address of addresses) {
        console.log(address);
    }
}

// Add function to print phone types and numbers
function showPhones(phoneNumbers) {
    console.log("Phone Numbers:")

    for (let [numberType, number] of phoneNumbers) {
        console.log(numberType + ": " + number);
    }
}

// ///////////////////////////////////////////////////////
// Transactions:

// Create a map of transactions
let transactions = new Map([
    ['May-2', -500],
    ['May-13', 1,200],
    ['May-15', -100],
    ['May-21', -359],
    ['May-29', 2,200],
]);

// Add function to add transactions
function addTransaction(date, amount) {
    transactions.set(date, amount);
}

// Add function to show balance status
function showBalanceStatus(amount) {

    console.log(`Current Balance: ${amount}`);

    if (amount < 0) {
        console.log("YOU ARE OVERDRAWN");
    } else if (amount < 20) { 
        console.log("Warning: You are close to zero balance");
    } else {
        console.log("Thank you for your business.")
    }
}

// Add function to show transactions
function showTransactions(transactions, startBalance) {
    var balanceAmount = startBalance;

    console.log(startBalance);
    for (let [date, transactionAmount] of transactions) {
        var transactionType;

        if (transactionAmount > 0) {
            transactionType = 'Deposit';
        } else {
            transactionType = 'Withdrawal';
        }

        balanceAmount += transactionAmount;
        console.log(date + " " + transactionType + ": " + transactionAmount);
        console.log("Balance: " + balanceAmount);
    }

    if (balanceAmount < 0) {
        balanceAmount -= 25;
        console.log("Balance has dropped below $0.00. You've been charged $25.")
    }

    showBalanceStatus(balanceAmount);
}




// ///////////////////////////////////////////////////////
// All Customer Info:

// Make an Object of customer info

let customer = {
    accountHolder,
    accountNumber,
    businessName,
    addresses,
    phoneNumbers,
    transactions,
    startingBalance: 260000
}


// Function to add customer attributes
function updateCustomer(favoriteMelon='Canteloupe', numPets=0) {
    customer['favoriteMelon'] = favoriteMelon;
    customer['numPets'] = numPets;
}

// ///////////////////////////////////////////////////////
// Getting a Business Loan
function getInterestRate(income, customer) {
    let isPreferred, interestRate;

    if (customer['favoriteMelon'] === 'Casaba' || customer['numPets'] > 5) {
        isPreferred = true;
    } else {
        isPreferred = false;
    }


    if (income < 100000 && isPreferred ) {
        interestRate = 0.05;
    } else if (income < 100000 && !isPreferred) {
        interestRate = 0.08;
    } else if ((income >= 100000 && income <= 200000) && isPreferred) {
        interestRate = 0.04;
    } else if ((income >= 100000 && income <= 200000) && !isPreferred) {
        interestRate = 0.07;
    } else {
        interestRate = 0.04;
    }

}

// Function to return loan rate


// ///////////////////////////////////////////////////////
// Account Report


// Add function to show bank customer report



// ///////////////////////////////////////////////////////
// PART 2:
// Bank Manager

// Create map of customer addresses


// Write a function to return the address of a given person


// Add a function to create an employee schedule for the week 


// Add a function for weekly hours






