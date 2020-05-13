// Subscribe to mailing list ajax
function subscribe_ajax(pk,username,encrypted_string) {
    $(document).ready(
        function() {
            $.ajax(
                {
                    url: `/idea/like/`,
                    data: {
                        'pk':pk,
                        'username':username,
                        'encrypted_string':encrypted_string
                    },
                    dataType: 'json',
                    success: function(data) {
                        if (data.failed) {
                            console.log("Like Failed");
                        } else {
                            $(`#like-count-${pk}`).html(data.updated_like_count);
                            $(`#like-count-${pk}`).attr('name', data.action);
                            $(`#like-svg-${pk}`).attr('name', data.action);
                        }
                    }
                }
            );
        }
    );
}