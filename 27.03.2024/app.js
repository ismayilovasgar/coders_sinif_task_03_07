// let num1 = +prompt("birinci ededi daxil edin");
// let num2 = +prompt("ikinci ededi daxil edin");
// let sum = num1 + num2;

// if (sum % 2 === 0) {
//   console.log(
//     ` ${num1} ve ${num2} ededlerinin cemi ${sum} ve  ${sum} cut ededdir`
//   );
// } else {
//   console.log(
//     ` ${num1} ve ${num2} ededlerinin cemi ${sum} ve  ${sum} tek ededdir`
//   );
// }

let soz = prompt("soz daxil edin");

// let count = 0;
// let soz_index = soz.length - 1;
// for (let i = 0; i < soz_index; i++) {
//   if (soz.charAt(i) === "a") {
//     count++;
//   }
// }
// console.log(count);

let soz_replace = soz.replace(/[a-z]/gi, "");
console.log(soz_replace);
