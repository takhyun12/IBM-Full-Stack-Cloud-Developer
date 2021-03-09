function compute() {   //getting input value into the function
    var principal = document.getElementById("principal").value;
    var rate = document.getElementById("rate").value;
    var years = document.getElementById("years").value;

    if (principal <= 0) {
        window.alert("Enter a positive number");
        document.getElementById("principal").focus();
    } else {
        var interest = principal * rate * years / 100;
        var yearNow = new Date().getFullYear();
        var yearsFromNow = (+yearNow) + (+years);
        var result = document.getElementById("result");
        result.innerHTML =
            '<div>' +
            'If you deposit <span class="number" id="principalResult\">' + principal + '</span>,<br/>' +
            'at an interest rate of <span class="number" id="rateResult">' + rate + '%</span>.<br/>' +
            'You will receive an amount of <span class="number" id="interestResult">' + interest + '</span>,<br/>' +
            'in the year <span class="number" id="futureYearResult">' + yearsFromNow + '</span>.<br/>' +
            '</div>'
    }
}

function slider() { //display the value from slider
    var slideValue = document.getElementById("rate").value;
    document.getElementById("slider_value").innerHTML = slideValue + "%";
}