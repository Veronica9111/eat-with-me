$(document).ready(function () {
    var placeDiv = $("#places");
    $.get('/places', function (data) {
        console.log(data); 
    });
});
