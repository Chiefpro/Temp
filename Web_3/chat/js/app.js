

function send() {
    document.getElementById('message').value = "";
    console.log("Вывести сообщение чата")
}

function app() {
    //ввод данных
    //let x = parseInt(prompt("Введите х"))
    //let x = parseInt(document.getElementById('x').value)
    
    x = 2

    switch(true) {
        case (x ===0):
            alert("х = 0")
            
        case (x > 0 && x <= 100):
            alert("х В диапазоне от 1 до 100")
           
      
        case (x > 100):
            alert("x > 100")
            

    }


    if (x === 0) {
        
    } 

    if (x > 0 && x <= 100) {
        alert("х В диапазоне от 1 до 100")
    } 

    if (x > 100) {
        alert("х > 100")
    } 

    //логика
    //const result = x * x  
    
    //вывод данных
   // alert(`Квадрат х = ${result}`)
   //document.getElementById('result').innerText = result
}
