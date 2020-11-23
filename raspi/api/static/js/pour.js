$(document).ready(function(){
        //connect to the socket server.
        var socket = io.connect('http://' + document.domain + ':' + location.port + '/pour');        
        socket.on('pour_update', function(data) {
                $('#message').text(data.message);
                $('#temperature').text(data.temperature);
                $('#weight').text(data.weight);
        });
});
