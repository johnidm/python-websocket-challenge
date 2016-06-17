$(document).ready(function() {

    var fakeNames = [
        "Darian Sanford",
        "Geovany Kunze",
        "Chasity Schmeler",
        "Caitlyn Kerluke"
    ]
    $("span[name=user").html(fakeNames[Math.floor(Math.random() * fakeNames.length)]);

    var ws = {
        socket: null,
        start: function() {
            var url = "ws://" + location.host + "/chatroom";
            ws.socket = new WebSocket(url);
            ws.socket.onmessage = function(event) {
                writeMessage(JSON.parse(event.data));
            };
        }
    };

    ws.start(); 

    $("button[name='send']").click(function() {
        var message = $("textarea[name='message']")[0]; 
        var user = $("span[name=user").text();

        var chat = {
            user: user,
            message: message.value
        }
        ws.socket.send(JSON.stringify(chat));

        message.value = '';
    });

    var writeMessage = function(message) {
        var template = '<p>' + message.user + ' |  ' + message.message + ' | ' + message.date + '<p>'
        $('messages').append(template);
    }
});