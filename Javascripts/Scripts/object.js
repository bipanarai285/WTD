let cat = {name:"Lucy", color:"golden", age:"3"};
let dog = new Object();
dog.breed = "husky";
dog.name = "jacky";
dog.isVaccinated = true;

document.getElementById("paral1").innerHTML = "breed: " + dog.breed + "<br>name:" + dog["name"];
console.log(dog);
delete dog.isVaccinated;
console.log(dog);

const person = {
    fname:"Bipana",
    lname:"Rai",
    age:20,
    fullname: function () {
        return this.fname + " " + this.lname
    }
};
console.log(person);
let x = 5;
let y = 6;
document.getElementById("paral1").innerHTML = person.fullname();