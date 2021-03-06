function getBathroomValue(){
    console.log("Bathroom Value");
    var uiBath = document.getElementByName("uiBathroom");
    for(var i in uiBath){
        if(uiBath[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1; // invalid value
}
function getBedroomValue(){
    var uibedroom = document.getElementbyName("uibedrooms");
    console.log("Bedroom Value")
    for(var i in uibedroom){
        if(uibedroom[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1; //invalid value
}
function getCarValue(){
    var uicar = document.getElementbyName("uicar");
    for(var i in uicar){
        if(uicar[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1; //invalid value
}

function onClickedEstimatePrice(){
    alert("Estimated Price button clicked");
    var sqm = document.getElementById("uiSqm");
    var bedrooms = getBedroomValue();
    var bathroom = getBathroomValue();
    var car = getCarValue();
    var dist = document.getElementById("uidist");
    var suburb = document.getElementById("uisuburb");
    var estPrice = document.getElementById("uiEstimatedPrice");
    var url = "http://127.0.0.1:5000/predict_home_price";
    alert(estPrice);
    $.post(url,{
        sqm: parseFloat(sqm.value),
        bedrooms: bedrooms,
        bathroom: bathroom,
        car: car,
        distance: parseFloat(dist.value),
        suburb: suburb.value
    }, function(data,status){
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "AUD</h2>";
        console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded")
    var url ="http://127.0.0.1:5000/get_suburb_names";
    $.get(url,function(data,status){
        console.log("got response for get_suburb_names request");
        if(data){
            var suburb = data.suburbs;
            var uisuburb = document.getElementById("uisuburb");
            $('#uisuburb').empty();
            for (var i in suburb){
                var opt = new Option(suburb[i]);
                $('#uisuburb').append(opt);
            }
        }
    });
}
window.onload = onPageLoad();