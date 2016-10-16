'use strict';

var lightSensor;
$.ready(function (error) {
    if (error) {
        console.log(error);
        return;
    }

    $('#led-r').turnOn();
    lightSensor = $('#light');
    setInterval(showLightIntensity, 1000);
});

function showLightIntensity() {
    lightSensor.getIlluminance(function (error, value) {
        if (error) {
            console.error(error);
            return;
        }
        console.log('illuminance: ' + value);
    });
}

$.end(function () {
    $('#led-r').turnOff();
});
