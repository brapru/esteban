$(document).ready(function(){
        //connect to the socket server.
        var socket = io.connect('http://' + document.domain + ':' + location.port + '/scale');        
        socket.on('scale_update', function(weight) {
                $('#weight').text(weight)
        });
});
