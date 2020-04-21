// Like button ajax
function like_post(pk,username) {
    $(document).ready(
        function() {
            $.ajax(
                {
                    url: `/idea/like/`,
                    data: {
                        'pk':pk,
                        'username':username
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