// => short hand operator

const z = (x,y) => x+y;

    // In detail: Both are the same:
// const z = (x,y) => {
//     return x+y;
// }

console.log(z(4,3));

// reduce function:: it takes first two values execute addition, after that return the output to X value, then Y takes 3rd value ,do addition

const marks = [10,20,30,40,50];
const totalMarks = marks.reduce((x,y) => x+y);
console.log(totalMarks)

//const sortedArray = marks.sort((x,y)=>y-x); // descending order(another method)
const sortedArray = marks.sort((x,y)=>x+y);
console.log(sortedArray)            // Ascending order
console.log(sortedArray.reverse())  // descending order


//map function:::
//filter function:::

const Scorecard = marks.map((item,index)=>{
    return {score:item};
}).filter(x=>{
    return x.score>=20
});
console.log(Scorecard)
//console.log(Scorecard.reverse())


const sortMarks = marks.
    sort((x,y)=> x - y)
    .map((item,index) => {
        return {score:item};
    }).filter(x=>{
    return x.score<=20
});
console.log(sortMarks)

// find = to find the value
// Index = to find the value location.
const isExisting = Scorecard.find(x=>x.score==30);
const indexOfItem = Scorecard.findIndex(x=>x.score==30);
//console.log(Scorecard);
console.log(isExisting);
console.log(indexOfItem);
