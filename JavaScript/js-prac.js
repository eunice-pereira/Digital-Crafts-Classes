// ex 1. 

let value = 10 

if(value == 10) { 
    console.log("The value is 10.")
} else { 
    console.log("The value is not 10.")
}

value = 10 

// ex 2. 

let a = 20, b = 10 

a >= b ? result = 'higher' : result = 'lower'
console.log(result)

// ex 3. 

let temp = 50 
color = null 

switch(true) { 
    case(temp < 0): 
        color = "#5533FF";
        break; 
    case(temp < 30): 
        color = "#3334FF";
        break; 
    case(temp < 50): 
        color = "#3361FF";
        break; 
    case(temp < 75): 
        color = "#3380FF";
        break; 
    case(temp < 80): 
        color = "#FF5D33";
        break; 
    case(temp < 90): 
        color = "#FF5233";
        break; 
    case(temp > 90): 
        color = "#FF3333";
        break; 
}
console.log(color)