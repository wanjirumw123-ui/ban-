let outputscreen = document.getElementById('output-screen')
let buttons = document.querySelectorAll('button')

function display (num){
    outputscreen.value +=num
}

function calculate () {
    try{
        outputscreen.value = eval(outputscreen.value)
    }
    catch (err){
        alert("invalid")
    }
}


function Ac (){
    outputscreen.value=''
}

function Del(){
    outputscreen.value = outputscreen.value.slice(0.-1)
}