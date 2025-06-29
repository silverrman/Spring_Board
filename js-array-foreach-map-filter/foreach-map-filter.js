/*
Write a function called doubleValues which accepts an array and returns a new array with all the values in the array passed to the function doubled

Examples:
    doubleValues([1,2,3]) // [2,4,6]
    doubleValues([5,1,2,3,10]) // [10,2,4,6,20]

*/
// doubleValues: Returns a new array with all values doubled.
// Uses .map() to transform each element by multiplying by 2.
function doubleValues(arr){
    return arr.map(function(val) {
        return val * 2;
    });
}

/*
Write a function called onlyEvenValues which accepts an array and returns a new array with only the even values in the array passed to the function

Examples:
    onlyEvenValues([1,2,3]) // [2]
    onlyEvenValues([5,1,2,3,10]) // [2,10]

*/
// onlyEvenValues: Returns a new array with only even values from the input array.
// Uses .filter() to include values divisible by 2.
function onlyEvenValues(arr){
    return arr.filter(function(val) {
        return val % 2 === 0;
    });
}

/*
Write a function called showFirstAndLast which accepts an array of strings and returns a new array with only the first and last character of each string.

Examples:
    showFirstAndLast(['colt','matt', 'tim', 'test']) // ["ct", "mt", "tm", "tt"]
    showFirstAndLast(['hi', 'goodbye', 'smile']) // ['hi', 'ge', 'se']

*/
// showFirstAndLast: Returns a new array with only the first and last character of each string.
// Uses .map() to concatenate the first and last character of each string.
function showFirstAndLast(arr){
    return arr.map(function(str) {
        return str[0] + str[str.length - 1];
    });
}

/*
Write a function called addKeyAndValue which accepts an array of objects, a key, and a value and returns the array passed to the function with the new key and value added for each object 

Examples:
    addKeyAndValue([{name: 'Elie'}, {name: 'Tim'}, {name: 'Matt'}, {name: 'Colt'}], 'title', 'instructor') 
    
    // [{name: 'Elie', title:'instructor'}, {name: 'Tim', title:'instructor'}, {name: 'Matt', title:'instructor'}, {name: 'Colt', title:'instructor'}]

*/
// addKeyAndValue: Adds a new key and value to each object in the array.
// Uses .map() to iterate and mutate each object by adding the key and value.
function addKeyAndValue(arr, key, value){
    return arr.map(function(obj) {
        obj[key] = value;
        return obj;
    });
}

/*
Write a function called vowelCount which accepts a string and returns an object with the keys as the vowel and the values as the number of times the vowel appears in the string. This function should be case insensitive so a lowercase letter and uppercase letter should count

Examples:
    vowelCount('Elie') // {e:2,i:1};
    vowelCount('Tim') // {i:1};
    vowelCount('Matt') // {a:1})
    vowelCount('hmmm') // {};
    vowelCount('I Am awesome and so are you') // {i: 1, a: 4, e: 3, o: 3, u: 1};
*/
// vowelCount: Returns an object with the count of each vowel in the string (case-insensitive).
// Uses .toLowerCase(), .split(''), and .forEach() to count vowels, storing results in an object.
function vowelCount(str) {
    const vowels = 'aeiou';
    const result = {};
    str.toLowerCase().split('').forEach(function(char) {
        if (vowels.indexOf(char) !== -1) {
            result[char] = (result[char] || 0) + 1;
        }
    });
    return result;
}

/*
Write a function called doubleValuesWithMap which accepts an array and returns a new array with all the values in the array passed to the function doubled

Examples:
    doubleValuesWithMap([1,2,3]) // [2,4,6]
    doubleValuesWithMap([1,-2,-3]) // [2,-4,-6]
*/

// doubleValuesWithMap: Returns a new array with all values doubled (demonstrates .map()).
function doubleValuesWithMap(arr){
    return arr.map(function(val) {
        return val * 2;
    });
}

/*
Write a function called valTimesIndex which accepts an array and returns a new array with each value multiplied by the index it is currently at in the array.

Examples:
    valTimesIndex([1,2,3]) // [0,2,6]
    valTimesIndex([1,-2,-3]) // [0,-2,-6]
*/

// valTimesIndex: Returns a new array where each value is multiplied by its index.
// Uses .map() with both value and index arguments.
function valTimesIndex(arr){
    return arr.map(function(val, idx) {
        return val * idx;
    });
}

/*
Write a function called extractKey which accepts an array of objects and some key and returns a new array with the value of that key in each object.

Examples:
    extractKey([{name: 'Elie'}, {name: 'Tim'}, {name: 'Matt'}, {name: 'Colt'}], 'name') // ['Elie', 'Tim', 'Matt', 'Colt']
*/

// extractKey: Returns a new array with the value of the given key from each object.
// Uses .map() to extract obj[key] from each object.
function extractKey(arr, key){
    return arr.map(function(obj) {
        return obj[key];
    });
}

/*
Write a function called extractFullName which accepts an array of objects and returns a new array with the value of the key with a name of "first" and the value of a key with the name of  "last" in each object, concatenated together with a space. 

Examples:
    extractFullName([{first: 'Elie', last:"Schoppik"}, {first: 'Tim', last:"Garcia"}, {first: 'Matt', last:"Lane"}, {first: 'Colt', last:"Steele"}]) // ['Elie Schoppik', 'Tim Garcia', 'Matt Lane', 'Colt Steele']
*/

// extractFullName: Returns a new array with full names (first + last) from objects.
// Uses .map() to concatenate obj.first and obj.last.
function extractFullName(arr){
    return arr.map(function(obj) {
        return obj.first + ' ' + obj.last;
    });
}

/*
Write a function called filterByValue which accepts an array of objects and a key and returns a new array with all the objects that contain that key.

Examples:
    filterByValue([{first: 'Elie', last:"Schoppik"}, {first: 'Tim', last:"Garcia", isCatOwner: true}, {first: 'Matt', last:"Lane"}, {first: 'Colt', last:"Steele", isCatOwner: true}], 'isCatOwner') // [{first: 'Tim', last:"Garcia", isCatOwner: true}, {first: 'Colt', last:"Steele", isCatOwner: true}]
*/

// filterByValue: Returns a new array of objects that contain the specified key.
// Uses .filter() and obj.hasOwnProperty(key).
function filterByValue(arr, key){
    return arr.filter(function(obj) {
        return obj.hasOwnProperty(key);
    });
}

/*
Write a function called find which accepts an array and a value and returns the first element in the array that has the same value as the second parameter or undefined if the value is not found in the array.

Examples:
    find([1,2,3,4,5], 3) // 3
    find([1,2,3,4,5], 10) // undefined
*/

// find: Returns the first element in the array that matches searchValue, or undefined if not found.
// Uses .find() to search for a matching value.
function find(arr, searchValue){
    return arr.find(function(val) {
        return val === searchValue;
    });
}

/*
Write a function called findInObj which accepts an array of objects, a key, and some value to search for and returns the first found value in the array.

Examples:
    findInObj([{first: 'Elie', last:"Schoppik"}, {first: 'Tim', last:"Garcia", isCatOwner: true}, {first: 'Matt', last:"Lane"}, {first: 'Colt', last:"Steele", isCatOwner: true}], 'isCatOwner',true) // {first: 'Tim', last:"Garcia", isCatOwner: true}
*/

// findInObj: Returns the first object where obj[key] === searchValue.
// Uses .find() to search for the first matching object.
function findInObj(arr, key, searchValue){
    return arr.find(function(obj) {
        return obj[key] === searchValue;
    });
} {}

/*
Write a function called removeVowels which accepts a string and returns a new string with all of the vowels (both uppercased and lowercased) removed. Every character in the new string should be lowercased.

Examples:
    removeVowels('Elie') // ('l')
    removeVowels('TIM') // ('tm')
    removeVowels('ZZZZZZ') // ('zzzzzz')
*/

// removeVowels: Returns a new string with all vowels removed and all characters lowercased.
// Uses .toLowerCase() and .replace() with a regex to remove vowels.
function removeVowels(str){
    return str.toLowerCase().replace(/[aeiou]/g, '');
}

/*
Write a function called doubleOddNumbers which accepts an array and returns a new array with all of the odd numbers doubled (HINT - you can use map and filter to double and then filter the odd numbers).

Examples:
    doubleOddNumbers([1,2,3,4,5]) // [2,6,10]
    doubleOddNumbers([4,4,4,4,4]) // []
*/

// doubleOddNumbers: Returns a new array with all odd numbers doubled.
// Uses .filter() to select odd numbers, then .map() to double them.
function doubleOddNumbers(arr){
    return arr.filter(function(val) {
        return val % 2 !== 0;
    }).map(function(val) {
        return val * 2;
    });
}
