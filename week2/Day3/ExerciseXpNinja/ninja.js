// /////////////////////////////////////
//   Exercise 1 : Checking The BMI   
// ////////////////////////////////////
let obj1 = {
    FullName : "Jhon Doe",
    Mass : 63,
    Height : 1.83,
    BMI : function () {
        return this.Mass/(this.Height * this.Height);
    }
}
let obj2 = {
    FullName : "Alicia Keys",
    Mass : 60,
    Height : 1.78,
    BMI : function () {
        return this.Mass/(this.Height * this.Height);
    }
}

function compareBMI(ob1,ob2) {
    if (ob1.BMI() > ob2.BMI()) {
        console.log(ob1.FullName+" have the largest BMI: "+ob1.BMI())
    } else{
        console.log(ob2.FullName+" has the largest BMI: "+ob2.BMI())
    }
}

compareBMI(obj1,obj2);

// /////////////////////////////////////
//   Exercise 2 : Grade Average
// ////////////////////////////////////

function findAvg(gradesList) {
    let average=0;
    for (const i of gradesList) {
        average=average+i;
    }
    decision(average=average/gradesList.length);
}


function decision(params) {
    if (params>65) {
       console.log(params+" : You passed")
    } else{
        console.log(params+" : You failed and must repeat the course.")
    }
}

findAvg([44,10,67,75,70]);