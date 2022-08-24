const input = document.getElementById("input");
const output = document.getElementById("output");
const url = "http://127.0.0.1:5000/";

const postData = async () => {
  const data = {};
  let i = 1;
  const myArray = input.value.split("\n");
  myArray.forEach((element) => {
    const s = "input".concat(i.toString());
    data[s] = element;
    ++i;
  });

  const response = await fetch(url, {
    method: "post",
    body: JSON.stringify(data),
  });

  output.innerHTML = await response.text();
};
