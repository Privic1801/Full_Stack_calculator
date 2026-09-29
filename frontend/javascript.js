expression = ""
let display = document.getElementById("display");
let numberButtons = document.querySelectorAll(".numbers");
let operatorButtons = document.querySelectorAll(".operator")
let equalButton = document.querySelector(".equal")
let clearButton = document.querySelector(".clear")
let decimalButton = document.querySelector(".decimal")
let backspaceButton = document.querySelector(".backspace")
let justCalculated = false

let operators = ['+', '-', '*', '/', '%']

numberButtons.forEach(function(button){
    button.addEventListener("click", function(event){
        if (justCalculated){
            display.value = event.target.textContent
            expression = event.target.textContent
            justCalculated = false
        }
        else if (display.value === '0'){
            display.value = event.target.textContent
            expression = expression + event.target.textContent
        }
        else{
            display.value = display.value + event.target.textContent;
            expression = expression + event.target.textContent
        }
    
    });
});

operatorButtons.forEach(function(button){
    button.addEventListener("click", function(event){
        let operator = event.target.textContent
        if (operator === "x"){
            operator = "*"
        }
        let lastCharacter = expression[expression.length - 1]
        if (justCalculated){
            justCalculated = false
        }
        if (operator === "-" && (expression === "" || operators.includes(lastCharacter))){
            expression = expression + operator
            if (expression === "-"){
                display.value = "-"
            }
            
        }
        else if (operators.includes(lastCharacter)){
        }
        else{
            expression = expression + operator
            display.value = display.value + event.target.textContent
        }
    })
})

equalButton.addEventListener("click", function(event){
    fetch("https://full-stack-calculator-api.onrender.com/calculate",{
        method: "POST",
        headers :{
            "Content-Type" : "application/json"
        },
        body :JSON.stringify({
            expression: expression
        })
    })
    .then(function(response){
        if (response.ok){
            return response.json()
        }
        else{
            return response.json().then(function(data){
                throw new Error(data.detail)
            })
        }
    })
    .then(function(data){
        display.value = data.Result
        expression = String(data.Result)
        justCalculated = true
    })
    .catch(function(error){
        display.value = error.message
        expression = ""
        justCalculated = false
    })
})

clearButton.addEventListener("click", function(event){
    display.value = "0"
    expression = ""
    justCalculated = false

})

decimalButton.addEventListener("click", function(event){
    let lastOperatorIndex = -1
    operators.forEach(function(operator){
        let index = expression.lastIndexOf(operator)
        if (index > lastOperatorIndex){
            lastOperatorIndex = index
        }

})
let currentNumber = expression.slice(lastOperatorIndex + 1)
if (!currentNumber.includes(".")){
    expression = expression + "."
    display.value = display.value + "."
}

})

backspaceButton.addEventListener("click", function(event){
    if(expression.length > 0){
        expression = expression.slice(0, -1)
        display.value = display.value.slice(0, -1)
    }
    if (expression === ""){
        display.value = "0"
    }
})