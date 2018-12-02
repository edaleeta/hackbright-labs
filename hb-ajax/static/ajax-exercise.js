"use strict";


// PART 1: SHOW A FORTUNE

function showFortune(evt) {

    // TODO: get the fortune and show it in the #fortune-text div

    $.get('/fortune', (result)=> {
        $('#fortune-text').html(result);
    });
}

$('#get-fortune-button').on('click', showFortune);





// PART 2: SHOW WEATHER

function showWeather(evt) {
    evt.preventDefault();

    let url = "/weather.json";
    let formData = {"zipcode": $("#zipcode-field").val()};


    // TODO: request weather with that URL and show the forecast in #weather-info

    $.get(url, formData, (weather_info) => {
        $('#weather-info').html(weather_info['forecast']);
    });
}

$("#weather-form").on('submit', showWeather);




// PART 3: ORDER MELONS

function orderMelons(evt) {
    evt.preventDefault();

    // TODO: show the result message after your form

    let url = '/order-melons.json';
    let formData = {'melon_type': $('#melon-type-field').val(), 
                    'qty': $('#qty-field').val()};

    $.post(url, formData, showOrderStatus);

}

// TODO: if the result code is ERROR, make it show up in red (see our CSS!)


function showOrderStatus(result) {

    $('#order-status').html(result['msg']);

    if (result['code'] === 'ERROR') {
        $('#order-status').addClass('order-error');
    } else {
        $('#order-status').removeClass('order-error');
    }
}


$("#order-form").on('submit', orderMelons);


