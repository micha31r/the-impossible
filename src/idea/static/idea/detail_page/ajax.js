// Like button ajax
function comment_ajax(pk) {
    $(document).ready(
        function() {
            $.ajax(
                {
                    url: `/idea/comment/get/`,
                    data: {
                        'pk':pk,
                        'comment_num':comment_num,
                    },
                    dataType: 'json',
                    success: function(data) {
                        if (data.failed) {
                            console.log("Getting Comments Failed");
                        } else {
                            console.log(data)
                        }
                    }
                }
            );
        }
    );
}
