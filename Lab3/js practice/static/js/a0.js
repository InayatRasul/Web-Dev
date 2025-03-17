console.log(2 == '2');//converts data to same data type
console.log(2 === '2');//sompare value and data type

let a= [1,2,3,4];

// for(var i = 0;i < a.length;i++){ 
//     console.log(a[i]);
// }
//console.log(i)// returns 4, because var works as global variable
for(let i = 0;i < a.length;i++){ //use let
    console.log(a[i]);
}
// for(let v of a){
//     console.log(v);
// }

// a.forEach(
//     function(v){
//         console.log(v);
//     }
// )

// let i = 0;
// while(i < a.length){
// console.log(a[i]);
// i++;
// }
a.push(55);
a.pop();
a.indexOf(22);
a.find(function(v){
    if(v == 2){
        console.log('hi')
    }
})
sort 
slice 
a.slice(2,4);
splice
map 
filter 
reduce