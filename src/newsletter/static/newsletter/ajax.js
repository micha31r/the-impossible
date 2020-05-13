// Subscribe to mailing list ajax
function join_newsletter_ajax(email) {
    $(document).ready(
        function() {
            $.ajax(
                {
                    url: `/newsletter/join/`,
                    data: {
                        'email':email,
                    },
                    dataType: 'json',
                    success: function(data) {
                        if (data.failed) {
                            console.log("Join Failed");
                        } else {
                            
                        }
                    }
                }
            );
        }
    );
}