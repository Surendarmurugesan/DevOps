function Person (){
    var name="Surendar";
    var age="38";
    this.firstName="Muruges";
}

var x = new Person();
console.log(typeof x);
console.log(x.firstName);

var Person2 = ()=>{
    this.lastName="JOHN"
}
var z = new Person2();
console.log(z);