function addition() {

    var ourAnswer = document.getElementById("answer").value;
    isNaN(ourAnswer);
    if (isNaN(ourAnswer)){
        document.getElementById("output").innerHTML = "Nope!"  +  ourAnswer  +  "is not a Number";
    } else {
        if (ourAnswer == correctAnswer){
            document.getElementById("output").innerHTML = "Correct,The answer is ="  +  correctAnswer;
        } else {
            document.getElementById("output").innerHTML = "Incorrect,The correct answer is"  +  correctAnswer; 
        }
    }
    

}

function newCard() {
    document.getElementById("output").innerHTML = "";
    document.getElementById("answer").value = "";
    num1 = Math.floor(Math.random() * 50) + 1;
    num2 = Math.floor(Math.random() * 50) + 1;
    document.getElementById("demo").innerHTML = num1 + "+" + num2;
    correctAnswer = num1 + num2

}
