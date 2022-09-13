
function createCalendar(year,month){

    let tab = document.createElement("table");
    // tab.setAttribute("class","tab");
    // CSS
    // let tab = document.querySelector("table");
    tab.style.borderCollapse = "collapse";
    tab.style.width="50%";
    tab.style.fontFamily="Helvetica";
    tab.style.marginLeft="250px";
    tab.style.marginTop="100px";
    // 
    let tr = document.createElement("tr")
    let daily = ["MO","TU","WE","TH","FR","SA","SU"]
    
    for (let i = 0; i < 7; i++) {
        let th = document.createElement("th");
        let text = document.createTextNode(daily[i]);
        th.appendChild(text);
        tr.appendChild(th);
        tab.appendChild(tr);
        // CSS
        th.style.border="1px solid #ddd";
        th.style.padding ="15px";
        th.style.textAlign="left";
        // th.style.textAlign="center";
        th.style.backgroundColor="#04AA6D";
        th.style.color="white";

    }
    for (let e = 0; e < 5; e++) {
        let tr = document.createElement("tr")
        for (let i = 0; i < 7; i++) {
            let td = document.createElement("td");
            let text = document.createTextNode(".");
            td.appendChild(text);
            tr.appendChild(td);
            // CSS
            td.style.border="1px solid #ddd";
            td.style.padding ="15px";
            td.style.textAlign="center";
        }
        tab.appendChild(tr);
    }
    document.body.appendChild(tab);


    let d = new Date(year,month);
    let jour = d.getDay();
    let date = d.getDate();
    console.log(jour+"+++"+date);

    let tday = document.querySelectorAll("td");
    let debu = date;
    for (let d = jour-1; d < 35; d++) {
        if (month==0 || month == 2 || month == 4 || month == 6 || month == 7 || month == 9 || month == 11) {            
            if (debu<32) {                
                tday[d].innerHTML =debu;
                debu++;
            }
        } else if(month==1){
            if (debu<29) {                
                tday[d].innerHTML =debu;
                debu++;
            }
        } else{
            if (debu<31) {                
                tday[d].innerHTML =debu;
                debu++;
            }
        }
    }
}
createCalendar(2012,9);