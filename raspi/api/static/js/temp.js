$(document).ready(function(){
        //connect to the socket server.
        var socket = io.connect('http://' + document.domain + ':' + location.port + '/temp');        
        socket.on('temp_update', function(fahr) {
                $('#fahr').text(fahr)
        });
});
