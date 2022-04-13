function animal(){
    this.type="domestic"
}

let x = new animal();
let y = new animal();

x.name="dog";
y.animalname="cat";

animal.prototype.addName =()=>{
    console.log("name added");
}

y.addName();
x.addName();

Array.prototype.getEven = function(){
    let result=[];
    for(let i=0;i<this.length;i++){
        if(this[i]%2==0){
            result.push(this[i]);
        }
    }
    return result;
}