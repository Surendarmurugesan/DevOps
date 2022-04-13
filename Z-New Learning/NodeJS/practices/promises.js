//First its execute the sync call, then execute in async calls 

var positive=true;

var result = new Promise((resolve,reject)=>{
    console.log("Im inside the promise")
    if(positive){
        resolve("I'm good");
    }
    else{
        reject("Its negative");
    }
});
console.log(result);
result.then(x=>{
    console.log(x)
}).catch(err=>{
    console.log(err);
}).finally(()=>{
    console.log("Im the final code")
})


console.log("Let u try")