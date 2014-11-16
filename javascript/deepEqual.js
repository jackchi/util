/**
 * JavaScript Utility to check if two Objects 
 * are equal in that they contain the same values
 * and they are isomorphic from each other
 * @param  {[any]} obj1 [object 1 for comparison]
 * @param  {[any]} obj2 [object 2 for comparison]
 * @return {[boolean]}      [recursively check the structure for equality]
 */
function deepEqual(obj1, obj2) {
  // recursively compare objects and non-nulls
  if (typeof obj1 == "object" && obj1 != null && typeof obj2 == "object" && obj2 != null) 
  {
    if (Object.keys(obj1).length != Object.keys(obj2).length) 
      return false;
    else {
      for (var prop in obj1) {
      	if (prop in obj2)
          return deepEqual(obj1[prop], obj2[prop]);
        else
          return false;
      }
      return true;
    }
  }
  // non-object comparisons
  else{
  	return obj1 === obj2;
  }
} 
var obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj)); // true
console.log(deepEqual(obj, {here: 1, object: 2})); // false
console.log(deepEqual(obj, {here: {is: "an"}, object: 2})); // true
console.log(deepEqual([1,2,3], [1,2,3])); // true
console.log(deepEqual([1,2,3], [1,2,3,3])); // false
console.log(deepEqual(null, null)); // true