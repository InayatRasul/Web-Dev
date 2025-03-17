// variable scoping mean limitation of variable access in some block

var s_name = {
    name: "Student 1",
    age: 20,
    gpa: 3.9
}
function h1(){
    if(s_name['gpa'] >= 3.5){
        var a = s_name['age'];
        console.log("hello " + s_name['name']);
    }else{
        console.log("Student gpa less than 3.5");
    }
    console.log(a); //20 with var, nothing with let
    // a links to the parent element whereas let copy data
}

h1();