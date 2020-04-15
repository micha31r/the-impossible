// Like button ajax
function like_post(pk,username) {
    $(".like-button").click(
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
                            $(".like-count").html(data.like_count);
                        }
                    }
                }
            );
        }
    );
}