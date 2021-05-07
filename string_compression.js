const compressStringV1 = (str) => {
  let currentIndex = 0,
    output = "",
    encounters = 1,
    nextIndex = 1;

  while (true) {
    let currentValue = str[currentIndex];

    if (str[nextIndex] === currentValue) {
      encounters++;
      nextIndex++;
    } else {
      output += currentValue + String(encounters);
      currentIndex = nextIndex;
      nextIndex++;
      encounters = 1;
    }

    if (nextIndex === str.length + 1) {
      return output;
    }
  }
};

console.log(compressStringV1("aaabbaaccbacd"));
console.log(compressStringV1("aabb"));

const compressStringV2 = (str) => {
  let encounters = 1;
  let output = "";

  for (let i = 0; i < str.length; i++) {
    if (str[i] === str[i + 1]) {
      encounters += 1;
    } else {
      output += str[i] + String(encounters);
      encounters = 1;
    }
  }

  return output;
};

console.log(compressStringV2("aaabbaaccbacd"));
console.log(compressStringV2("aabb"));
