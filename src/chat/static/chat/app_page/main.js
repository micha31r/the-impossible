function fade(element_name) {
    animation_css = {
        'animation-name': 'fadein',
        'animation-duration': '0.3s',
        'animation-fill-mode': 'forwards',
    }
    if ($(element_name).css("opacity") == 0) {
        $(element_name).css(animation_css);
    } else {
        $(element_name).css('animation-name','fadeout');
    }
}

auto_run.queue(
    function() {
        // Focus on the input box when window loads
        $('#chat-message-input').focus();

        // Scroll to the bottom of chat log
        $('#chat-log-container').scrollTop($('#chat-log-container')[0].scrollHeight);

        // Send data when the enter key is pressed
        $('#chat-message-input').on(
            'keypress',
            function(event) {
                if(event.which == 13) {
                    // Only trigger send button if input is not empty
                    $('#chat-message-submit').click();
                }
            }
        );

        // Only show send button if input is not empty or contains more than space
        $("#chat-message-input").on(
            'change paste keyup',
            function() {
                if (($(this).val().replace(/ /g,"")).length > 0) {
                    $('#chat-message-submit').show();
                } else {
                    $('#chat-message-submit').hide();
                }
            }
        );

        // Hide button on page load
        $('#chat-message-submit').hide();
    }
);