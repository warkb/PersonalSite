$(function () {
    $(document).on('mousemove', function (e) {
    	var browserWidth = document.body.clientWidth;
    	var browserHeight = document.body.clientHeight;
        $('#bgContainer').css({
            left: -e.pageX /10  - browserWidth / 10 + 10,
            top: -e.pageY / 10 - browserHeight / 10 - 10
        });
    });
});