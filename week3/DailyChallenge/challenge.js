let solarSys = [{color:"red",planet:"Mercury"}, {color:"lightblue",planet:"Venus"}, {color:"blue",planet:"Earth"}, {color:"red",planet:"Mars"}, {color:"green",planet:"Jupiter"}, {color:"pink",planet:"Saturn"}, {color:"grey",planet:"Uranus"}, {color:"orange",planet:"Neptune"}];

solarSys.forEach(elem => {
    let text = document.createTextNode(elem.planet);
    console.log(text);
    let div = document.createElement("div");
    div.setAttribute("class","planet");
    div.appendChild(text);
    // 
    div.style.backgroundColor = elem.color;
    let sect = document.querySelector("section");
    sect.appendChild(div);
});
