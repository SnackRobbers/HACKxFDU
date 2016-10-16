'use strict';

$.ready(function (error) {
    if (error) {
        console.error(error);
        return;
    }
    $('#lcd1602-02').print('By M$ , Ruff', function (error) {
        if (error) {
            console.log(error);
            return;
        }
        console.log('printed');
    });
    // ...
});

$.end(function () {
    // ...
});
