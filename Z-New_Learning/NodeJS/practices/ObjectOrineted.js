class Profile {
    constructor(){
        this.username="Suren";
        this.age=26;
    }
    getFullName(){
        return this.username+this.age;
    }
}

const x = new Profile();
console.log(x);

// By default, its all in public.