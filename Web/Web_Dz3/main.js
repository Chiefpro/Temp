// let a = Number.parseInt(prompt("Введи число А "));
// let b = Number.parseInt(prompt("Введи число B "));
// alert(`Результат сложения ${a} и ${b} = ${a + b}`);

// const cels = +prompt("Введи температуру в цельсиях: ");
// const farenh = (cels + 32) * 9 / 5;
// alert(`Цельсия: ${cels}, Фаренгейт: ${Math.round(farenh * 100) / 100}`);


// function sum(n1, n2) {
//     const n3 = n1 + n2;
//     return n3;
// }

// alert(`Результат сложения через функцию ${a} и ${b} = ${sum(a, b)}`);

// const life = confirm("Хорошо живется? ");
// console.log(life);
// if (life){
//     alert("Тогда мы имем к вам!!")
// } else {
//     alert("Ну, догда держись там!!")
// }

// const life2 = (confirm("Хорошо живется? ")) ? alert("OKKKKKKK") : alert("NOOOOOOO");

// -----------------------------------------------------------------------------------------------------------------------

greeting(prompt("Введите пожалуйста Ваше имя => "));

function greeting(name) {
    console.log(`Привет ${name}`);
}