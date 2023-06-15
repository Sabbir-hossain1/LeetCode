let isValid = function (s) {
  let stack = [];
  for (let idx = 0; idx < s.length; idx++) {
    if (s[idx] === "(") {
      stack.push(")");
    } else if (s[idx] === "{") {
      stack.push("}");
    } else if (s[idx] === "[") {
      stack.push("]");
    } else if (s[idx] !== stack.pop()) {
      return false;
    }
  }
  return !stack.length;
};

console.log(isValid("((()))"))
