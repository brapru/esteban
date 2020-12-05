$(document).ready(function(){
        //connect to the socket server.
        var socket = io.connect('http://' + document.domain + ':' + location.port + '/timer');        
        socket.on('timer', function(timer) {
                $('#timer').text(timer)
        });
});
