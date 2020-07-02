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
                            comment_num = data.new_comment_num;
                            data.comments = JSON.parse(data.comments);
                            for (var i=0; i<data.comments.length; i++) {
                                comment = data.comments[i];
                                author = data.authors[i];
                                $("#append-target2").append(
                                    `<div class="comment-wrapper">
                                    <h6>${comment.fields.full_description}</h6>
                                    <p class="small">${author}</p>
                                    <p class="small">Last Edited <span class="time">${comment.fields.last_edit}</span></p>
                                    </div>`
                                );
                            }
                            hide_button();
                        }
                    }
                }
            );
        }
    );
}

auto_run.queue( 
    hide_button
);

function hide_button() {
    if (total_comments_num <= comment_num) {
        $(".more-comment-btn").css("display","none");
    }
}
