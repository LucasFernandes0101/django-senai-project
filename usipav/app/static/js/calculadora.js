const maxChars = 10;

const $visor = document.getElementById("visor");
let currentNumber = "";
let previousNumber = "";
let operator = "";
let result = "";

function pressNumber(num) {
  if (currentNumber.length < maxChars) {
    currentNumber += num;
    $visor.value = currentNumber;
  }
}

function pressDot() {
  if (currentNumber.length < maxChars && currentNumber.indexOf(".") === -1) {
    currentNumber += ".";
    $visor.value = currentNumber;
  }
}

function pressPlusMinus() {
  if (currentNumber !== "" && currentNumber !== "0") {
    currentNumber =
      currentNumber.charAt(0) === "-"
        ? currentNumber.slice(1)
        : "-" + currentNumber;
    $visor.value = currentNumber;
  }
}

function pressOperator(op) {
  if (currentNumber !== "") {
    if (previousNumber !== "") {
      result = calculateResult(previousNumber, currentNumber, operator);
      currentNumber = "";
      previousNumber = result;
    } else {
      previousNumber = currentNumber;
      currentNumber = "";
    }
    operator = op;
    $visor.value = previousNumber;
  }
}

function calculateResult(num1, num2, op) {
  let result;
  switch (op) {
    case "+":
      result = Number(num1) + Number(num2);
      break;
    case "-":
      result = num1 - num2;
      break;
    case "*":
      result = num1 * num2;
      break;
    case "/":
      if (num2 === "0") {
        alert("Erro: divisão por zero");
        clearCalc();
        return;
      } else {
        result = num1 / num2;
      }
      break;
  }
  return result.toFixed(4);
}

function calculate() {
  if (currentNumber !== "") {
    result = calculateResult(previousNumber, currentNumber, operator);
    currentNumber = result;
    previousNumber = "";
    operator = "";
    $visor.value = result;
  }
}

function clearCalc() {
  currentNumber = "";
  previousNumber = "";
  operator = "";
  result = "";
  $visor.value = "";
}
