//* container
const container = document.createElement("div");
container.classList.add("container");
document.body.append(container);

//* box

for (let i = 0; i < 8; i++) {
  for (let j = 0; j < 8; j++) {
    const box = document.createElement("div");
    box.classList.add("box", (i + j) % 2 === 0 ? "white" : "blue");
    container.append(box);

    if (j == 7) {
      const number = document.createElement("p");
      number.classList.add("number");
      number.textContent = `${8 - i}`;
      box.append(number);
    }
   

    if (i == 7) {
      const letter = document.createElement("p");
      letter.classList.add("letter");
      letter.textContent = String.fromCharCode(`${j + 97}`);
      box.append(letter);
    }
  }
}
