const btn_convert = document.getElementById("convert_pul");
const input_az = document.getElementById("az");
const input_dollar = document.getElementById("dollar");

//*
const convert_data = (e) => {
  input_dollar.value = `${(input_az.value / 1.7).toFixed(2)} $ `;
};
btn_convert.addEventListener("click", convert_data);
