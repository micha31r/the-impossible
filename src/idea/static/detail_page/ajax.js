// Like button ajax
function like_ajax(id) {
    // $("#id_username").change(function () {
    // var username = $(this).val();
    $.ajax({
        url: `/idea/like/${id}`,
        data: {
            'username': username
        },
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                alert("A user with this username already exists.");
            }
        }
    });
    // });
}