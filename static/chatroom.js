var ws = {
    socket: null,
    start: function() {
        var url = "ws://" + location.host + "/chatroom";
        ws.socket = new WebSocket(url);
        ws.socket.onmessage = function(event) {
            writeMessage(JSON.parse(event.data));
        };

        // Solved this issue 
        // https://github.com/johnidm/python-websocket-challenge/issues/2
        ws.onclose = function(){   
            setTimeout(function(){ ws.start() }, 1000);
        };
    }
};
ws.start();

var fakeAvatars = [
  'images/baby.png', 'images/cris.png',
  'images/corner.jpg', 'images/super.png',
  'images/dog.png', 'images/john.png',
  'images/mussun.png'
]

var avatar = fakeAvatars[Math.floor(Math.random() * fakeAvatars.length)];

var $messages = $('.messages-content');
$(window).load(function() {
    $messages.mCustomScrollbar();
});

function updateScrollbar() {
    $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
        scrollInertia: 10,
        timeout: 0
    });
}

function insertMessage() {
    var message = $('.message-input').val();

    var uuid = generateUUID();

    if ($.trim(message) == '') {
        return false;
    }
    $('<div class="message message-personal" uuid="' + uuid + '">' + message + '</div>').appendTo($('.mCSB_container')).addClass('new');

    sendMessageWS(message, uuid);
    updateScrollbar();

    $('.message-input').val(null);
}

$('.message-submit').click(function() {
    insertMessage();
});

$(window).on('keydown', function(e) {
    if (e.which == 13) {
        insertMessage();
        return false;
    }
})

function sendMessageWS(message, uuid) {
    var chat = {
        avatar: avatar,
        uuid, uuid,
        message: message
    }
    ws.socket.send(JSON.stringify(chat));
}

function writeMessage(message) {

    var existing = $('.message-personal[uuid="' + message.uuid + '"]');
    if (existing.length > 0) return;

    var avatar = message.avatar;

    $('<div class="message loading new"><figure class="avatar"><img src="' + avatar + '" /></figure><span></span></div>').appendTo($('.mCSB_container'));

    updateScrollbar();

    setTimeout(function() {
        $('.message.loading').remove();
        $('<div class="message new"><figure class="avatar"><img src="' + avatar + '" /></figure>' + message.message + '</div>').appendTo($('.mCSB_container')).addClass('new');
        updateScrollbar();
    }, 1000 + (Math.random() * 20) * 100);

}

function generateUUID() {
    var d = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
};